import telebot
from telebot import types
import http.client
import json


TOKEN = '1735368244:AAEI8MeEV-UBCOERReeALFTjg9j105kYI14'
tb = telebot.TeleBot(TOKEN)
chat_id = ''

def get_data():
    global headers, conn, res, data, countries

    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

    headers = {
    'x-rapidapi-key': "a7e52c0917msh2b786bc8814a02dp1fe800jsn8714ff36dedd",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    conn.request("GET", "/api/npm-covid-data/", headers=headers)

    res = conn.getresponse()
    data = json.loads(res.read().decode('utf-8'))
    countries = sorted([i["Country"] for i in data])



@tb.message_handler(commands=['get_file'])
def get_file_stat(message):
    with open(f'files/stat_{country["Country"]}.txt', 'w') as file:
        file.write(stat)
                
    with open(f'files/stat_{country["Country"]}.txt', 'rb') as file:
        tb.send_document(chat_id, file)
        

@tb.message_handler(content_types=['text'])
def test(message):
    get_data()
    if message.text in countries:
        global country, stat, chat_id
        chat_id = message.chat.id
        country = {}
        for i in data:
            if i["Country"] == message.text:
                country = i
                
        stat = f'''
<b>Current COVID-19 situation in {message.text}</b>\n
Total cases:                {country["TotalCases"]}
New cases:                  {country["NewCases"]}
New deaths:                 {country["NewDeaths"]}
Total deaths:               {country["TotalDeaths"]}
New recovered:              {country["NewRecovered"]}
Total recovered:            {country["TotalRecovered"]}
Case fatality rate:         {country["Case_Fatality_Rate"]}
Active cases:               {country["ActiveCases"]}
Total cases:                {country["TotalCases"]}
Infection risk:             {country["Infection_Risk"]}
                '''
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        get_file_btn = types.KeyboardButton("/get_file")

        markup.add(get_file_btn)

        tb.send_message(message.chat.id, stat, parse_mode='html', reply_markup=markup)

    else:
        tb.send_message(message.chat.id, 'Sorry, I don\'t know this country...')


tb.polling(none_stop=True)

while True:
    pass
