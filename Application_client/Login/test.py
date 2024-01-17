import tkinter as tk
from PIL import Image, ImageTk

def redimensionner_image(event):
    # Redimensionner l'image en fonction de la taille de la fenêtre
    nouvelle_largeur = event.width
    nouvelle_hauteur = event.height
    image_redimensionnee = image_pil.resize((nouvelle_largeur, nouvelle_hauteur), Image.ANTIALIAS)
    nouvelle_image_tk = ImageTk.PhotoImage(image_redimensionnee)
    canvas.config(width=nouvelle_largeur, height=nouvelle_hauteur)
    canvas.create_image(0, 0, anchor=tk.NW, image=nouvelle_image_tk)
    canvas.image = nouvelle_image_tk  # Garde une référence à l'image pour éviter la suppression par le ramasse-miettes

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Fenêtre avec image redimensionnable")

# Chargement de l'image avec Pillow
chemin_image_jpg = "/home/user/Documents/ProjetPythonNIIINE/Application_client/Login/v915-wit-011.png"
image_pil = Image.open(chemin_image_jpg)
image_tk = ImageTk.PhotoImage(image_pil)

# Création d'un widget Canvas pour afficher l'image
canvas = tk.Canvas(fenetre, width=image_tk.width(), height=image_tk.height())
canvas.pack(expand=tk.YES, fill=tk.BOTH)

# Affichage de l'image en fond d'écran
canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)

# Associer la fonction de redimensionnement à l'événement de redimensionnement de la fenêtre
fenetre.bind("<Configure>", redimensionner_image)

# Exécution de la boucle principale
fenetre.mainloop()
