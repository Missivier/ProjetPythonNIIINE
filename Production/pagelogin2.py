import tkinter as tk
from tkinter import messagebox



def page_login(root):

    def login():
        username = entry_username.get()
        password = entry_password.get()

        if username == "1" and password == "1":
            hide_login_page()
        else:
            messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect")

#enleve le login
    def hide_login_page():
        login_frame.place_forget()
        page_of(root)



    login_frame = tk.Frame(root)
    login_frame.place(relx=0.5, rely=0.5, anchor="center")

    label_username = tk.Label(login_frame, text="Nom d'utilisateur:")
    label_password = tk.Label(login_frame, text="Mot de passe:")
    entry_username = tk.Entry(login_frame)
    entry_password = tk.Entry(login_frame, show="*")
    button_login = tk.Button(login_frame, text="Connexion", command=login)

    label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
    label_password.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
    entry_username.grid(row=0, column=1, padx=10, pady=10)
    entry_password.grid(row=1, column=1, padx=10, pady=10)
    button_login.grid(row=2, column=1, pady=20)


def page_of(root):

    def deconnexion():
        title_frame.place_forget()
        border.place_forget()
        page_login(root)

    # Ajout d'une barre de titre en haut de la page
    border = tk.Frame(root, bg="black")
    border.place(relx=0, rely=0.11, relwidth=1, relheight=0.01)

    # Ajout d'une barre de titre en haut de la page
    title_frame = tk.Frame(root, bg="#DAD7D7")
    title_frame.place(relx=0.1, rely=0, relwidth=1, relheight=0.1)

    # Positionnement horizontal du label au centre
    title_label = tk.Label(title_frame, text="Liste des OF", font=("Arial", 16), bg="#DAD7D7")
    title_label.place(relx=0.4, rely=0.5, anchor="center")  # Centrer horizontalement

    # Ajout d'un bouton à droite du cadre
    button_right = tk.Button(title_frame, text="Déconnexion", command= deconnexion)
    button_right.place(relx=0.85, rely=0.5, anchor="center")  # Centrer horizontalement




