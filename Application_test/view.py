from tkinter import Frame, Label, Button, ttk

class BaseView(Frame):
    """Classe de base pour les vues."""
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

class HomeView(BaseView):
    """Vue pour la page d'accueil."""
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.label = Label(self, text="Bienvenue sur la page d'accueil !")
        self.label.pack(pady=10)
        self.button = Button(self, text="Aller à la fonctionnalité", command=self.affichage_tableau)
        self.button.pack(pady=10)

    def affichage_tableau(self):
        # Création de la grille pour afficher les articles
        self.tree = ttk.Treeview(self, columns=("Code", "Nom", "Prix", "Stock"), show="headings")
 
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

        # Ajouter des données d'exemple à la Treeview
        self.tree.insert("", "end", values=("001", "Article 1", "10.00", "50"))
        self.tree.insert("", "end", values=("002", "Article 2", "15.00", "30"))

        self.tree.pack()

    def sort_column(self, col, reverse):
        # Implémenter la logique de tri ici
        pass
