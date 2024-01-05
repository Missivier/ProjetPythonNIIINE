from tkinter import Frame, Label, Button, ttk, Tk
import sys
sys.path.insert(0,'odoo')
from intregration import ERP

class BaseView(Tk):
    """Classe de base pour les vues."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.attributes('-fullscreen', True)  # Configurer la fenêtre principale en plein écran
        self.title("Votre Titre")

    def toggle_fullscreen(self, event=None):
        self.attributes('-fullscreen', not self.attributes('-fullscreen'))

    def end_fullscreen(self, event=None):
        self.attributes('-fullscreen', False)


class HomeView(Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.label = Label(self, text="Bienvenue sur la page d'accueil !", font=('Helvetica', 24))
        self.label.pack(pady=10)

        # Création de la grille pour afficher les articles
        self.tree = ttk.Treeview(self, columns=("Nom", "Prix", "Référence Interne", "Stock Disponible"), show="headings")
 
        # Configuration des en-têtes de colonnes
        self.tree.heading("Nom", text="Nom", command=lambda: self.sort_column("Nom", False))
        self.tree.heading("Prix", text="Prix", command=lambda: self.sort_column("Prix", False))
        self.tree.heading("Référence Interne", text="Référence Interne", command=lambda: self.sort_column("Référence Interne", False))
        self.tree.heading("Stock Disponible", text="Stock Disponible", command=lambda: self.sort_column("Stock Disponible", False))
 
        # Ajout des colonnes avec une largeur augmentée de 50%
        self.tree.column("Nom", width=int(150 * 1.5), anchor="center")
        self.tree.column("Prix", width=int(100 * 1.5), anchor="center")
        self.tree.column("Référence Interne", width=int(100 * 1.5), anchor="center")
        self.tree.column("Stock Disponible", width=int(100 * 1.5), anchor="center")

        self.tree.pack()

        # Ajout d'une instance de la classe ERP comme attribut de la classe HomeView
        self.erp_instance = ERP()

        # Appeler la méthode pour obtenir les informations des produits et afficher le tableau
        self.affichage_tableau()

        # Ajouter un bouton pour activer la modification du stock
        self.modify_stock_button = Button(self, text="Modifier le stock", command=self.modif_stock)
        self.modify_stock_button.pack(pady=10)

    def affichage_tableau(self):
        # Utiliser l'instance de la classe ERP
        self.erp_instance.obtenir_informations_produits()

        # Effacer les éléments existants dans la Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Ajouter les nouvelles données obtenues à la Treeview
        for i in range(len(self.erp_instance.nom_article)):
            # Utiliser anchor pour centrer le texte
            self.tree.insert("", "end", values=(self.erp_instance.nom_article[i], self.erp_instance.prix_article[i], 
                                                self.erp_instance.reference_interne[i], self.erp_instance.stock_disponible[i]))

    def update_table(self):
        # Effacer les éléments existants dans la Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Ajouter les nouvelles données obtenues à la Treeview après mise à jour
        for i in range(len(self.erp_instance.nom_article)):
            self.tree.insert("", "end", values=(self.erp_instance.nom_article[i], self.erp_instance.prix_article[i], 
                                                self.erp_instance.reference_interne[i], self.erp_instance.stock_disponible[i]))

    def sort_column(self, col, reverse):
        # Obtenez les données actuelles de la Treeview
        data = [(self.tree.set(child, "Nom"), self.tree.set(child, "Prix"), self.tree.set(child, "Référence Interne"), self.tree.set(child, "Stock Disponible"))
                for child in self.tree.get_children("")]
        
        # Triez les données en fonction de la colonne spécifiée
        data.sort(key=lambda x: x[int(col == "Prix")], reverse=reverse)
        
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
