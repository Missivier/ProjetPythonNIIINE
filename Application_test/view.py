from tkinter import Frame, Label, Button, ttk, Tk, Entry
import sys
sys.path.insert(0, 'odoo')
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
        self.label.grid(row=0, column=0, pady=10, columnspan=5)

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
 
        # Utilisez grid au lieu de pack
        self.tree.grid(row=1, column=0, padx=10, pady=10, columnspan=5)
 
        # Ajout d'une instance de la classe ERP comme attribut de la classe HomeView
        self.erp_instance = ERP()
 
        # Appeler la méthode pour obtenir les informations des produits et afficher le tableau
        self.affichage_tableau()
 
        # Binding de l'événement de clic
        self.tree.bind("<ButtonRelease-1>", self.show_image)
 
        # Ajoutez la variable self.sort_order pour suivre l'état du tri (ascendant ou descendant)
        self.sort_order = {}

        # Configuration des en-têtes de colonnes
        columns = ("Nom", "Prix", "Référence Interne", "Stock Disponible")
        for col in columns:
            self.sort_order[col] = True  # Initialisation à True pour tri ascendant par défaut
            self.tree.heading(col, text=col, command=lambda c=col: self.sort_column(c))

        # Ajout de la case d'entrée pour la quantité d'articles à retirer
        self.stock_entry_label = Label(self, text="Affectation stock:")
        self.stock_entry_label.grid(row=3, column=0, padx=5, pady=5)

        self.stock_entry = Entry(self)
        self.stock_entry.grid(row=3, column=1, padx=5, pady=5)

        # Ajout du bouton Valider
        self.validate_stock_button = Button(self, text="Valider", command=self.update_stock)
        self.validate_stock_button.grid(row=3, column=2, padx=5, pady=5, sticky="e")

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
 
    def sort_column(self, col):
        # Obtenez l'état actuel du tri pour la colonne spécifiée
        reverse = self.sort_order[col]
        
        # Inversez l'état du tri pour la prochaine fois
        self.sort_order[col] = not reverse

        # Obtenez les données actuelles de la Treeview
        data = [(self.tree.set(child, "Nom"), self.tree.set(child, "Prix"), self.tree.set(child, "Référence Interne"), self.tree.set(child, "Stock Disponible"))
                for child in self.tree.get_children("")]

        # Triez les données en fonction de la colonne spécifiée et de l'état du tri
        data.sort(key=lambda x: x[int(col == "Prix")], reverse=reverse)

        # Effacez les éléments existants dans la Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Ajoutez les données triées à la Treeview
        for item in data:
            self.tree.insert("", "end", values=item)

    def update_stock(self):
        # Récupération de la quantité saisie dans la case d'entrée
        quantite = self.stock_entry.get()

        # Assurez-vous que la quantité est un nombre entier
        try:
            quantite = int(quantite)
        except ValueError:
            print("Veuillez saisir un nombre entier pour la quantité.")
            return

        # Stockage de la nouvelle quantité dans la variable new_stock
        self.new_stock = quantite

        # Obtenez la ligne sélectionnée
        item_selectionne = self.tree.selection()

        if not item_selectionne:
            print("Aucune ligne sélectionnée.")
            return

        # Obtenez le nom de l'article associé à la ligne sélectionnée
        nom_article = self.tree.item(item_selectionne, "values")[0]

        # Mise à jour du stock dans Odoo
        succes = self.erp_instance.update_odoo_stock(nom_article, quantite)

        if succes:
            # Affichage d'un message de confirmation dans le terminal
            print(f"Stock de {quantite} articles de '{nom_article}' mis à jour avec succès dans Odoo.")
        else:
            # En cas d'échec de la mise à jour dans Odoo
            print(f"Échec de la mise à jour du stock pour '{nom_article}' dans Odoo.")

        # Effacement de la case d'entrée et du bouton Valider après la mise à jour
        self.stock_entry.delete(0, 'end')
 
    def show_image(self, event):
        # Récupération de la ligne sélectionnée
        item = self.tree.selection()[0]
 
        # Récupération du nom de l'article associé à la ligne sélectionnée
        article_name = self.tree.item(item, "values")[0]  # Utilisez l'index 0 pour le nom de l'article

        # Afficher le nom de l'article dans le terminal
        print("Article sélectionné:", article_name)
 
        # Récupération de l'index associé à l'article
        article_index = self.get_article_index(article_name)
 
        # Récupération du chemin de l'image associée à l'article
        image_path = self.erp_instance.images_stock[article_index]
 
        # Supprimer l'ancien Label s'il existe
        for widget in self.grid_slaves():
            if isinstance(widget, Label) and widget != self.label:
                widget.destroy()
 
        if image_path:
            # Affichage de l'image dans un Label à l'intérieur de la même fenêtre
            img = PhotoImage(file=image_path)
 
            # Création d'un widget Label pour afficher l'image à droite
            image_label = Label(self, image=img)
            image_label.photo = img
            image_label.pack(side="right", padx=10, pady=10, fill="both", expand=True)
 
 
    def get_article_index(self, article_name):
        # Fonction utilitaire pour récupérer l'index de l'article dans self.erp_instance.images_stock
        for i, article in enumerate(self.erp_instance.images_stock):
            if article["name"] == article_name:
                return i
        return -1  # Retourne -1 si l'article n'est pas trouvé
