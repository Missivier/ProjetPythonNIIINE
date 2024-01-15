import sys
sys.path.insert(0,'odoo')
from intregration import ERP

from tkinter import Tk, Label, Entry, Button, Frame
from tkinter import messagebox
from view import HomeView
from Production import ProductionPage

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

        self.login_page()
#-----------------------------------------------------------------------------------------------------------------------------------
    #Création de la page login
        '''
    def login_page(self):
        self.username_label = Label(self, text="Nom d'utilisateur:")
        self.username_entry = Entry(self)

        self.password_label = Label(self, text="Mot de passe:")
        self.password_entry = Entry(self, show="*")

        self.login_button = Button(self, text="Connexion", command = self.login())

        self.username_label.pack(pady=10)
        self.username_entry.pack(pady=5)
        self.password_label.pack(pady=10)
        self.password_entry.pack(pady=5)
        self.login_button.pack(pady=20)
        '''
    def login_page(self):
     # Création de la frame pour la page login
        self.login_frame = Frame(self)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        label_username = Label(self.login_frame, text="Nom d'utilisateur:")
        label_password = Label(self.login_frame, text="Mot de passe:")

        self.entry_username = Entry(self.login_frame)
        self.entry_password = Entry(self.login_frame, show="*")
        button_login = Button(self.login_frame, text="Connexion", command=self.login)

        label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        label_password.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

        self.entry_username.grid(row=0, column=1, padx=10, pady=10)
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)
        button_login.grid(row=2, column=1, pady=20)
#-----------------------------------------------------------------------------------------------------------------------------------
    # Fonction pour la connection
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Vérification du login, exemple simplifié
        if username == 'admin' and password == 'adminpass':
            self.show_page(HomeView)
        elif username == '1' and password == '1':
            self.show_page(HomeView)
        else:
            self.show_error("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect")

    def show_page(self, page_class):
        # Supprime les widgets de la page de connexion
        self.login_frame.destroy()

        # Supprime le bouton Quitter
        #self.bouton_quit.destroy()

        # Crée une instance de la nouvelle classe
        page_instance = page_class(self)

        # Affiche la nouvelle page
        page_instance.pack(fill="both", expand=True)

    def show_error(self, title, message):
        messagebox.showerror(title, message)
#-----------------------------------------------------------------------------------------------------------------------------------
#Lancement du main
if __name__ == "__main__":
    app = Application()
    app.mainloop()
