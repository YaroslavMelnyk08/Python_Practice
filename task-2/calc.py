import tkinter as tk
import math

def add_digit(digit):
    value = calc.get()+ str(digit)
    calc.delete(0, tk.END)
    calc.insert(0, value)

def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*%':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value+operation)

def calculate():
    value = calc.get()
    if value[-1] in '+-*/%':
        value = value+value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, eval(value))

def clear ():
    calc.delete(0, tk.END)
    calc.insert(0,' ')

def Cosinus():
    value=calc.get()
    x=float(value)
    value=math.cos(x)
    calc.delete(0,tk.END)
    calc.insert(0,value)

def Sinus():
    value=calc.get()
    x=float(value)
    value=math.sin(x)
    calc.delete(0,tk.END)
    calc.insert(0,value)

def tan():
    value=calc.get()
    x=float(value)
    value=math.tan(x)
    calc.delete(0,tk.END)
    calc.insert(0,value)

def ctg():
    value=calc.get()
    x=float(value)
    value=math.cos(x)/math.sin(x)
    calc.delete(0,tk.END)
    calc.insert(0,value)

def log():
    value=calc.get()
    x=float(value)
    value=math.log2(x)
    calc.delete(0,tk.END)
    calc.insert(0,value)

def ln():
    value=calc.get()
    x=float(value)
    value=math.log10(x)
    calc.delete(0,tk.END)
    calc.insert(0,value)

def DK():
    value = calc.get()
    n = ''
    x=int(value)
    while x > 0 :
            y = str(x % 2)
            n = y + n
            x = int(x / 2)    
    calc.delete(0,tk.END)
    calc.insert(0,n)
   
def operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial, 13'), fg='red',
                     command=lambda: add_operation(operation))

def calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial, 13'), fg='red',
                    command=calculate)

def clear_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial, 13'), fg='red',
                    command=clear)

def cos_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial,13'), fg='red',
                     command=Cosinus)

def sin_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial,13'), fg='red',
                     command=Sinus)

def tan_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial,13'), fg='red',
                     command=tan)

def ctg_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial,13'), fg='red',
                     command=ctg)

def log_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial,13'), fg='red',
                     command=log)

def ln_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial,13'), fg='red',
                     command=ln)

def dkod_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial,13'), fg='#008000',
                     command=DK)

win = tk.Tk()
win.geometry(f"365x280+100+200")
win['bg']= '#D3D3D3'
win.title('Калькулятор')

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.grid(row=0, column=0, columnspan=6, stick='we', padx=5, pady=5)

tk.Button(text='1', bd=5, font=('Arial', 13),command=lambda : add_digit(1)).grid(row=1, column=0, stick='wens', padx=5, pady=5)
tk.Button(text='2', bd=5, font=('Arial', 13),command=lambda : add_digit(2)).grid(row=1, column=1, stick='wens', padx=5, pady=5)
tk.Button(text='3', bd=5, font=('Arial', 13),command=lambda : add_digit(3)).grid(row=1, column=2, stick='wens', padx=5, pady=5)
tk.Button(text='4', bd=5, font=('Arial', 13),command=lambda : add_digit(4)).grid(row=2, column=0, stick='wens', padx=5, pady=5)
tk.Button(text='5', bd=5, font=('Arial', 13),command=lambda : add_digit(5)).grid(row=2, column=1, stick='wens', padx=5, pady=5)
tk.Button(text='6', bd=5, font=('Arial', 13),command=lambda : add_digit(6)).grid(row=2, column=2, stick='wens', padx=5, pady=5)
tk.Button(text='7', bd=5, font=('Arial', 13),command=lambda : add_digit(7)).grid(row=3, column=0, stick='wens', padx=5, pady=5)
tk.Button(text='8', bd=5, font=('Arial', 13),command=lambda : add_digit(8)).grid(row=3, column=1, stick='wens', padx=5, pady=5)
tk.Button(text='9', bd=5, font=('Arial', 13),command=lambda : add_digit(9)).grid(row=3, column=2, stick='wens', padx=5, pady=5)
tk.Button(text='0', bd=5, font=('Arial', 13),command=lambda : add_digit(0)).grid(row=4, column=0, stick='wens', padx=5, pady=5)

operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
operation_button('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
operation_button('*').grid(row=4, column=3, stick='wens', padx=5, pady=5)
operation_button('%').grid(row=3, column=5, stick='wens', padx=5, pady=5)

cos_button('cos').grid(row=1, column=4, stick='wens', padx=5, pady=5)
sin_button('sin').grid(row=2, column=4, stick='wens', padx=5, pady=5)
tan_button('tan').grid(row=3, column=4, stick='wens', padx=5, pady=5)
ctg_button('ctg').grid(row=4, column=4, stick='wens', padx=5, pady=5)
log_button('log').grid(row=1, column=5, stick='wens', padx=5, pady=5)
ln_button('ln').grid(row=2, column=5, stick='wens', padx=5, pady=5)
dkod_button('DK').grid(row=4, column=5, stick='wens', padx=5, pady=5)


calc_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
clear_button('C').grid(row=4, column=1, stick='wens', padx=5, pady=5)


win.grid_columnconfigure(0,minsize=60)
win.grid_columnconfigure(1,minsize=60)
win.grid_columnconfigure(2,minsize=60)
win.grid_columnconfigure(3,minsize=60)

win.grid_rowconfigure(1,minsize=60)
win.grid_rowconfigure(2,minsize=60)
win.grid_rowconfigure(3,minsize=60)
win.grid_rowconfigure(4,minsize=60)
