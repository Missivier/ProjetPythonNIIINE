import tkinter as tk
from tkinter import ttk, Tk, messagebox


from Page_init import page_init
from Page_Login import page_login
from Page_Prod import page_prod
from Page_Admin import page_admin
from Page_Logistique import page_logistique
from Page_Commerce import page_commerce
#---------------------------------------------------------------------------------------------------
#===================================================================================================
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        

        #Creation de la page
        page_init(self)
#---------------------------------------------------------------------------------------------------
        # Création de la frame pour la page login
        page_login(self)
#---------------------------------------------------------------------------------------------------
        #Page production
        page_prod(self)
#---------------------------------------------------------------------------------------------------
        # Page admin
        page_admin(self)
#---------------------------------------------------------------------------------------------------
        # Page logistique
        page_logistique(self)
#---------------------------------------------------------------------------------------------------
        # Page commerce
        page_commerce(self)
#---------------------------------------------------------------------------------------------------
        # Bouton déconnection
        self.button_deconnexion = tk.Button(self, text="Déconnexion", command=self.hide_retour_login)
#---------------------------------------------------------------------------------------------------
        # Bouton retour admin
        self.button_return = tk.Button(self, text="Retour", command=self.show_admin_page)
           

#===================================================================================================
# Fonction du login
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "1" and password == "1":
            self.hide_login_page()
            self.show_prod_page()
            self.show_button_deconnexion()

        elif username == "0" and password == "0":
            self.hide_login_page()
            self.show_admin_page()
            self.show_button_deconnexion()

        elif username == "2" and password == "2":
            self.hide_login_page()
            self.show_logis_page()
            self.show_button_deconnexion()

        elif username == "3" and password == "3":
            self.hide_login_page()
            self.show_commerce_page()
            self.show_button_deconnexion()
        else:
            messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect")
    def show_page_login(self):
        self.entry_password.delete(0, tk.END)
        self.entry_username.delete(0, tk.END)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")
    def hide_login_page(self):
        self.login_frame.place_forget()
    def hide_retour_login(self):
        self.page_prod_frame.place_forget()        
        self.page_logis_frame.place_forget()        
        self.page_admin_frame.place_forget()
        self.page_commerce_frame.place_forget()
        self.hide_button_return()
        self.hide_button_deconnexion()
        self.show_page_login()
#---------------------------------------------------------------------------------------------------
# Fonction page production
    def show_prod_page(self):
        self.page_prod_frame.place(relx=0, rely=0, relwidth=1, relheight=0.9)
#---------------------------------------------------------------------------------------------------
#Fonction page logistique
    def show_logis_page(self):
        self.page_logis_frame.place(relx=0, rely=0, relwidth=1, relheight=0.9)
#---------------------------------------------------------------------------------------------------
#Fonction page commerce
    def show_commerce_page(self):
        self.page_commerce_frame.place(relx=0, rely=0, relwidth=1, relheight=0.9)
#---------------------------------------------------------------------------------------------------
#Fonction page admin
    def show_admin_page(self):
        self.page_admin_frame.place(relx=0, rely=0, relwidth=1, relheight=0.9)
        self.page_prod_frame.place_forget()        
        self.page_logis_frame.place_forget()
        self.page_commerce_frame.place_forget()
        self.button_return.place_forget()
        

    def show_prod_page_admin(self):
        self.page_admin_frame.place_forget()
        self.show_prod_page()
        self.show_button_return()

    def show_logis_page_admin(self):
        self.page_admin_frame.place_forget()
        self.show_logis_page()
        self.show_button_return()

    def show_commerce_page_admin(self):
        self.page_admin_frame.place_forget()
        self.show_commerce_page()
        self.show_button_return()
#---------------------------------------------------------------------------------------------------
#Boutton retour
    def show_button_return(self):
        self.button_return.place(relx=0, rely=1, anchor='sw') 
    def hide_button_return(self):
        self.button_return.place_forget()
#---------------------------------------------------------------------------------------------------
#Fonction deconnexion
    def show_button_deconnexion(self):
        self.button_deconnexion.place(relx=0.92, rely=0.03)
    def hide_button_deconnexion(self):
        self.button_deconnexion.place_forget()
    
def show_image(self, event):
         # Vérifier s'il y a une sélection dans le Treeview
        if not self.tree.selection():
            return
        # Récupération de la ligne sélectionnée
        item = self.tree.selection()[0]
 
        # Récupération du nom de l'article associé à la ligne sélectionnée
        article_name = self.tree.item(item, "values")[1]
 
        # Récupération du nom de l'image associée à l'article
        image_name = self.image_dict.get(article_name, "")
 
        if image_name:
            # Affichage de l'image dans un Label à l'intérieur de la même fenêtre
            image_path = f"/home/user/Documents/ProjetPythonNIIINE/Login/{image_name}"
            img = tk.PhotoImage(file=image_path)
 
            # Supprimer l'ancien Label s'il existe
            for widget in self.root.grid_slaves():
                if isinstance(widget, tk.Label):
                    widget.destroy()
 
            # Création d'un widget Label pour afficher l'image à droite
            image_label = tk.Label(self.page_logis_frame, image=img)
            image_label.photo = img
            image_label.grid(row=0, column=5, padx=0, pady=0, rowspan=100, sticky="n")  # Ajustez la position et la colonne selon vos besoins
 
        else:
                print("Image introuvable pour cet article.")
################################################################################################
if __name__=="__main__":
    myApp = App()
    myApp.mainloop()

