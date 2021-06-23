import tkinter as tk
from tkinter.constants import BOTTOM, DISABLED, E, RIGHT, TOP
import math

# Processing of pressing some buttons

funcPairs = {
    'ln': 'math.log',
    'log': 'math.log',
    'tan': 'math.tan',
    'ctg': 'myCtgFun',
    'sin': 'math.sin',
    'cos': 'math.cos'
}

def btnPress(btn_text):
    global expression, result_text, is_bin_displayed, top_text

    if expression == 'Error!' or is_bin_displayed:
        is_bin_displayed = False
        top_text.set('')
        expression = ''
        checkEmpty()

    if btn_text not in ['cos', 'sin', 'tan', 'ctg', 'log', 'ln', '%']:
        if btn_text in ['0', '*', '/', '+'] and len(expression) == 0:
            return

        if len(expression) > 0 and btn_text in ['*', '/', '+', '-'] and expression[len(expression) - 1] in ['*', '/', '+', '-']:
            return 

        if btn_text == '.' and len(expression) == 0:
            expression += '0.'
            result_text.set('0.')
            return

        if len(expression) == 0:
            result_text.set('')

        expression += btn_text
        result_text.set(result_text.get() + btn_text)

    elif btn_text != '%':
        if len(expression) == 0:
            result_text.set('')

        expression += funcPairs[btn_text] + '('
        result_text.set(result_text.get() + btn_text + '(')
        return
        
    elif len(expression) > 0:
        expression += '*0.01'
        result_text.set(result_text.get() + '%')

    print(expression)
    

# Processing of pressing 'equal' button

def equalsPress():
    global result_text, expression, top_text
    try:
        expression += ')' * (expression.count('(') - expression.count(')'))
        top_text.set(result_text.get() + ')' * (result_text.get().count('(') - result_text.get().count(')')) + '=')

        expression = str(eval(expression))
        result_text.set(expression)
    except:
        expression = 'Error!'
        result_text.set(expression)

# Processing of pressing 'clear' and 'erase' buttons

def clearPress():
    global result_text, expression, is_bin_displayed
    is_bin_displayed = False
    expression = ''
    result_text.set('0')
    top_text.set('')

def erasePress():
    global result_text, expression

    if len(result_text.get()) > 3 and result_text.get()[-4:-1] in ['cos', 'sin', 'tan', 'ctg', 'log']:
        expression = expression[:-9]
        result_text.set(result_text.get()[:-4])
    elif len(result_text.get()) > 2 and result_text.get()[-3:-1] == 'ln':
        expression = expression[:-9]
        result_text.set(result_text.get()[:-3])
    elif result_text.get()[-1] == '%' :
        expression = expression[:-5]
        result_text.set(result_text.get()[:-1])
    else:    
        expression = expression[:-1]
        result_text.set(result_text.get()[:-1])

    print(expression)
    checkEmpty()


# my ctg function

def myCtgFun(number):
    return 1 / math.tan(number)    



def checkEmpty():
    global result_text
    if len(result_text.get()) == 0:
        result_text.set('0')


# Conversion to binary

is_bin_displayed = False
def to_bin():
    global result_text, top_text, expression, is_bin_displayed
    try:
        is_bin_displayed = True
        top_text.set(result_text.get() + " (DEC)")
        expression = bin(eval(expression))[2:]
        result_text.set(expression + ' (BIN)')
    except:
        result_text.set("Error!")


# Functions, processing of pressing keys

def key_pressed(event):
    if ord(event.char) in range(40, 44) or ord(event.char) in range(45, 58) or event.char == '%':
        btnPress(event.char)

def backspace_pressed(event):
    erasePress()

def enter_pressed(event):
    equalsPress()

def delete_pressed(event):
    clearPress()

# GUI settings

window = tk.Tk()
window['bg'] = '#242424'
window.title("Task 2")
window.geometry('685x363')
window.wm_attributes('-alpha', 0.97)
window.resizable(width=False, height=False)

frame = tk.Frame(window, bg='#242424', padx=5, pady=5)
frame.place(relwidth=1, relheight=1)

expression = ''
result_text = tk.StringVar()
result_text.set("0")
top_text =tk.StringVar()


topTxtField = tk.Entry(frame, bg='#4a4a4a', fg='white', font=('Consolas', 19), justify=RIGHT, state=DISABLED, textvariable=top_text)
topTxtField.place(relwidth=1)

txtField = tk.Entry(frame, bg='white', fg='black', font=('Consolas', 27), justify=RIGHT, state=DISABLED, textvariable=result_text)
txtField.place(relwidth=1, y=35)

numFrame = tk.Frame(frame, bg='#242424', width=100, height=100)
numFrame.place(relwidth=1, height=450, y=85)

btnFontFamily = 'Consolas'
btnFontSize = 23
numForeground = 'black'
funcForeground = 'black'
funcBg = '#d1d1d1'

btn1 = tk.Button(numFrame, text='1', height=1, width=5, bg='white', fg=numForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('1'))
btn1.grid(pady=1, padx=1, row=1, column=1)

btn2 = tk.Button(numFrame, text='2', height=1, width=5, bg='white', fg=numForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('2'))
btn2.grid(pady=1, padx=1, row=1, column=2)

btn3 = tk.Button(numFrame, text='3', height=1, width=5, bg='white', fg=numForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('3'))
btn3.grid(pady=1, padx=1, row=1, column=3)

