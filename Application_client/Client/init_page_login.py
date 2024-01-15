import tkinter as tk
from tkinter import messagebox

class VotreApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Votre Application")
        self.geometry("800x600")

        self.page_login()

    def page_login(self):
        # Création de la frame pour la page login
        self.login_frame = tk.Frame(self)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        label_username = tk.Label(self.login_frame, text="Nom d'utilisateur:")
        label_password = tk.Label(self.login_frame, text="Mot de passe:")
        self.entry_username = tk.Entry(self.login_frame)
        self.entry_password = tk.Entry(self.login_frame, show="*")
        button_login = tk.Button(self.login_frame, text="Connexion", command=self.login)

        label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        label_password.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)
        button_login.grid(row=2, column=1, pady=20)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "1" and password == "1":
            self.hide_login_page()
            # Ajoutez la logique pour afficher la page produit et autres actions nécessaires
        elif username == "0" and password == "0":
            self.hide_login_page()
            # Ajoutez la logique pour afficher la page administrateur et autres actions nécessaires
        elif username == "2" and password == "2":
            self.hide_login_page()
            # Ajoutez la logique pour afficher la page logistique et autres actions nécessaires
        elif username == "3" and password == "3":
            self.hide_login_page()
            # Ajoutez la logique pour afficher la page commerce et autres actions nécessaires
        else:
            messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect")

    def show_page_login(self):
        self.entry_password.delete(0, tk.END)
        self.entry_username.delete(0, tk.END)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

    def hide_login_page(self):
        self.login_frame.place_forget()

    def hide_retour_login(self):
        # Ajoutez la logique pour cacher les autres pages et afficher la page de connexion
        pass

if __name__ == "__main__":
    app = VotreApplication()
    app.mainloop()
