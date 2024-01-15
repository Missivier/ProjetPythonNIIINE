import sys
sys.path.insert(0,'odoo')
from intregration import ERP

from tkinter import Tk, Label, Entry, Button, Frame, messagebox
from view import HomeView

class Application(Tk):
    def __init__(self):
        super().__init__()


        self.title("Application CyberVest")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"{self.screen_width}x{self.screen_height}+0+0")

        self.background_frame = Frame(self, bg="#DAD7D7")
        self.background_frame.place(relwidth=1, relheight=1)

        # Création d'un bouton pour quitter l'application
        self.bouton_quit = Button(self, text="Quitter", fg="#296EDF", bg="#DAD7D7", font=("Arial", 20), command=self.destroy)
        self.bouton_quit.pack(side="bottom", anchor="se", pady=10, padx=10)  # Positionne le bouton en bas à droite

         # Instance classe ERP
        self.erp = ERP("db_cybervest", self.username_entry.get(), self.password_entry.get())

        self.login_page()

    def login_page(self):
        self.username_label = Label(self, text="Nom d'utilisateur:")
        self.entry_username = Entry(self)

        self.password_label = Label(self, text="Mot de passe:")
        self.entry_password = Entry(self, show="*")

        self.login_button = Button(self, text="Connexion", command = self.login())

        self.username_label.pack(pady=10)
        self.entry_username.pack(pady=5)
        self.password_label.pack(pady=10)
        self.entry_password.pack(pady=5)
        self.login_button.pack(pady=20)

    def login(self):
        self.erp.connexion()

    def show_page(self, page_class):
        # Supprime les widgets de la page de connexion
        self.username_label.destroy()
        self.username_entry.destroy()
        self.password_label.destroy()
        self.password_entry.destroy()
        self.login_button.destroy()

        # Supprime le bouton Quitter
        self.bouton_quit.destroy()

        # Crée une instance de la nouvelle classe
        page_instance = page_class(self)

        # Affiche la nouvelle page
        page_instance.pack(fill="both", expand=True)

    def show_error(self, title, message):
        messagebox.showerror(title, message)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
