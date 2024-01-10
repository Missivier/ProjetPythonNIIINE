        # Page logistique
import tkinter as tk
from tkinter import ttk


def page_logistique(self, show_image,edit_stock):
        '''
        '''
        #self.show_image = show_image
        #self.edit_stock = edit_stock
        #Création de la page
        self.page_logis_frame = tk.Frame(self,bg="#DAD7D7")

        #Création de deux zone d'affichage
        self.left_frame = tk.Frame(self.page_logis_frame,bg="#DAD7D7")
        self.right_frame = tk.Frame(self.page_logis_frame,bg="#DAD7D7")
        self.left_frame.pack(side="top", padx=10, pady=10, anchor="nw")
        self.right_frame.pack(side="right", padx=10, pady=10)

        # Création de la grille pour afficher les articles
        self.table = ttk.Treeview(self.left_frame, columns=("Code", "Nom", "Prix", "Stock"), show="headings")
        self.table.pack()

        #data du tableau
        self.data = [
            ("123456", "Veste bouée", "249.90", "25","veste_bouee.png"),
            ("123457", "Veste parachute", "544.90", "30","veste parachute.png"),
            ("123458", "Veste chauffante", "119.90", "20","veste chauffante.png"),
            ("123459", "Veste réfrigérée", "129.90", "20","veste réfrigérée.png"),
        ]

        # Configuration des en-têtes de colonnes
        self.table.heading("Code", text="Code")
        self.table.heading("Nom", text="Nom")
        self.table.heading("Prix", text="Prix")
        self.table.heading("Stock", text="Stock")
        '''
        self.table.bind("<ButtonRelease-1>")
        self.table.bind("<Double-ButtonRelease-1>")
        '''
        for item in self.data:
            self.table.insert("", "end", values=item)


'''
        self.image_label = tk.Label(self.right_frame)
        self.image_label.pack()    

        '''
######################################################################