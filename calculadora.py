import tkinter as tk

def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def on_clear():
    entry.delete(0, tk.END)

def on_equals():
    try:
        current = entry.get()
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Cria a janela principal
root = tk.Tk()
root.title("Calculadora")

# Cria uma entrada para a calculadora
entry = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=2, relief='solid')
entry.grid(row=0, column=0, columnspan=4)

# Cria botões com os números e operadores
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for text, row, col in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=col)

# Botão para limpar a entrada
clear_button = tk.Button(root, text='C', width=5, height=2, font=('Arial', 18), command=on_clear)
clear_button.grid(row=5, column=0, columnspan=2)

# Botão para calcular a expressão
equals_button = tk.Button(root, text='=', width=5, height=2, font=('Arial', 18), command=on_equals)
equals_button.grid(row=5, column=2, columnspan=2)

# Executa o loop principal
root.mainloop()