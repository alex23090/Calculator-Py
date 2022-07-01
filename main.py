def clear():
    name['state'] = tk.NORMAL
    name.delete(0, tk.END)
    name.insert(0, '0')
    name['state'] = tk.DISABLED

def calculate():
    value = name.get()
    if value[-1] in '*-+/':
        value = value + value[:-1]
    name['state'] = tk.NORMAL
    name.delete(0, tk.END)
    try:
        name.insert(0, eval(value))
    except(NameError, SyntaxError):
        messagebox.showinfo('Внимание','Необходимо вводить только цифры и математические знаки')
        name.insert(0, '0')
    except(ZeroDivisionError):
        messagebox.showinfo('Внимание','Деление на ноль невозможно')
        name.insert(0, '0')
    name['state'] = tk.DISABLED

def add_digit(digit):
    value = name.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    name['state'] = tk.NORMAL
    name.delete(0, tk.END)
    name.insert(0, value+digit)
    name['state'] = tk.DISABLED

def add_operation(operation):
    value = name.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = name.get()
    value += operation
    name['state'] = tk.NORMAL
    name.delete(0, tk.END)
    name.insert(0, value)
    name['state'] = tk.DISABLED

def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '-+/*':
        add_operation(event.char)
    elif event.char == '=' or event.char == '\r':
        calculate()
    elif event.char == '\b' and name.get() != "":
        value = name.get()
        name['state'] = tk.NORMAL
        name.delete(0, tk.END)
        name.insert(0, value[:-1])
        if len(name.get()) < 1:
            clear()
        name['state'] = tk.DISABLED

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

win = tk.Tk()
photo = tk.PhotoImage(file='calc.png')
win.iconphoto(False, photo)
win.config(bg = "white")
win.title("Calculator")
win.geometry("340x370")
win.resizable(True, True)
win.bind('<Key>', press_key)

name = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
name.insert(0, '0')
name['state'] = tk.DISABLED
name.grid(row=0, column=0, columnspan=4, stick='we', padx=5, pady=2)

tk.Button(win, text = '4', font=('Product Sans', 13), bg="#ebebeb", command=lambda : add_digit('4')).grid(row=2, column=0, stick='wens', pady=5, padx=5)
tk.Button(win, text = '5', font=('Product Sans', 13), bg="#ebebeb", command=lambda : add_digit('5')).grid(row=2, column=1, stick='wens', pady=5, padx=5)
tk.Button(win, text = '6', font=('Product Sans', 13), bg="#ebebeb", command=lambda : add_digit('6')).grid(row=2, column=2, stick='wens', pady=5, padx=5)
tk.Button(win, text = '1', font=('Product Sans', 13), bg="#ebebeb", command=lambda : add_digit('1')).grid(row=3, column=0, stick='wens', pady=5, padx=5)
tk.Button(win, text = '2', font=('Product Sans', 13), bg="#ebebeb", command=lambda : add_digit('2')).grid(row=3, column=1, stick='wens', pady=5, padx=5)
tk.Button(win, text = '3', font=('Product Sans', 13), bg="#ebebeb", command=lambda : add_digit('3')).grid(row=3, column=2, stick='wens', pady=5, padx=5)
tk.Button(win, text = '7', font=('Product Sans', 13), bg="#ebebeb", command=lambda : add_digit('7')).grid(row=1, column=0, stick='wens', pady=5, padx=5)
tk.Button(win, text = '8', font=('Product Sans', 13), bg="#ebebeb", command=lambda : add_digit('8')).grid(row=1, column=1, stick='wens', pady=5, padx=5)
tk.Button(win, text = '9', font=('Product Sans', 13), bg="#ebebeb", command=lambda : add_digit('9')).grid(row=1, column=2, stick='wens', pady=5, padx=5)
tk.Button(win, text = '0', font=('Product Sans', 13), bg="#ebebeb", command=lambda : add_digit('0')).grid(row=4, column=0, stick='wens', pady=5, padx=5)

tk.Button(win, text = '/', font=('Product Sans', 13), bg="#cfcfcf", command=lambda : add_operation('/')).grid(row=4, column=1, stick='wens', pady=5, padx=5)
tk.Button(win, text = 'x', font=('Product Sans', 13), bg="#cfcfcf", command=lambda : add_operation('*')).grid(row=4, column=2, stick='wens', pady=5, padx=5)
tk.Button(win, text = '-', font=('Product Sans', 13), bg="#cfcfcf", command=lambda : add_operation('-')).grid(row=3, column=3, stick='wens', pady=5, padx=5)
tk.Button(win, text = 'C', font=('Product Sans', 13), bg="#cfcfcf", command=lambda : clear()).grid(row=1, column=3, stick='wens', pady=5, padx=5)
tk.Button(win, text = '+', font=('Product Sans', 13), bg="#cfcfcf", command=lambda : add_operation('+')).grid(row=2, column=3, stick='wens', pady=5, padx=5)
tk.Button(win, text = '=', font=('Product Sans', 14), bg="#297eff", foreground="white", command=lambda : calculate()).grid(row=4, column=3, stick='wens', pady=5, padx=5)

win.grid_columnconfigure(0, minsize=85)
win.grid_columnconfigure(1, minsize=85)
win.grid_columnconfigure(2, minsize=85)
win.grid_columnconfigure(3, minsize=85)

win.grid_rowconfigure(1, minsize=85)
win.grid_rowconfigure(2, minsize=85)
win.grid_rowconfigure(3, minsize=85)
win.grid_rowconfigure(4, minsize=85)

win.mainloop()