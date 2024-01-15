from tkinter import Frame, Label, Button, ttk, Tk
import tkinter as tk
import sys
sys.path.insert(0,'odoo')
from intregration import ERP

class BaseView(tk.Tk):
    """Classe de base pour les vues."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"{self.screen_width}x{self.screen_height}+0+0")


class ProductionPage(Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.label = Label(self, text="Production", font=('Helvetica', 24))
        self.label.pack(pady=10)

        # Création de la grille pour afficher les articles
        self.tree = ttk.Treeview(self, columns=("Numéro d'OF", "Date", "Quantité à réaliser", "Quantité en production"), show="headings")
 
        # Configuration des en-têtes de colonnes
        self.tree.heading("Numéro d'OF", text="Numéro d'OF", command=lambda: self.sort_column("Numéro d'OF", False))
        self.tree.heading("Date", text="Date", command=lambda: self.sort_column("Date", False))
        self.tree.heading("Quantité à réaliser", text="Quantité à réaliser", command=lambda: self.sort_column("Quantité à réaliser", False))
        self.tree.heading("Quantité en production", text="Quantité en production", command=lambda: self.sort_column("Quantité en production", False))
 
        # Ajout des colonnes avec une largeur augmentée de 50%
        self.tree.column("Numéro d'OF", width=int(150 * 1.5), anchor="center")
        self.tree.column("Date", width=int(150 * 1.5), anchor="center")
        self.tree.column("Quantité à réaliser", width=int(150 * 1.5), anchor="center")
        self.tree.column("Quantité en production", width=int(150 * 1.5), anchor="center")

        self.tree.pack()

        # Ajout d'une instance de la classe ERP comme attribut de la classe HomeView
        self.erp_instance = ERP()

        # Appeler la méthode pour obtenir les informations des produits et afficher le tableau
        self.affichage_tableau()

        # Ajouter un bouton pour activer la modification du stock
        self.modify_stock_button = Button(self, text="Modifier", command=self.modif_stock)
        self.modify_stock_button.pack(pady=10)

    def affichage_tableau(self):
        # Utiliser l'instance de la classe ERP
        self.erp_instance.obtenir_informations_ordres_fabrication()

        # Effacer les éléments existants dans la Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Ajouter les nouvelles données obtenues à la Treeview
        for i in range(len(self.erp_instance.ordres_fabrication)):
            # Utiliser anchor pour centrer le texte
            self.tree.insert("", "end", values=(self.erp_instance.ordres_fabrication[i], self.erp_instance.dates_ordres_fabrication[i], 
                                                self.erp_instance.quantite_a_produire[i], self.erp_instance.qty_producing[i]))

    def update_table(self):
        # Effacer les éléments existants dans la Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Ajouter les nouvelles données obtenues à la Treeview après mise à jour
        for i in range(len(self.erp_instance.ordres_fabrication)):
            self.tree.insert("", "end", values=(self.erp_instance.ordres_fabrication[i], self.erp_instance.dates_ordres_fabrication[i], 
                                                self.erp_instance.quantite_a_produire[i], self.erp_instance.qty_producing[i]))

    def sort_column(self, col, reverse):
        # Obtenez les données actuelles de la Treeview
<<<<<<< HEAD
        data = [(self.tree.set(child, "Nom"), self.tree.set(child, "Prix"), self.tree.set(child, "Référence Interne"), self.tree.set(child, "Stock Disponible"))
=======
        data = [(self.tree.set(child, "Numéro d'OF"), self.tree.set(child, "Date"),
                self.tree.set(child, "Quantité à réaliser"), self.tree.set(child, "Quantité en production"))
>>>>>>> f70424dbcfd7828e2809e49fced72745ab248805
                for child in self.tree.get_children("")]
        
        # Triez les données en fonction de la colonne spécifiée
<<<<<<< HEAD
        data.sort(key=lambda x: x[int(col == "Prix")], reverse=reverse)
        
=======
        col_index = {"Numéro d'OF": 0, "Date": 1, "Quantité à réaliser": 2, "Quantité en production": 3}[col]
        data.sort(key=lambda x: x[col_index], reverse=reverse)

>>>>>>> f70424dbcfd7828e2809e49fced72745ab248805
        # Effacez les éléments existants dans la Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Ajoutez les données triées à la Treeview
        for item in data:
            self.tree.insert("", "end", values=item)

    def modif_stock(self):
        # Création du rectangle pour entrer le nombre d'articles
        self.entry_frame = Tk.Frame(self.master)
        self.entry_label = Tk.Label(self.entry_frame, text="Ajustement stock:")
        self.entry_label.grid(row=0, column=0, padx=5, pady=5)
 
        self.num_articles_entry = Tk.Entry(self.entry_frame)
        self.num_articles_entry.grid(row=0, column=1, padx=5, pady=5)
 
        # Création du bouton Valider
        self.validate_button = Tk.Button(self.entry_frame, text="Valider", command=self.validate)
        self.validate_button.grid(row=0, column=2, padx=5, pady=5, sticky="e")
 
        self.entry_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    def validate(self):
        # Mettez ici le code pour valider et modifier le stock
        pass


if __name__ == "__main__":
    root = BaseView()
    app = ProductionPage(master=root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()