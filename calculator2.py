import tkinter as tk

def press(num):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))

def equalpress():
    try:
        total = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, total)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Erro")

def clear():
    entry.delete(0, tk.END)

window = tk.Tk()
window.geometry('300x300')
window.title('Calculadora')
entry = tk.Entry(window)
entry.grid(row=0, column=0, columnspan=4)
for i in range(9):
    tk.Button(window, text=str(i+1), command=lambda i=i: press(i+1)).grid(row=(i//3)+1, column=i%3)
    
tk.Button(window, text='0', command=lambda: press(0)).grid(row=4, column=1)
tk.Button(window, text='+', command=lambda: press('+')).grid(row=1, column=3)
tk.Button(window, text='-', command=lambda: press('-')).grid(row=2, column=3)
tk.Button(window, text='*', command=lambda: press('*')).grid(row=3, column=3)
tk.Button(window, text='/', command=lambda: press('/')).grid(row=4, column=3)
tk.Button(window, text='=', command=equalpress).grid(row=4, column=2)
tk.Button(window, text='C', command=clear).grid(row=4, column=0)

window.mainloop()
