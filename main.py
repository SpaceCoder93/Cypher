import tkinter as tk
import tkinter.ttk as ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Cypher - Password Manager')
        self.state('zoomed')
        LoginScreen(self)
        self.mainloop()

class LoginScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets(self)
        self.pack()

    def create_widgets(self, parent):
        email_lbl = tk.Label(parent, text="Email:", font=('Montserrat', 32), width=16)
        email_lbl.pack()
        email_ent = tk.Entry(parent, font=('Montserrat', 32), width=16)
        email_ent.pack()
        pass_lbl = tk.Label(parent, text="Password: ", font=('Montserrat', 32), width=16)
        pass_lbl.pack()
        pass_ent = tk.Entry(parent, font=('Montserrat', 32), width=16, show="*")
        pass_ent.pack()
        login_btn = tk.Button(parent, text="Login", font=('Montserrat', 32), width=16)
        login_btn.pack()
        create_btn = tk.Button(parent, text="New here? Sign up here.", font=('Montserrat', 32), width=16)
        create_btn.pack()


if __name__ == "__main__":
    App()
