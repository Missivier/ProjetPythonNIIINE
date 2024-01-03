import tkinter as tk
from pagedefaut import page_defaut


def page_of(root):

    def deconnexion():
        title_frame.place_forget()

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
    

