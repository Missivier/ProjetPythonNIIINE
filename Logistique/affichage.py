import tkinter as tk
from tkinter import ttk

class ArticlePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Affichage des articles")
 
        # Création de la grille pour afficher les articles
        self.tree = ttk.Treeview(root, columns=("Code", "Nom", "Prix", "Stock"), show="headings")
 
        # Configuration des en-têtes de colonnes
        self.tree.heading("Code", text="Code")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Prix", text="Prix")
        self.tree.heading("Stock", text="Stock")
 
        # Ajout des colonnes avec une largeur augmentée de 50%
        self.tree.column("Code", width=int(100 * 1.5))
        self.tree.column("Nom", width=int(150 * 1.5))
        self.tree.column("Prix", width=int(100 * 1.5))
        self.tree.column("Stock", width=int(100 * 1.5))
 
        # Insertion des données (exemples)
        self.insert_data("123456", "Veste bouée", 249.90, "50", "veste bouée.jpg")
        self.insert_data("123457", "Veste parachute", 544.90, "50", "veste parachute.jpg")
        self.insert_data("123458", "Veste chauffante", 119.90, "50", "veste chauffante.jpg")
        self.insert_data("123459", "Veste réfrigérée", 129.90, "50", "veste réfrigérée.jpg")
 
        # Binding de l'événement de clic
        self.tree.bind("<ButtonRelease-1>", self.show_image)
 
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
 
        # Dictionnaire associant chaque article à son image correspondante
        self.image_dict = {
            "Veste bouée": "veste bouée.jpg",
            "Veste parachute": "veste parachute.jpg",
            "Veste chauffante": "veste chauffante.jpg",
            "Veste réfrigérée": "veste réfrigérée.jpg",
        }

    def insert_data(self, code, name, price, stock, image):
        # Insertion des données dans le Treeview
        self.tree.insert("", tk.END, values=(code, name, price, stock, image))
 
    def show_image(self, event):
        # Récupération de la ligne sélectionnée
        item = self.tree.selection()[0]
 
        # Récupération du nom de l'article associé à la ligne sélectionnée
        article_name = self.tree.item(item, "values")[1]
 
        # Récupération du nom de l'image associée à l'article
        image_name = self.image_dict.get(article_name, "")
 
        if image_name:
            # Affichage de l'image dans un Label à l'intérieur de la même fenêtre
            image_path = {image_name}
            img = tk.PhotoImage(file=image_path)
 
            # Supprimer l'ancien Label s'il existe
            for widget in self.root.grid_slaves():
                if isinstance(widget, tk.Label):
                    widget.destroy()
 
            # Création d'un widget Label pour afficher l'image à droite
            image_label = tk.Label(self.root, image=img)
            image_label.photo = img
            image_label.grid(row=0, column=1, padx=10, pady=10, rowspan=2, sticky="e")  # Ajustez la position et la colonne selon vos besoins

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
