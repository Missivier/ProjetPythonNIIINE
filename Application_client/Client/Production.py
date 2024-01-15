import tkinter as tk
from tkinter import ttk, messagebox
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


class ProductionPage(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # Données à afficher dans le tableau
        data = [
            ("A1", "B1", "C1"),
            ("A2", "B2", "C2"),
            ("A3", "B3", "C3")
        ]

        # Création du tableau
        self.tree = ttk.Treeview(self, columns=("Numéro d'OF", "Date", "Quantité produite"), show="headings")

        # Configuration des en-têtes du tableau
        self.tree.heading("Numéro d'OF", text="Numéro d'OF")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Quantité produite", text="Quantité produite")

        # Ajout des données au tableau
        for row in data:
            self.tree.insert("", "end", values=row)

        # Liaison de l'événement de clic sur une ligne avec la fonction associée
        self.tree.bind("<ButtonRelease-1>", self.on_item_click)

        # Placement du tableau dans le cadre (Frame)
        self.tree.pack(pady=10)

    def on_item_click(self, event):
        # Récupérer l'élément sélectionné
        selected_item = self.tree.selection()

        if selected_item:
            # Récupérer les valeurs de l'élément sélectionné
            values = self.tree.item(selected_item, "values")

            # Afficher une boîte de dialogue pour valider la quantité
            result = messagebox.askquestion("Validation de la quantité", f"Valider la quantité produite ?", icon="question")

            # Supprimer la ligne si l'utilisateur clique sur "Valider"
            if result == "yes":
                self.tree.delete(selected_item)


if __name__ == "__main__":
    root = BaseView()
    app = ProductionPage(master=root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
