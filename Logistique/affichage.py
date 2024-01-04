import tkinter as tk
from tkinter import ttk

class ArticlePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Affichage des articles")

        # Création de la grille pour afficher les articles
        self.tree = ttk.Treeview(root, columns=("Code", "Nom", "Prix", "Stock"), show="headings")

        # Configuration des en-têtes de colonnes
        self.tree.heading("Code", text="Code", command=lambda: self.sort_column("Code", False))
        self.tree.heading("Nom", text="Nom", command=lambda: self.sort_column("Nom", False))
        self.tree.heading("Prix", text="Prix", command=lambda: self.sort_column("Prix", False))
        self.tree.heading("Stock", text="Stock", command=lambda: self.sort_column("Stock", False))

        # Ajout des colonnes avec une largeur augmentée de 50%
        self.tree.column("Code", width=int(100 * 1.5))
        self.tree.column("Nom", width=int(150 * 1.5))
        self.tree.column("Prix", width=int(100 * 1.5))
        self.tree.column("Stock", width=int(100 * 1.5))

        # Insertion des données (exemples)
        self.insert_data("123456", "Veste bouée", 249.90, "50", "veste_bouee.jpg")
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
            "Veste bouée": "veste_bouee.png",
            "Veste parachute": "veste_parachute.png",
            "Veste chauffante": "veste_chauffante.png",
            "Veste réfrigérée": "veste_refrigeree.png",
        }

    def insert_data(self, code, name, price, stock, image):
        self.tree.insert("", tk.END, values=(code, name, price, stock, image))

    def show_image(self, event):
        item = self.tree.selection()[0]
        article_name = self.tree.item(item, "values")[1]
        image_name = self.image_dict.get(article_name, "")

        if image_name:
            image_path = f"/home/user/Documents/ProjetPythonNIIINE/Logistique/{image_name}"
            img = tk.PhotoImage(file=image_path)

            for widget in self.root.grid_slaves():
                if isinstance(widget, tk.Label):
                    widget.destroy()

            image_label = tk.Label(self.root, image=img)
            image_label.photo = img
            image_label.grid(row=0, column=5, padx=0, pady=0, rowspan=100, sticky="n")

    def validate(self):
        num_articles_to_withdraw = int(self.num_articles_entry.get())
        selected_item = self.tree.selection()[0]
        current_stock = int(self.tree.item(selected_item, "values")[3])
        new_stock = max(0, current_stock - num_articles_to_withdraw)
        self.tree.set(selected_item, "Stock", new_stock)

        # Ajoutez ici tout autre traitement nécessaire après la validation

        # Effacer le contenu de la zone de saisie
        self.num_articles_entry.delete(0, tk.END)

    def sort_column(self, col, reverse):
        items = [(self.tree.set(k, col), k) for k in self.tree.get_children("")]
        items.sort(reverse=reverse)

        for index, (val, k) in enumerate(items):
            self.tree.move(k, "", index)

        self.tree.heading(col, command=lambda: self.sort_column(col, not reverse))

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
