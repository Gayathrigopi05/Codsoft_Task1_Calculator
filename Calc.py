import tkinter as tk
def button_click(symbol):
    current = display_var.get()
    if current == "Error":
        clear_display()
    if symbol == "C":
        clear_display()
    elif symbol == "=":
        try:
            result = eval(current)
            display_var.set(str(result))
        except Exception as e:
            display_var.set("Error")
    else:
        display_var.set(current + symbol)

def clear_display():
    display_var.set("")

root = tk.Tk()
root.title("Calculator")
root.configure(bg="#f0f0f0")

display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=("Arial", 18), bd=10, insertwidth=4, width=14, justify="right", bg="white")
display.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

for i in range(4):
    for j in range(4):
        btn = tk.Button(root, text=buttons[i][j], font=("Arial", 14), padx=20, pady=20,
                        command=lambda symbol=buttons[i][j]: button_click(symbol), bg="#4CAF50", fg="white", bd=0)
        btn.grid(row=i+1, column=j, padx=5, pady=5)

root.mainloop()
