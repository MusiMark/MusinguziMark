import tkinter as tk
from tkinter import messagebox

#Valuables
first = 0
second = 0
operator = ""
result = 0

# My Functions
def add_numbers(first_value, second_value):
    return first_value + second_value

def subtract_numbers(first_value, second_value):
    return first_value - second_value

def multiply_numbers(first_value, second_value):
    return first_value * second_value

def divide_numbers(first_value, second_value):
    return first_value / second_value

def calculate(operator_value):
    if operator_value == "+":
        result = add_numbers(first, second)
    elif operator_value == "-":
        result = subtract_numbers(first, second)
    elif operator_value == "*":
        result = multiply_numbers(first, second)
    elif operator_value == "/":
        result = divide_numbers(first, second)
    else:
        messagebox.showerror("Error", "Invalid operator")
        result = 0

    return result

# GUI Functions
def button_click(value):
    display.insert(tk.END, value)


def set_operator(op):
    global first, operator

    try:
        first = float(display.get())
        operator = op
        display.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Enter a number first.")


def show_result():
    global second

    try:
        second = float(display.get())

        answer = calculate(operator)

        display.delete(0, tk.END)
        display.insert(0, str(answer))

    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")
        clear_display()

    except ValueError:
        messagebox.showerror("Error", "Invalid input.")


def clear_display():
    global first, second, operator

    first = 0
    second = 0
    operator = ""

    display.delete(0, tk.END)


# Window
window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)

# Display
display = tk.Entry(window, width=18, font=("Arial", 20), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons Layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create Buttons
for text, row, col in buttons:
    if text.isdigit():
        command = lambda t=text: button_click(t)

    elif text in ['+', '-', '*', '/']:
        command = lambda t=text: set_operator(t)

    elif text == '=':
        command = show_result

    else:  # C
        command = clear_display

    tk.Button(
        window,
        text=text,
        width=5,
        height=2,
        font=("Arial", 18),
        command=command
    ).grid(row=row, column=col, padx=5, pady=5)

window.mainloop()