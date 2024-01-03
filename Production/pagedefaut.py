import tkinter as tk

def page_defaut():
    # Création de la fenêtre principale
    root = tk.Tk()
    root.title("Application Production")

    # Configuration de la taille et position de la fenêtre principale
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(f"{screen_width}x{screen_height}+0+0")

    # Création d'un cadre pour la page de fond (plage)
    background_frame = tk.Frame(root, bg="#DAD7D7")
    background_frame.place(relwidth=1, relheight=1)

    # Ajout du libellé "Production" en haut à gauche
    label_production = tk.Label(root, text="Production", fg="#296EDF", bg="#DAD7D7", font=("Arial", 20))
    label_production.place(x=10, y=10)  # Position du libellé en coordonnées x, y

    # Lancement de la boucle principale
    root.mainloop()

# Appel de la fonction pour afficher la page par défaut
#page_defaut()
