import tkinter as tk

def click_button(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

root = tk.Tk()
root.title("Máy Tính")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    ('phan dinh phap', 4),  # Change to a tuple with the button text and columnspan
    '1', '2', '3', '-',
    'C', '0', '=', '+',
    '.'
]

row_val = 1
col_val = 0

my_name = isinstance

for button in buttons:
    if my_name(button, tuple):
        tk.Button(root, text=button[0], padx=70, pady=20, command=lambda: entry.delete(0, tk.END)).grid(row=row_val, column=col_val, columnspan=button[1])
    elif button == '=':
        tk.Button(root, text=button, padx=20, pady=20, command=calculate).grid(row=row_val, column=col_val)
    elif button == 'C':
        tk.Button(root, text=button, padx=20, pady=20, command=lambda: entry.delete(0, tk.END)).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, command=lambda b=button: click_button(b)).grid(row=row_val, column=col_val)

    col_val += button[1] if my_name(button, tuple) else 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
