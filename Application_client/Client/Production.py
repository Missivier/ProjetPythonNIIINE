import tkinter as tk
from tkinter import ttk, Label, Frame, Button, messagebox
import sys
sys.path.insert(0, 'odoo')
from intregration import ERP

class ProductionPage(Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.label = Label(self, text="Production!", font=('Helvetica', 24))
        self.label.pack(pady=10)

        # Création de la grille pour afficher les articles
        self.tree = ttk.Treeview(self, columns=("Numéro OF", "Date", "Quantité Produite"), show="headings")

        # Configuration des en-têtes de colonnes
        self.tree.heading("Numéro OF", text="Numéro OF", command=lambda: self.sort_column("Numéro OF", False))
        self.tree.heading("Date", text="Date", command=lambda: self.sort_column("Date", False))
        self.tree.heading("Quantité Produite", text="Quantité Produite", command=lambda: self.sort_column("Quantité Produite", False))

        # Ajout des colonnes avec une largeur augmentée de 50%
        self.tree.column("Numéro OF", width=int(150 * 1.5), anchor="center")
        self.tree.column("Date", width=int(100 * 1.5), anchor="center")
        self.tree.column("Quantité Produite", width=int(100 * 1.5), anchor="center")

        self.tree.pack()

        # Ajout d'une instance de la classe ERP comme attribut de la classe HomeView
        self.erp_instance = ERP()

        # Appeler la méthode pour obtenir les informations des produits et afficher le tableau
        self.affichage_tableau()

        # Ajouter un bouton pour activer la modification du stock
        self.modify_stock_button = Button(self, text="Modifier le stock", command=self.modif_stock)
        self.modify_stock_button.pack(pady=10)

        # Ajout d'un gestionnaire d'événements pour détecter le clic sur une ligne du tableau
        self.tree.bind("<ButtonRelease-1>", self.on_click)

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
        data = [(self.tree.set(child, "Nom"), self.tree.set(child, "Prix"), self.tree.set(child, "Référence Interne"),
                 self.tree.set(child, "Stock Disponible"))
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
        self.entry_frame = tk.Frame(self.master)
        self.entry_label = tk.Label(self.entry_frame, text="Ajustement stock:")
        self.entry_label.grid(row=0, column=0, padx=5, pady=5)

        self.num_articles_entry = tk.Entry(self.entry_frame)
        self.num_articles_entry.grid(row=0, column=1, padx=5, pady=5)

        # Création du bouton Valider
        self.validate_button = tk.Button(self.entry_frame, text="Valider", command=self.validate)
        self.validate_button.grid(row=0, column=2, padx=5, pady=5, sticky="e")

        self.entry_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    def validate(self):
        # Mettez ici le code pour valider et modifier le stock
        # Vérifier si une ligne est sélectionnée
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Sélection nécessaire", "Veuillez sélectionner une ligne.")
            return

        # Afficher une messagebox avec le choix "Valider" ou "Annuler"
        response = messagebox.askquestion("Validation", "Voulez-vous valider la quantité produite?", icon="warning")

        if response == "yes":
            # Retirer la ligne sélectionnée
            self.tree.delete(selected_item)

            # Récupérer la quantité produite à partir de la ligne sélectionnée
            quantite_produite = self.tree.item(selected_item, "values")[2]

            # Mettez ici le code pour renvoyer la quantité produite à la classe d'intégration (self.erp_instance)
            self.erp_instance.envoyer_quantite_produite(quantite_produite)

            # Afficher un message de confirmation
            messagebox.showinfo("Confirmation", "Validation réussie!")
        else:
            # Afficher un message d'annulation
            messagebox.showinfo("Annulation", "Validation annulée.")

        # Détruire le cadre d'entrée après validation ou annulation
       
