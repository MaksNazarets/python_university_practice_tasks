import http.client
import json
import tkinter as tk
from tkinter import font
from tkinter.constants import ANCHOR, GROOVE, LEFT, RAISED, RIDGE, SUNKEN
import tkinter.ttk as ttk
from datetime import datetime


def combo_selected(event):
    global combo
    get_info(countries[combo.current()])

def get_info(country):
    for i in data:
        if i["Country"] == country:
            total_cases_number.configure(text=i['TotalCases'])
            new_cases_number.configure(text=i['NewCases'])
            new_deaths_number.configure(text=i['NewDeaths'])
            total_deaths_number.configure(text=i['TotalDeaths'])
            new_recovered_number.configure(text=i['NewRecovered'])
            total_recovered_number.configure(text=i['TotalRecovered'])
            case_fatality_rate_number.configure(text=i['Case_Fatality_Rate'])
            active_cases_number.configure(text=i['ActiveCases'])
            total_tests_number.configure(text=i['TotalCases'])
            infection_risc_number.configure(text=i['Infection_Risk'])

def refresh():
    global headers, conn, res, data, countries, combo, last_update_date

    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

    headers = {
    'x-rapidapi-key': "a7e52c0917msh2b786bc8814a02dp1fe800jsn8714ff36dedd",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    conn.request("GET", "/api/npm-covid-data/", headers=headers)

    res = conn.getresponse()
    data = json.loads(res.read().decode('utf-8'))

    countries = sorted([i["Country"] for i in data])
    get_info(countries[combo.current()])
    last_update_date.configure(text=datetime.today().strftime("%d.%m.%Y\n%H:%M:%S"))


window = tk.Tk()
window.title("task 3")
window.geometry('920x445')
window.resizable(width=False, height=False)
window.pack_propagate()

frameTop = tk.Frame(window, bg='#242424', padx=10, pady=10)
frameTop.place(relwidth=1, relheight=1)

combo_font = [('Calibri bold', 21), ('Calibri', 20)]

frameBottom = tk.Frame(frameTop, bg='#292929', pady=17)
frameBottom.place(relwidth=1, height=370, y=55)

refreshButton = tk.Button(frameTop, text="REFRESH", font=('Calibri bold', 15), command=refresh)
refreshButton.place(relwidth=0.49, relx=0.51)

info_font = [("Arial bold", 19), ("Calibri", 19)]
info_pady = 7
info_padx = 3
info_bg = '#292929'
info_fg = 'white'

total_cases_lbl = tk.Label(frameBottom, text="Total cases: ", font=info_font[0], bg=info_bg, fg=info_fg,  width=19, anchor='w')
total_cases_lbl.grid(column=0, row=0, pady=info_pady, padx=info_padx )

new_cases_lbl = tk.Label(frameBottom, text="New cases: ", font=info_font[0], bg=info_bg, fg=info_fg,  width=19, anchor='w')
new_cases_lbl.grid(column=0, row=1, pady=info_pady, padx=info_padx)

new_deaths_lbl = tk.Label(frameBottom, text="New deaths: ", font=info_font[0], bg=info_bg, fg=info_fg,  width=19, anchor='w')
new_deaths_lbl.grid(column=0, row=2, pady=info_pady, padx=info_padx)

total_deaths_lbl = tk.Label(frameBottom, text="Total deaths: ", font=info_font[0], bg=info_bg, fg=info_fg,  width=19, anchor='w')
total_deaths_lbl.grid(column=0, row=3, pady=info_pady, padx=info_padx)

new_recovered_lbl = tk.Label(frameBottom, text="New recovered: ", font=info_font[0], bg=info_bg, fg=info_fg,  width=19, anchor='w')
new_recovered_lbl.grid(column=0, row=4, pady=info_pady, padx=info_padx)

total_recovered_lbl = tk.Label(frameBottom, text="Total recovered: ", font=info_font[0], bg=info_bg, fg=info_fg,  width=17, anchor='w')
total_recovered_lbl.grid(column=2, row=0, pady=info_pady, padx=info_padx)

case_fatality_rate_lbl = tk.Label(frameBottom, text="Case fatality rate: ", font=info_font[0], bg=info_bg, fg=info_fg,  width=17, anchor='w')
case_fatality_rate_lbl.grid(column=2, row=1, pady=info_pady, padx=info_padx)

active_cases_lbl = tk.Label(frameBottom, text="Active cases: ", font=info_font[0], bg=info_bg, fg=info_fg,  width=17, anchor='w')
active_cases_lbl.grid(column=2, row=2, pady=info_pady, padx=info_padx)

total_tests_lbl = tk.Label(frameBottom, text="Total tests: ", font=info_font[0], bg=info_bg, fg=info_fg,  width=17, anchor='w')
total_tests_lbl.grid(column=2, row=3, pady=info_pady, padx=info_padx)

infection_risc_lbl = tk.Label(frameBottom, text="Infection risk: ", font=info_font[0], bg=info_bg, fg=info_fg,  width=17, anchor='w')
infection_risc_lbl.grid(column=2, row=4, pady=info_pady, padx=info_padx)



total_cases_number = tk.Label(frameBottom, text="0", font=info_font[1], bg=info_bg, fg=info_fg,  width=10, anchor='w')
total_cases_number.grid(column=1, row=0, pady=info_pady, padx=info_padx )

new_cases_number = tk.Label(frameBottom, text="0", font=info_font[1], bg=info_bg, fg=info_fg,  width=10, anchor='w')
new_cases_number.grid(column=1, row=1, pady=info_pady, padx=info_padx)

new_deaths_number = tk.Label(frameBottom, text="0", font=info_font[1], bg=info_bg, fg=info_fg,  width=10, anchor='w')
new_deaths_number.grid(column=1, row=2, pady=info_pady, padx=info_padx)

total_deaths_number = tk.Label(frameBottom, text="0", font=info_font[1], bg=info_bg, fg=info_fg,  width=10, anchor='w')
total_deaths_number.grid(column=1, row=3, pady=info_pady, padx=info_padx)

new_recovered_number = tk.Label(frameBottom, text="0", font=info_font[1], bg=info_bg, fg=info_fg,  width=10, anchor='w')
new_recovered_number.grid(column=1, row=4, pady=info_pady, padx=info_padx)

total_recovered_number = tk.Label(frameBottom, text="0", font=info_font[1], bg=info_bg, fg=info_fg,  width=10, anchor='w')
total_recovered_number.grid(column=3, row=0, pady=info_pady, padx=info_padx)

case_fatality_rate_number = tk.Label(frameBottom, text="0", font=info_font[1], bg=info_bg, fg=info_fg,  width=10, anchor='w')
case_fatality_rate_number.grid(column=3, row=1, pady=info_pady, padx=info_padx)

active_cases_number = tk.Label(frameBottom, text="0", font=info_font[1], bg=info_bg, fg=info_fg,  width=10, anchor='w')
active_cases_number.grid(column=3, row=2, pady=info_pady, padx=info_padx)

total_tests_number = tk.Label(frameBottom, text="0", font=info_font[1], bg=info_bg, fg=info_fg,  width=10, anchor='w')
total_tests_number.grid(column=3, row=3, pady=info_pady, padx=info_padx)

infection_risc_number = tk.Label(frameBottom, text="0", font=info_font[1], bg=info_bg, fg=info_fg,  width=10, anchor='w')
infection_risc_number.grid(column=3, row=4, pady=info_pady, padx=info_padx)

last_update_lbl = tk.Label(frameBottom, text="Last info update:\t", font=('Calibri italic', 15), bg='#242424', fg=info_fg,  width=72, height=2, anchor='e', pady=7)
last_update_lbl.grid(column=0, row=5, pady=40, padx=0, columnspan=3)

last_update_date = tk.Label(frameBottom, text="No data", font=('Calibri italic', 15), bg='#242424', fg=info_fg,  width=17, height=2, anchor='w', pady=7)
last_update_date.grid(column=3, row=5, pady=40, padx=0)


combo = ttk.Combobox(frameTop, font=combo_font[0], state='readonly')
window.option_add('*TCombobox*Listbox.font', combo_font[1])

refresh()

combo['values'] = (countries)
combo.current(countries.index("Ukraine"))
combo.place(relwidth=0.5)

combo.bind("<<ComboboxSelected>>", combo_selected)

refresh()


window.mainloop()