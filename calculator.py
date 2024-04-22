import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        valor1 = float(entry_valor1.get())
        valor2 = float(entry_valor2.get())
        operacao = combo_operacao.get()

        if operacao == "Sum":
            resultado = valor1 + valor2
            aux = "+"
        elif operacao == "Subtract":
            resultado = valor1 - valor2
            aux = "-"
        elif operacao == "Multiply":
            resultado = valor1 * valor2
            aux = "x"
        elif operacao == "Divide":
            resultado = valor1 / valor2
            aux = "/"

        label_resultado.config(text=f"{valor1} {aux} {valor2} = {resultado}")
    except ValueError:
        label_resultado.config(text="Insert valid numbers.")

janela = tk.Tk()
janela.title("Calculator")
janela.geometry("300x220")

label_valor1 = tk.Label(janela, text="First Value:")
entry_valor1 = tk.Entry(janela)
label_valor2 = tk.Label(janela, text="Second Value:")
entry_valor2 = tk.Entry(janela)

label_operacao = tk.Label(janela, text="Chose an Operation:")
operacoes = ["Sum", "Subtract", "Multiply", "Divide"]
combo_operacao = tk.StringVar()
combo_operacao.set(operacoes[0])  # Valor padrão
menu_operacao = tk.OptionMenu(janela, combo_operacao, *operacoes)

botao_calcular = tk.Button(janela, text="Calculate", command=calcular)

label_resultado = tk.Label(janela, text="")

label_resultText = tk.Label(janela, text="Result:")

label_valor1.pack()
entry_valor1.pack()
label_valor2.pack()
entry_valor2.pack()
label_resultText.pack()
label_resultado.pack()
label_operacao.pack()
menu_operacao.pack()
botao_calcular.pack()

# Iniciando a exibição da janela
janela.mainloop()
