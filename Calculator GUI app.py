import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced GUI Calculator")
        self.root.geometry("380x450")
        self.root.resizable(False, False)
        
        # String variable to track the current expression
        self.expression = ""
        
        # Display Screen Setup
        self.display_var = tk.StringVar()
        self.display_entry = tk.Entry(
            root, 
            textvariable=self.display_var, 
            font=("Arial", 20), 
            bd=10, 
            insertwidth=4, 
            width=14, 
            borderwidth=5, 
            justify="right"
        )
        self.display_entry.grid(row=0, column=0, columnspan=4, ipady=10, padx=10, pady=10)
        
        # Create the button layout grid
        self.create_buttons()

    def create_buttons(self):
        # Format: (Button Text, Row, Column)
        buttons = [
            ('C', 1, 0), ('**', 1, 1), ('//', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('%', 5, 2), ('=', 5, 3)
        ]
        
        for (text, row, col) in buttons:
            # Set action parameters depending on the type of key
            if text == '=':
                action = self.evaluate_expression
                bg_color = "#4CAF50"  # Green for Equals
                fg_color = "white"
            elif text == 'C':
                action = self.clear_display
                bg_color = "#f44336"  # Red for Clear
                fg_color = "white"
            else:
                action = lambda t=text: self.append_to_expression(t)
                bg_color = "#e7e7e7" if text.isdigit() or text == '.' else "#d2d2d2"
                fg_color = "black"

            btn = tk.Button(
                self.root, 
                text=text, 
                font=("Arial", 14, "bold"), 
                bg=bg_color, 
                fg=fg_color,
                padx=20, 
                pady=20, 
                borderwidth=1, 
                command=action
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            
        # Adjust grid sizing rules so buttons stretch evenly
        for i in range(4):
            self.root.columnconfigure(i, weight=1)
        for i in range(1, 6):
            self.root.rowconfigure(i, weight=1)

    def append_to_expression(self, operator_or_digit):
        self.expression += str(operator_or_digit)
        self.display_var.set(self.expression)

    def clear_display(self):
        self.expression = ""
        self.display_var.set("")

    def evaluate_expression(self):
        try:
            # Evaluates the expression string safely
            # Note: eval() can handle Python operators directly (+, -, *, /, %, **, //)
            result = str(eval(self.expression))
            self.display_var.set(result)
            self.expression = result  # Allow continuing calculations using result
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero is not allowed.")
            self.clear_display()
        except Exception:
            messagebox.showerror("Error", "Invalid expression.")
            self.clear_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
