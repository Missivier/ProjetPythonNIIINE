# Page production
import tkinter as tk
from tkinter import ttk
from Style_tableau import  style_tableau

def page_prod(self):
        #Création del apage
        self.page_prod_frame = tk.Frame(self,bg="#DAD7D7")

        #Création du tableau
        self.tableau = ttk.Treeview(self.page_prod_frame, columns=("Colonne 1", "Colonne 2", "Colonne 3", "Colonne 4", "Colonne 5","Colonne 6","Validation"), show="headings")
        self.tableau.place(relx=0.01, rely=0.15)
        # Configurer les en-têtes de colonnes
        self.tableau.heading("Colonne 1", text="N° OF")
        self.tableau.heading("Colonne 2", text="Référence")
        self.tableau.heading("Colonne 3", text="Quantité")
        self.tableau.heading("Colonne 4", text="Date")
        self.tableau.heading("Colonne 5", text="Heure")
        self.tableau.heading("Colonne 6", text="Status")
        self.tableau.heading("Validation", text="Validation")

        for i in range(20):  # Exemple avec 20 lignes fictives
            self.tableau.insert("", "end", values=(f"Ligne {i+1} - Colonne 1", f"Ligne {i+1} - Colonne 2", f"Ligne {i+1} - Colonne 3", f"Ligne {i+1} - Colonne 4", f"Ligne {i+1} - Colonne 5", f"Ligne {i+1} - Colonne 6", ""))

              # Appliquer le quadrillage
        style = ttk.Style()
        style.configure("mystyle.Treeview", rowheight=30)
        style.map("mystyle.Treeview", background=[("selected", "#bce0ff")])
        style.configure("mystyle.Treeview", background="white", fieldbackground="white", foreground="black", font=('Arial', 10), borderwidth=0)
        self.tableau.configure(style="mystyle.Treeview")
        style_tableau(self)
        
        # Ajout ligne de délimitation
        self.border = tk.Frame(self.page_prod_frame, bg="black")
        self.border.place(relx=0, rely=0.11, relwidth=1, relheight=0.01)
        # Ajout nom menu
        self.title_frame = tk.Label(self.page_prod_frame,text="Liste OF production", bg="#DAD7D7",font=("Arial", 16))
        self.title_frame.place(relx=0.5, rely=0.05, anchor="center")
        # Ajout Production
        self.production_label = tk.Label(self.page_prod_frame, text="Menu Production", font=("Arial", 16), bg="#DAD7D7")
        self.production_label.place(relx=0.05, rely=0.05, anchor="center")