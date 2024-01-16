import sys
sys.path.insert(0,'odoo')
from intregration import ERP
 
from tkinter import Tk, Label, Entry, Button, Frame, messagebox, ttk
import tkinter as tk

 
 
class Application(Tk):
    def __init__(self):
        super().__init__()
 
        # Créer les variables d'entrée
        self.entry_username = tk.StringVar()
        self.entry_password = tk.StringVar()
 
        self.title("Application CyberVest")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
 
        self.background_frame = Frame(self, bg="#DAD7D7")
        self.background_frame.place(relwidth=1, relheight=1)
 
        # Création d'un bouton pour quitter l'application
        self.bouton_quit = Button(self, text="Quitter", fg="#296EDF", bg="#DAD7D7", font=("Arial", 20), command=self.destroy)
        self.bouton_quit.pack(side="bottom", anchor="se", pady=10, padx=10)  # Positionne le bouton en bas à droite
 
        self.erp = ERP("db_cybervest")
        self.login_page()
 
    #Création de la page login
    def login_page(self):
     # Création de la frame pour la page login
        self.login_frame = tk.Frame(self)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")
 
        label_username = tk.Label(self.login_frame, text="Nom d'utilisateur:")
        label_password = tk.Label(self.login_frame, text="Mot de passe:")
 
        self.entry_username = tk.Entry(self.login_frame)
        self.entry_password = tk.Entry(self.login_frame, show="*")
        button_login = tk.Button(self.login_frame, text="Connexion", command=self.login)
 
        label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        label_password.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
 
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)
        button_login.grid(row=2, column=1, pady=20)
 
        
 
    def login(self):
        # Créer l'instance de la classe ERP ici, après que l'utilisateur ait cliqué sur le bouton de connexion.
        
        if self.erp.connexion( self.entry_username.get(), self.entry_password.get()) == 2 :
            self.pageProd()
        elif self.erp.connexion( self.entry_username.get(), self.entry_password.get()) == 6:
            self.pageAdmin()

        else:
            self.pageLog()


    def pageProd(self):

        # Supprime les widgets de la page de connexion
        self.login_frame.place_forget()
        #Supprime page admin si afficher
        self.page_admin_frame.place_forget()
        
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

        # Appeler la méthode pour obtenir les informations des produits et afficher le tableau
        self.affichage_tableau()

        # Ajouter un bouton pour activer la modification du stock
       # self.modify_stock_button = Button(self, text="Modifier", command=self.modif_stock)
        #self.modify_stock_button.pack(pady=10)


    def pageLog(self):

        # Supprime les widgets de la page de connexion
        self.login_frame.place_forget()
        #Supprime page admin si afficher
        self.page_admin_frame.place_forget()
        
        
        self.label = Label(self, text="Logistique", font=('Helvetica', 24))
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

        # Appeler la méthode pour obtenir les informations des produits et afficher le tableau
        self.affichage_tableau()

        # Ajouter un bouton pour activer la modification du stock
       # self.modify_stock_button = Button(self, text="Modifier", command=self.modif_stock)
        #self.modify_stock_button.pack(pady=10)

    def pageAdmin(self):

        # Supprime les widgets de la page de connexion
        self.login_frame.place_forget()
        #Création de la page
        self.page_admin_frame = tk.Frame(self,bg="#DAD7D7")
        self.page_admin_frame.place(relx=0, rely=0, relwidth=1, relheight=0.9)
        #Creation bouton pour aller page prod
        self.Button_prod = tk.Button(self.page_admin_frame, text="Production",fg="black", bg="#DAD7D7", font=("Arial", 20), command=lambda: [self.pageProd(), self.Boutton_retour()])
        self.Button_prod.place(relx=0.3, rely=0.5, anchor="center")
        #Creation bouton pour aller page logistique
        self.Button_logis = tk.Button(self.page_admin_frame, text="Logistique",fg="black", bg="#DAD7D7", font=("Arial", 20), command=lambda: [self.pageLog(), self.Boutton_retour()])
        self.Button_logis.place(relx=0.5, rely=0.5, anchor="center")
        #Creation bouton pour aller page commerce
        self.Button_commerce = tk.Button(self.page_admin_frame, text="Commerce",fg="black", bg="#DAD7D7", font=("Arial", 20),command=lambda: [self.pageVente(), self.Boutton_retour()])
        self.Button_commerce.place(relx=0.7, rely=0.5, anchor="center")

    def pageVente(self):
        print("ok")

    def Boutton_retour(self):
        #Creation bouton pour aller retourner menu admin
        self.Button_retour = tk.Button(self, text="Retour",fg="black", bg="#DAD7D7", font=("Arial", 20), command=self.Retour)
        self.Button_retour.place(relx=0.1, rely=0.9, anchor="sw")

    def Retour(self):
        #Fonction pour revenir sur le menu admin
        self.Button_retour.place_forget()

    def affichage_tableau(self):
        # Utiliser l'instance de la classe ERP
        self.erp.obtenir_informations_produits()

        # Afficher les valeurs récupérées pour le débogage
        print("Nom des articles:", self.erp.nom_article)
        print("Prix des articles:", self.erp.prix_article)
        print("Référence Interne:", self.erp.reference_interne)
        print("Stock Disponible:", self.erp.stock_disponible)

        # Effacer les éléments existants dans la Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Ajouter les nouvelles données obtenues à la Treeview
        for i in range(len(self.erp.nom_article)):
            # Utiliser anchor pour centrer le texte
            self.tree.insert("", "end", values=(self.erp.nom_article[i], self.erp.prix_article[i],
                                                self.erp.reference_interne[i], self.erp.stock_disponible[i]))

    def update_table(self):
        # Effacer les éléments existants dans la Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Ajouter les nouvelles données obtenues à la Treeview après mise à jour
        for i in range(len(self.erp_instance.ordres_fabrication)):
            self.tree.insert("", "end", values=(self.erp.ordres_fabrication[i], self.erp.dates_ordres_fabrication[i], 
                                                self.erp.quantite_a_produire[i], self.erp.qty_producing[i]))

    def sort_column(self, col, reverse):
        # Obtenez les données actuelles de la Treeview
        data = [(self.tree.set(child, "Numéro d'OF"), self.tree.set(child, "Date"),
                self.tree.set(child, "Quantité à réaliser"), self.tree.set(child, "Quantité en production"))
                for child in self.tree.get_children("")]
        
        # Triez les données en fonction de la colonne spécifiée
        col_index = {"Numéro d'OF": 0, "Date": 1, "Quantité à réaliser": 2, "Quantité en production": 3}[col]
        data.sort(key=lambda x: x[col_index], reverse=reverse)

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



        self.stock_entry = Entry(self)
        self.stock_entry.grid(row=3, column=1, padx=5, pady=5)

        # Ajout du bouton Valider
        self.validate_stock_button = Button(self, text="Valider", command=self.update_stock)
        self.validate_stock_button.grid(row=3, column=2, padx=5, pady=5, sticky="e")
 
 
 
 
    def affichage_tableau(self):
        # Utiliser l'instance de la classe ERP
        self.erp.obtenir_informations_produits()
 
        # Afficher les valeurs récupérées pour le débogage
        print("Nom des articles:", self.erp.nom_article)
        print("Prix des articles:", self.erp.prix_article)
        print("Référence Interne:", self.erp.reference_interne)
        print("Stock Disponible:", self.erp.stock_disponible)
 
        # Effacer les éléments existants dans la Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
 
        # Ajouter les nouvelles données obtenues à la Treeview
        for i in range(len(self.erp.nom_article)):
            # Utiliser anchor pour centrer le texte
            self.tree.insert("", "end", values=(self.erp.nom_article[i], self.erp.prix_article[i],
                                                self.erp.reference_interne[i], self.erp.stock_disponible[i]))
 
    def update_table(self):
        # Effacer les éléments existants dans la Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
 
        # Ajouter les nouvelles données obtenues à la Treeview après mise à jour
        for i in range(len(self.erp_instance.ordres_fabrication)):
            self.tree.insert("", "end", values=(self.erp.ordres_fabrication[i], self.erp.dates_ordres_fabrication[i],
                                                self.erp.quantite_a_produire[i], self.erp.qty_producing[i]))
 
    def sort_column(self, col, reverse):
        # Obtenez les données actuelles de la Treeview
        data = [(self.tree.set(child, "Numéro d'OF"), self.tree.set(child, "Date"),
                self.tree.set(child, "Quantité à réaliser"), self.tree.set(child, "Quantité en production"))
                for child in self.tree.get_children("")]
        
        # Triez les données en fonction de la colonne spécifiée
        col_index = {"Numéro d'OF": 0, "Date": 1, "Quantité à réaliser": 2, "Quantité en production": 3}[col]
        data.sort(key=lambda x: x[col_index], reverse=reverse)
 
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
 
 
 
if __name__ == "__main__":
    app = Application()
    app.mainloop()