import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator Simplu")
        
        self.set_window_icon()

        # Crează și plasează widget-urile pentru calculator
        self.entry = tk.Entry(root, width=20, font=('Arial', 18))
        self.entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        # Butoane pentru cifre si operatii
        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
            ('C', 6, 0)  # Butonul pentru ștergere
        ]

        for (text, row, col) in buttons:
            tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                      command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, padx=5, pady=5)

    def set_window_icon(self):
        icon = Image.open('images/calculator_icon.png')
        icon = icon.resize((32, 32), Image.LANCZOS)
        self.icon_image = ImageTk.PhotoImage(icon)
        self.root.iconphoto(False, self.icon_image)

    def on_button_click(self, text):
        if text == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                tk.messagebox.showerror("Eroare", "Expresie invalidă!")
        elif text == 'C':
            self.entry.delete(0, tk.END)  # Șterge tot din caseta de text
        else:
            self.entry.insert(tk.END, text)

# Funcția main
def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()