btn4 = tk.Button(numFrame, text='4', height=1, width=5, bg='white', fg=numForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('4'))
btn4.grid(pady=1, padx=1, row=2, column=1)

btn5 = tk.Button(numFrame, text='5', height=1, width=5, bg='white', fg=numForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('5'))
btn5.grid(pady=1, padx=1, row=2, column=2)

btn6 = tk.Button(numFrame, text='6', height=1, width=5, bg='white', fg=numForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('6'))
btn6.grid(pady=1, padx=1, row=2, column=3)

btn7 = tk.Button(numFrame, text='7', height=1, width=5, bg='white', fg=numForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('7'))
btn7.grid(pady=1, padx=1, row=3, column=1)

btn8 = tk.Button(numFrame, text='8', height=1, width=5, bg='white', fg=numForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('8'))
btn8.grid(pady=1, padx=1, row=3, column=2)

btn9 = tk.Button(numFrame, text='9', height=1, width=5, bg='white', fg=numForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('9'))
btn9.grid(pady=1, padx=1, row=3, column=3)

btn0 = tk.Button(numFrame, text='0', height=1, width=5, bg='white', fg=numForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('0'))
btn0.grid(pady=1, padx=1, row=4, column=2)

btn_point = tk.Button(numFrame, text='.', height=1, width=5, bg='white', fg=numForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('.'))
btn_point.grid(pady=1, padx=1, row=4, column=1)

btn_equals = tk.Button(numFrame, text='=', height=1, width=5, bg='#696969', fg='white', font=(btnFontFamily, btnFontSize), command=lambda:equalsPress())
btn_equals.grid(pady=1, padx=1, row=4, column=3)


btn_plus = tk.Button(numFrame, text='+', height=1, width=5, bg=funcBg,fg=funcForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('+'))
btn_plus.grid(pady=1, padx=1, row=3, column=4)

btn_minus = tk.Button(numFrame, text='-', height=1, width=5, bg=funcBg,fg=funcForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('-'))
btn_minus.grid(pady=1, padx=1, row=3, column=5)

btn_mult = tk.Button(numFrame, text='*', height=1, width=5, bg=funcBg,fg=funcForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('*'))
btn_mult.grid(pady=1, padx=1, row=2, column=4)

btn_div = tk.Button(numFrame, text='/', height=1, width=5, bg=funcBg,fg=funcForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('/'))
btn_div.grid(pady=1, padx=1, row=2, column=5)

btn_clear = tk.Button(numFrame, text='C', height=1, width=5, bg=funcBg,fg=funcForeground, font=(btnFontFamily, btnFontSize), command=lambda:clearPress())
btn_clear.grid(pady=1, padx=1, row=1, column=6)

btn_erase1 = tk.Button(numFrame, text='←', height=1, width=5, bg=funcBg,fg=funcForeground, font=(btnFontFamily, btnFontSize), command=lambda:erasePress())
btn_erase1.grid(pady=1, padx=1, row=1, column=7)

btn_sin = tk.Button(numFrame, text='sin', height=1, width=5, bg=funcBg,fg=funcForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('sin'))
btn_sin.grid(pady=1, padx=1, row=2, column=6)

btn_cos = tk.Button(numFrame, text='cos', height=1, width=5, bg=funcBg,fg=funcForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('cos'))
btn_cos.grid(pady=1, padx=1, row=2, column=7)

btn_tan = tk.Button(numFrame, text='tan', height=1, width=5, bg=funcBg,fg=funcForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('tan'))
btn_tan.grid(pady=1, padx=1, row=3, column=6)

btn_ctg = tk.Button(numFrame, text='ctg', height=1, width=5, bg=funcBg,fg=funcForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('ctg'))
btn_ctg.grid(pady=1, padx=1, row=3, column=7)

btn_percent = tk.Button(numFrame, text='%', height=1, width=5, bg=funcBg,fg=funcForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('%'))
btn_percent.grid(pady=1, padx=1, row=4, column=4)

btn_ln = tk.Button(numFrame, text='ln', height=1, width=5, bg=funcBg,fg=funcForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('ln'))
btn_ln.grid(pady=1, padx=1, row=4, column=5)

btn_log = tk.Button(numFrame, text='log', height=1, width=5, bg=funcBg,fg=funcForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('log'))
btn_log.grid(pady=1, padx=1, row=4, column=6)

btn_tobin = tk.Button(numFrame, text='bin', height=1, width=5, bg=funcBg,fg=funcForeground, font=(btnFontFamily, btnFontSize), command=lambda:to_bin())
btn_tobin.grid(pady=1, padx=1, row=4, column=7)

btn_par1 = tk.Button(numFrame, text='(', height=1, width=5, bg=funcBg,fg=funcForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress('('))
btn_par1.grid(pady=1, padx=1, row=1, column=4)

btn_par2 = tk.Button(numFrame, text=')', height=1, width=5, bg=funcBg,fg=funcForeground, font=(btnFontFamily, btnFontSize), command=lambda:btnPress(')'))
btn_par2.grid(pady=1.5, padx=1.5, row=1, column=5)

window.bind('<Key>', key_pressed)
window.bind('<Return>', enter_pressed)
window.bind('<BackSpace>', backspace_pressed)
window.bind('<Delete>', delete_pressed)


window.mainloop()
