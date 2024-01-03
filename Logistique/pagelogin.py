import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "1" and password == "1":
        hide_login_page()
    else:
        messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect")

def hide_login_page():
    # Cacher la page de connexion
    login_frame.place_forget()
    # Afficher la page de fond (plage)
    background_frame.place(relwidth=1, relheight=1)

    # Fermer la fenêtre après la connexion réussie
    root.destroy()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Application Logistique")

# Configuration de la taille et position de la fenêtre principale
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}+0+0")

# Création d'un cadre pour la page de fond (plage)
background_frame = tk.Frame(root, bg="white")
background_frame.place(relwidth=1, relheight=1)

# Création d'un cadre pour la page de connexion
login_frame = tk.Frame(root)
login_frame.place(relx=0.5, rely=0.5, anchor="center")

# Création des widgets pour la page de connexion
label_username = tk.Label(login_frame, text="Nom d'utilisateur:")
label_password = tk.Label(login_frame, text="Mot de passe:")
entry_username = tk.Entry(login_frame)
entry_password = tk.Entry(login_frame, show="*")
button_login = tk.Button(login_frame, text="Connexion", command=login)

# Placement des widgets à l'aide de la gestion de grille dans le cadre de connexion
label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
label_password.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
entry_username.grid(row=0, column=1, padx=10, pady=10)
entry_password.grid(row=1, column=1, padx=10, pady=10)
button_login.grid(row=2, column=1, pady=20)

# Lancement de la boucle principale
root.mainloop()
