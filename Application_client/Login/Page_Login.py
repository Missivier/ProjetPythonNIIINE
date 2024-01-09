import tkinter as tk
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