from tkinter import Frame, Label, Button, ttk
import sys
sys.path.insert(0,'odoo')
from intregration import ERP

class BaseView(Frame):
    """Classe de base pour les vues."""
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

class HomeView(Frame, ERP):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.label = Label(self, text="Bienvenue sur la page d'accueil !")
        self.label.pack(pady=10)

        # Création de la grille pour afficher les articles
        self.tree = ttk.Treeview(self, columns=("Nom", "Prix", "Référence Interne", "Stock Disponible"), show="headings")
 
        # Configuration des en-têtes de colonnes
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Prix", text="Prix")
        self.tree.heading("Référence Interne", text="Référence Interne")
        self.tree.heading("Stock Disponible", text="Stock Disponible")
 
        # Ajout des colonnes avec une largeur augmentée de 50%
        self.tree.column("Nom", width=int(150 * 1.5))
        self.tree.column("Prix", width=int(100 * 1.5))
        self.tree.column("Référence Interne", width=int(100 * 1.5))
        self.tree.column("Stock Disponible", width=int(100 * 1.5))

        self.tree.pack()

        # Ajout d'une instance de la classe ERP comme attribut de la classe HomeView
        self.erp_instance = ERP()

        # Appeler la méthode pour obtenir les informations des produits et afficher le tableau
        self.affichage_tableau()

    def affichage_tableau(self):
        # Utiliser l'instance de la classe ERP
        self.erp_instance.obtenir_informations_produits()

        # Effacer les éléments existants dans la Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Ajouter les nouvelles données obtenues à la Treeview
        for i in range(len(self.erp_instance.nom_article)):
            self.tree.insert("", "end", values=(self.erp_instance.nom_article[i], self.erp_instance.prix_article[i], 
                                                self.erp_instance.reference_interne[i], self.erp_instance.stock_disponible[i]))
