import tkinter as tk
from tkinter import ttk
 
class ArticlePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Affichage des articles")
 
        # Création de la grille pour afficher les articles
        self.tree = ttk.Treeview(root, columns=("Code", "Nom", "Prix", "Image", "Stock"), show="headings")
 
        # Configuration des en-têtes de colonnes
        self.tree.heading("Code", text="Code")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Prix", text="Prix")
        self.tree.heading("Image", text="Image")
        self.tree.heading("Stock", text="Stock")
 
        # Ajout des colonnes avec une largeur augmentée de 50%
        self.tree.column("Code", width=int(100 * 1.5))
        self.tree.column("Nom", width=int(150 * 1.5))
        self.tree.column("Prix", width=int(100 * 1.5))
        self.tree.column("Image", width=int(150 * 1.5))
        self.tree.column("Stock", width=int(100 * 1.5))
 
        # Insertion des données (exemples)
        self.insert_data("123456", "Veste bouée", 249.90, "image1.jpg", 50)
        self.insert_data("123457", "Veste parachute", 544.90, "image2.jpg", 30)
        self.insert_data("123458", "Veste chauffante", 119.90, "image3.jpg", 40)
        self.insert_data("123459", "Veste réfrigérée", 129.90, "image4.jpg", 20)
 
        # Placement du Treeview
        self.tree.grid(row=0, column=0, padx=10, pady=10, columnspan=5)
 
        # Création du rectangle pour entrer le nombre d'articles
        self.entry_frame = tk.Frame(root)
        self.entry_label = tk.Label(self.entry_frame, text="Nombre d'articles à retirer:")
        self.entry_label.grid(row=0, column=0, padx=5, pady=5)
 
        self.num_articles_entry = tk.Entry(self.entry_frame)
        self.num_articles_entry.grid(row=0, column=1, padx=5, pady=5)
 
        # Création du bouton Valider
        self.validate_button = tk.Button(self.entry_frame, text="Valider", command=self.validate)
        self.validate_button.grid(row=0, column=2, padx=5, pady=5, sticky="e")
 
        self.entry_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")
 
    def insert_data(self, code, name, price, image, stock):
        # Insertion des données dans le Treeview
        self.tree.insert("", tk.END, values=(code, name, price, image, stock))
 
    def validate(self):
        # Ajoutez ici le code pour traiter la validation du nombre d'articles
        # par exemple, récupérez la valeur de self.num_articles_entry.get()
        pass
 
# Création de la fenêtre principale
root = tk.Tk()
 
# Récupération de la résolution de l'écran
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
 
# Ajustement de la taille de la fenêtre principale de 50%
window_width = int(screen_width * 1.5)
window_height = int(screen_height * 1.5)
root.geometry(f"{window_width}x{window_height}")
 
# Instanciation de la classe ArticlePage
app = ArticlePage(root)
 
# Lancement de la boucle principale
root.mainloop()