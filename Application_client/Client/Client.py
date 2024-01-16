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

        #Creation de la page Client
        self.title("Application CyberVest")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
        self.background_frame = Frame(self, bg="#DAD7D7")
        self.background_frame.place(relwidth=1, relheight=1)
 
        # Création d'un bouton pour quitter l'application
        self.bouton_quit = Button(self, text="Quitter", fg="#296EDF", bg="#DAD7D7", font=("Arial", 20), command=self.destroy)
        self.bouton_quit.pack(side="bottom", anchor="se", pady=10, padx=10)  # Positionne le bouton en bas à droite

        #connexion à L'ERP
        self.erp = ERP("db_cybervest")

        #Afficher La page de login
        self.login_page()
 
    #Création de la page login
    def login_page(self):
     # Création de la frame pour la page login
        self.login_frame = tk.Frame(self)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        border_frame = tk.Label(self.login_frame,bg="#333333")
        border_frame.grid(row=0, column=1, padx=10, pady=10)
 
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
        self.tree.column("Quantité en production", width=int(150 * 1.5), anchor="center")
        self.tree.column("Quantité à réaliser", width=int(150 * 1.5), anchor="center")

        self.tree.pack()
 
        # Appeler la méthode pour obtenir les informations des produits et afficher le tableau
        self.affichage_tableau_prod()
 
        # Ajouter un bouton pour activer la modification du stock
       # self.modify_stock_button = Button(self, text="Modifier", command=self.modif_stock)
        #self.modify_stock_button.pack(pady=10)
 
 
    def pageLog(self, master=None):
 
        # Supprime les widgets de la page de connexion
        self.login_frame.grid_forget()
         # Supprime le bouton Quitter
        self.bouton_quit.grid_forget()
 
        self.page_log_frame = tk.Frame(self)
        self.page_log_frame.place(relx=0, rely=0, relwidth=1, relheight=0.9)
 
        self.label = Label(self, text="Logistique", font=('Helvetica', 24))
        self.label.pack(pady=10)
 
        # Création de la grille pour afficher les articles
        self.tree = ttk.Treeview(self, columns=("Nom", "Prix", "Référence Interne", "Stock Disponible"), show="headings")
 
        # Configuration des en-têtes de colonnes
        self.tree.heading("Nom", text="Nom", command=lambda: self.sort_column_log("Nom", False))
        self.tree.heading("Prix", text="Prix", command=lambda: self.sort_column_log("Prix", False))
        self.tree.heading("Référence Interne", text="Référence Interne", command=lambda: self.sort_column_log("Référence Interne", False))
        self.tree.heading("Stock Disponible", text="Stock Disponible", command=lambda: self.sort_column_log("Stock Disponible", False))
 
        # Ajout des colonnes avec une largeur augmentée de 50%
        self.tree.column("Nom", width=int(150 * 1.5), anchor="center")
        self.tree.column("Prix", width=int(100 * 1.5), anchor="center")
        self.tree.column("Référence Interne", width=int(100 * 1.5), anchor="center")
        self.tree.column("Stock Disponible", width=int(100 * 1.5), anchor="center")
 
        self.tree.pack()
 
        # Appeler la méthode pour obtenir les informations des produits et afficher le tableau
        self.affichage_tableau_log()
 
        # Binding de l'événement de clic
        self.tree.bind("<ButtonRelease-1>", self.show_image_log)
 
        # Ajoutez la variable self.sort_order pour suivre l'état du tri (ascendant ou descendant)
        self.sort_order = {}
 
        # Configuration des en-têtes de colonnes
        columns = ("Nom", "Prix", "Référence Interne", "Stock Disponible")
        for col in columns:
            self.sort_order[col] = True  # Initialisation à True pour tri ascendant par défaut
            self.tree.heading(col, text=col, command=lambda c=col: self.sort_column_log(c))
 
        # Ajout de la case d'entrée pour la quantité d'articles à retirer
        self.stock_entry_label = Label(self.page_log_frame, text="Affectation stock:")
        self.stock_entry_label.place(relx=0.5, rely=0.4, anchor='center')
 
        self.stock_entry = Entry(self.page_log_frame)
        self.stock_entry.place(relx=0.49, rely=0.41)
 
        # Ajout du bouton Valider
        self.validate_stock_button = tk.Button(self.page_log_frame, text="Valider", command=self.update_stock_log)
        self.validate_stock_button.place(relx=0.55, rely=0.4, anchor='center')
 
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

        # Configuration des en-têtes de colonnes
        columns = ("Nom", "Prix", "Référence Interne", "Stock Disponible")
        for col in columns:
            self.sort_order[col] = True  # Initialisation à True pour tri ascendant par défaut
            self.tree.heading(col, text=col, command=lambda c=col: self.sort_column_log(c))

        # Ajout de la case d'entrée pour la quantité d'articles à retirer
        self.stock_entry_label = Label(self.page_log_frame, text="Affectation stock:")
        self.stock_entry_label.place(relx=0.5, rely=0.4, anchor='center') 

        self.stock_entry = Entry(self.page_log_frame)
        self.stock_entry.place(relx=0.48, rely=0.41) 

        # Ajout du bouton Valider
        self.validate_stock_button = tk.Button(self.page_log_frame, text="Valider", command=self.update_stock_log)
        self.validate_stock_button.place(relx=0.535, rely=0.405, anchor='center')

    def pageVente(self):
        print("ok")

    def Boutton_retour(self):
        #Creation bouton pour aller retourner menu admin
        self.Button_retour = tk.Button(self, text="Retour",fg="black", bg="#DAD7D7", font=("Arial", 20), command=self.Retour)
        self.Button_retour.place(relx=0.1, rely=0.9, anchor="sw")

    def Retour(self):
        #Fonction pour revenir sur le menu admin
        self.Button_retour.place_forget()

    def affichage_tableau_log(self):
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
        # Ajouter les nouvelles donné   es obtenues à la Treeview
        for i in range(len(self.erp.nom_article)):
            # Utiliser anchor pour centrer le texte
            self.tree.insert("", "end", values=(self.erp.nom_article[i], self.erp.prix_article[i],
                                                self.erp.reference_interne[i], self.erp.stock_disponible[i]))
 
    def update_table_prod(self):
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
 
 
 
 
    def affichage_tableau_prod(self):
        # Utiliser l'instance de la classe ERP
        self.erp.obtenir_informations_ordres_fabrication()
 
        # Afficher les valeurs récupérées pour le débogage
        print("Ordre fabrication:", self.erp.ordres_fabrication)
        print("Date ordre fabrication:", self.erp.dates_ordres_fabrication)
        print("Quantité à produire:", self.erp.quantite_a_produire)
        print("Quantité en production:", self.erp.qty_producing)
 
        # Effacer les éléments existants dans la Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
 
        # Ajouter les nouvelles données obtenues à la Treeview
        for i in range(len(self.erp.ordres_fabrication)):
            # Utiliser anchor pour centrer le texte
            self.tree.insert("", "end", values=(self.erp.ordres_fabrication[i], self.erp.dates_ordres_fabrication[i],
                                                self.erp.qty_producing[i], self.erp.quantite_a_produire[i]))
 
    def update_table(self):
        # Effacer les éléments existants dans la Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
 
        # Ajouter les nouvelles données obtenues à la Treeview après mise à jour
        for i in range(len(self.erp_instance.ordres_fabrication)):
            self.tree.insert("", "end", values=(self.erp.ordres_fabrication[i], self.erp.dates_ordres_fabrication[i],
                                                self.erp.quantite_a_produire[i], self.erp.qty_producing[i]))
 
    def sort_column_log(self, col):
        # Obtenez l'état actuel du tri pour la colonne spécifiée
        reverse = self.sort_order[col]

        # Inversez l'état du tri pour la prochaine fois
        self.sort_order[col] = not reverse

        # Obtenez les données actuelles de la Treeview
        data = [(self.tree.set(child, "Nom"), self.tree.set(child, "Prix"), self.tree.set(child, "Référence Interne"), self.tree.set(child, "Stock Disponible"))
                for child in self.tree.get_children("")]

        # Triez les données en fonction de la colonne spécifiée et de l'état du tri
        col_index = ["Nom", "Prix", "Référence Interne", "Stock Disponible"].index(col)
        data.sort(key=lambda x: x[col_index], reverse=reverse)

        # Effacez les éléments existants dans la Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Ajoutez les données triées à la Treeview
        for item in data:
            self.tree.insert("", "end", values=item)

 
    def modif_stock_log(self):
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

    def update_stock_log(self):
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
        succes = self.erp.update_odoo_stock(nom_article, quantite)

        if succes:
            # Affichage d'un message de confirmation dans le terminal
            print(f"Stock de {quantite} articles de '{nom_article}' mis à jour avec succès dans Odoo.")
        else:
            # En cas d'échec de la mise à jour dans Odoo
            print(f"Échec de la mise à jour du stock pour '{nom_article}' dans Odoo.")

        # Effacement de la case d'entrée et du bouton Valider après la mise à jour
        self.stock_entry.delete(0, 'end')
 
    def show_image_log(self, event):
        # Récupération de la ligne sélectionnée
        item = self.tree.selection()[0]
 
        # Récupération du nom de l'article associé à la ligne sélectionnée
        article_name = self.tree.item(item, "values")[0]  # Utilisez l'index 0 pour le nom de l'article

        # Afficher le nom de l'article dans le terminal
        print("Article sélectionné:", article_name)
 
        # Récupération de l'index associé à l'article
        article_index = self.get_article_index(article_name)
 
        # Récupération du chemin de l'image associée à l'article
        image_path = self.erp.images_stock[article_index]
 
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
 
    def get_article_index_log(self, article_name):
        # Fonction utilitaire pour récupérer l'index de l'article dans self.erp_instance.images_stock
        for i, article in enumerate(self.erp.images_stock):
            if article["name"] == article_name:
                return i
        return -1  # Retourne -1 si l'article n'est pas trouvé 
 
if __name__ == "__main__":
    app = Application()
    app.mainloop()