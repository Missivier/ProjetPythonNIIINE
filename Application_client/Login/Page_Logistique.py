        # Page logistique
import tkinter as tk
from tkinter import ttk

def page_logistique(self,show_image):
        #Création de la page
        self.page_logis_frame = tk.Frame(self,bg="#DAD7D7")

        # Création de la grille pour afficher les articles
        self.tree = ttk.Treeview(self.page_logis_frame, columns=("Code", "Nom", "Prix", "Stock"), show="headings")
 
        # Configuration des en-têtes de colonnes
        self.tree.heading("Code", text="Code", command=lambda: self.sort_column("Code", False))
        self.tree.heading("Nom", text="Nom", command=lambda: self.sort_column("Nom", False))
        self.tree.heading("Prix", text="Prix", command=lambda: self.sort_column("Prix", False))
        self.tree.heading("Stock", text="Stock", command=lambda: self.sort_column("Stock", False))
        #self.tree.pack(fill="both", expand=True)

        # Ajout des colonnes avec une largeur augmentée de 50%
        self.tree.column("Code", width=int(100 * 1.5))
        self.tree.column("Nom", width=int(150 * 1.5))
        self.tree.column("Prix", width=int(100 * 1.5))
        self.tree.column("Stock", width=int(100 * 1.5))
        data = [
            ("123456", "Veste bouée", "249.90", "25","veste_bouee.jpg"),
            ("123457", "Veste parachute", "544.90", "30","veste parachute.jpg"),
            ("123458", "Veste chauffante", "119.90", "20","veste chauffante.jpg"),
            ("123459", "Veste réfrigérée", "129.90", "20""veste réfrigérée.jpg"),
        ]

        for item in data:
            self.tree.insert("", "end", values=item)

        # Binding de l'événement de clic
        self.tree.bind("<ButtonRelease-1>", self.show_image)
 
        # Placement du Treeview
        self.tree.grid(row=0, column=0, padx=10, pady=10, columnspan=5)
 
        # Création du rectangle pour entrer le nombre d'articles
        self.entry_frame = tk.Frame(self.page_logis_frame)
        self.entry_label = tk.Label(self.entry_frame, text="Ajustement stock:")
        self.entry_label.grid(row=0, column=0, padx=5, pady=5)
 
        self.num_articles_entry = tk.Entry(self.entry_frame)
        self.num_articles_entry.grid(row=0, column=1, padx=5, pady=5)
 
        # Création du bouton Valider
        self.validate_button = tk.Button(self.page_logis_frame.entry_frame, text="Valider", command=self.validate)
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
        # Insertion des données dans le Treeview
        self.tree.insert("", tk.END, values=(code, name, price, stock, image))
 
def validate(self):
        # Ajoutez ici le code pour traiter la validation du nombre d'articles
        # par exemple, récupérez la valeur de self.num_articles_entry.get()
        pass
 
def sort_column(self, col, reverse):
        # Trier la colonne
        items = [(self.tree.set(k, col), k) for k in self.tree.get_children("")]
        items.sort(reverse=reverse)
 
        # Réorganiser les éléments dans le Treeview
        for index, (val, k) in enumerate(items):
            self.tree.move(k, "", index)
 
        # Mettre à jour l'ordre de tri pour la colonne suivante
        self.tree.heading(col, command=lambda: self.sort_column(col, not reverse))
 