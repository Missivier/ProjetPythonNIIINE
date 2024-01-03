import tkinter as tk
from tkinter import ttk

class ArticlePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des Articles et Stocks")

        # Création de la grille pour afficher les articles
        self.tree = ttk.Treeview(root, columns=("Code", "Nom", "Prix", "Image", "Stock"), show="headings")

        # Configuration des en-têtes de colonnes
        self.tree.heading("Code", text="Code")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Prix", text="Prix")
        self.tree.heading("Image", text="Image")
        self.tree.heading("Stock", text="Stock")

        # Ajout des colonnes
        self.tree.column("Code", width=100)
        self.tree.column("Nom", width=150)
        self.tree.column("Prix", width=100)
        self.tree.column("Image", width=150)
        self.tree.column("Stock", width=100)

        # Insertion des données (exemples)
        self.insert_data("001", "Article 1", 20.0, "image1.jpg", 50)
        self.insert_data("002", "Article 2", 25.0, "image2.jpg", 30)
        self.insert_data("003", "Article 3", 30.0, "image3.jpg", 40)
        self.insert_data("004", "Article 4", 15.0, "image4.jpg", 20)

        # Placement du Treeview
        self.tree.grid(row=0, column=0, padx=10, pady=10, columnspan=5)

    def insert_data(self, code, name, price, image, stock):
        # Insertion des données dans le Treeview
        self.tree.insert("", tk.END, values=(code, name, price, image, stock))

if __name__ == "__main__":
    root = tk.Tk()
    app = ArticlePage(root)
    root.mainloop()
