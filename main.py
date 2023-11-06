import threading
import time
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font
from PIL import Image, ImageTk

PRIMARY_COLOR = "#272932" #60%
SECONDARY_COLOR = "#F8F7F9" #30%
ACCENT_COLOR = "#5DA9E9" #10%
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Cypher - Password Manager')
        self.state('zoomed')
        #LoginScreen(self)
        MainPage(self)
        self.mainloop()

class LoginScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.image1 = Image.open("assets/loginpage_image.png")
        self.image1 = self.image1.resize((925, 925), Image.BILINEAR)
        self.image1 = ImageTk.PhotoImage(self.image1)
        self.create_widgets(self, parent)
        self.place(x=0, y=0, relheight=1, relwidth=1)

    def create_widgets(self, parent, root):
        frame_carousal = tk.Label(parent, bg=ACCENT_COLOR, image=parent.image1)
        frame_carousal.place(relx=0, rely=0, relwidth=0.6, relheight=1)
        widget_carousal = tk.Frame(parent, bg=PRIMARY_COLOR)
        widget_carousal.place(relx=0.6, rely=0, relwidth=0.4, relheight=1)
        title_lbl = tk.Label(parent, text="CYPHER", font=("Montserrat", 36), width=16, bg=PRIMARY_COLOR, fg=SECONDARY_COLOR)
        title_lbl.place(relx=0.66, rely=0.25)
        email_ent = tk.Entry(parent, font=("Montserrat", 28), width=19, bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, bd=10)
        email_ent.place(relx=0.675, rely=0.35)
        pass_ent = tk.Entry(parent, font=("Montserrat", 28), width=19, show="*", bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, bd=10)
        pass_ent.place(relx=0.675, rely=0.45)
        login_btn = tk.Button(parent, text="Login", font=("Montserrat", 28), width=10, bg=ACCENT_COLOR, fg=SECONDARY_COLOR, bd=10, command=lambda: self.auth(str(email_ent.get()), str(pass_ent.get()), parent, root))
        login_btn.place(relx=0.735, rely=0.55, relheight=0.09)
        create_btn = tk.Button(parent, text="New here? Sign up here.", font=("Montserrat", 16), bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, bd=10)
        create_btn.place(relx=0.7275, rely=0.65)
        self.error_lbl = tk.Label(parent, text="", fg=PRIMARY_COLOR, bg=PRIMARY_COLOR, bd=0, font=("Montserrat", 28))
        self.error_lbl.place(relx=0.68, rely=0.75, relwidth=0.25)

    def auth(self, username, passw, parent, root):
        if username == "viraj" and passw == "1234":
            parent.forget()
            MainPage(root)
        else:
            parent.error_lbl.config(text="Invalid Credentials", fg="red")

class MainPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.image1 = Image.open("assets/loginpage_image.png")
        self.image1 = self.image1.resize((5, 5), Image.BILINEAR)
        self.image1 = ImageTk.PhotoImage(self.image1)
        self.create_widget(self)
        self.place(x=0, y=0, relheight=1, relwidth=1)

    def printer(self, x):
        print(x)

    def create_widget(self, parent):
        title_lbl = tk.Label(parent, text="CYPHER", font=("Montserrat", 36), width=16, bg=PRIMARY_COLOR, fg=ACCENT_COLOR, highlightbackground=ACCENT_COLOR, borderwidth=5, highlightcolor=ACCENT_COLOR, highlightthickness=2)
        title_lbl.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        category_frame = tk.Frame(parent, bg=PRIMARY_COLOR, bd=0, highlightbackground=ACCENT_COLOR, borderwidth=5, highlightcolor=ACCENT_COLOR, highlightthickness=2)
        category_frame.place(relx=0, rely=0.1, relwidth=0.2, relheight=0.9)
        list_frame = tk.Frame(parent, bg=PRIMARY_COLOR, bd=0, highlightbackground=ACCENT_COLOR, borderwidth=5, highlightcolor=ACCENT_COLOR, highlightthickness=2)
        list_frame.place(relx=0.2, rely=0.1, relwidth=0.25, relheight=0.9)
        content_frame = tk.Frame(parent, bg=PRIMARY_COLOR, bd=10,highlightbackground=ACCENT_COLOR, borderwidth=5, highlightcolor=ACCENT_COLOR, highlightthickness=2)
        content_frame.place(relx=0.45, rely=0.1, relwidth=0.55, relheight=0.9)
        password_btn = tk.Button(category_frame, text="PASSWORDS", width=10, bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, bd=10, font=("Montserrat", 25), relief='groove')
        password_btn.pack(fill="x", pady=5)
        card_btn = tk.Button(category_frame, text="CARDS", width=10, bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, bd=10, font=("Montserrat", 25), relief='groove')
        card_btn.pack(fill="x", pady=5)
        id_btn = tk.Button(category_frame, text="IDENTITY CARD", width=10, bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, bd=10, font=("Montserrat", 25), relief='groove')
        id_btn.pack(fill="x", pady=5)
        note_btn = tk.Button(category_frame, text="SECURE NOTE", width=10, bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, bd=10, font=("Montserrat", 25), relief='groove')
        note_btn.pack(fill="x", pady=5)
        cloud_btn = tk.Button(parent, text="Cloud Sync", width=10, bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, bd=2, font=("Montserrat", 10), relief='groove')
        cloud_btn.place(relx=0.815, rely=0.01)
        local_btn = tk.Button(parent, text="Local Save", width=10, bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, bd=2, font=("Montserrat", 10), relief='groove')
        local_btn.place(relx=0.875, rely=0.01)
        logout_btn = tk.Button(parent, text="  Logout  ", width=10, bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, bd=2, font=("Montserrat", 10), relief='groove')
        logout_btn.place(relx=0.935, rely=0.01)
        style = ttk.Style(parent)
        style.theme_use("alt")
        style.configure('Treeview', background=PRIMARY_COLOR, foreground=SECONDARY_COLOR, font=("Montserrat", 15), anchor="center", fieldbackground=PRIMARY_COLOR, bd=0)
        style.map('Treeview', background=[('selected', ACCENT_COLOR)], foreground=[('selected', PRIMARY_COLOR)])
        style.configure('Treeview.Column', stretch=tk.YES)
        style.configure('Treeview', rowheight=35)
        list_treeview = ttk.Treeview(list_frame, columns=('item',), show='tree')
        list_treeview.column('#0', width=200)
        verscrlbar = ttk.Scrollbar(list_frame, orient="vertical", command=list_treeview.yview)
        verscrlbar.place(relx=0.95, rely=0, relheight=0.95)
        list_treeview.configure(yscrollcommand=verscrlbar.set)
        list_treeview.place(x=0, y=0, relwidth=0.95, relheight=0.95)
        add_to_btn = tk.Button(list_frame, text="ADD A NEW ENTRY", width=10, bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, bd=2, font=("Montserrat", 15), relief='groove')
        add_to_btn.place(relx=0, rely=0.95, relwidth=1)
        self.create_btn(list_treeview)

    def create_btn(self, widget):
        a = ["Apple", "Google", "Linkedin", "Microsoft"]
        for i in a:
            widget.insert(parent='', index='end', text=i)


if __name__ == "__main__":
    App()
