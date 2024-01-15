import sys
sys.path.insert(0,'odoo')
from intregration import ERP

import tkinter as tk
from tkinter import messagebox


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

         # Créer les variables d'entrée
        self.entry_username = tk.StringVar()
        self.entry_password = tk.StringVar()
        

        #Creation de la page
        page_init(self)
#---------------------------------------------------------------------------------------------------
        # Création de la frame pour la page login
        page_login(self,)
#---------------------------------------------------------------------------------------------------
        #Page production
        page_prod(self)
#---------------------------------------------------------------------------------------------------
        # Page admin
        page_admin(self)
#---------------------------------------------------------------------------------------------------
        # Page logistique
        page_logistique(self,show_image,edit_stock)
#---------------------------------------------------------------------------------------------------
        # Page commerce
        page_commerce(self)
#---------------------------------------------------------------------------------------------------
        # Bouton déconnection
        self.button_deconnexion = tk.Button(self, text="Déconnexion", command=self.hide_retour_login)
#---------------------------------------------------------------------------------------------------
        # Bouton retour admin
        self.button_return = tk.Button(self, text="Retour", command=self.show_admin_page)


        # Instance classe ERP
        self.erp = ERP("db_cybervest", self.entry_username.get(), self.entry_password.get())
           

#===================================================================================================
# Fonction du login

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
        selection = self.table.selection()
        if selection:
            item = self.table.item(selection[0])
            image_name = item['values'][4]
            try:
                image_path = f"/home/user/Documents/ProjetPythonNIIINE/Application_client/Image/{image_name}"  # Modifier le chemin vers votre dossier
                img = tk.PhotoImage(file=image_path)
                self.image_label.config(image=img)
                self.image_label.image = img
            except tk.TclError:
                # Gérer une éventuelle erreur si le chemin est incorrect ou si le fichier image est corrompu
                print("Erreur lors du chargement de l'image")

def edit_stock(self, event):
        col = self.table.identify_column(event.x)
        row = self.table.identify_row(event.y)

        if col == '#4':  # Vérification de la colonne Stock (colonne n°4)
            item = self.table.item(row)
            current_stock = item['values'][3]

            new_stock = self.create_stock_dialog(current_stock)

            if new_stock is not None:
                index = self.table.index(row)
                self.data[index] = (
                    item['values'][0],
                    item['values'][1],
                    item['values'][2],
                    new_stock,
                    item['values'][4]
                )

                for row in self.table.get_children():
                    self.table.delete(row)

                for data_row in self.data:
                    self.table.insert("", "end", values=data_row)

def create_stock_dialog(self, current_stock):
        stock_dialog = tk.Toplevel(self)
        stock_dialog.title("Modifier le stock")
        stock_dialog.geometry("300x100")

        new_stock = tk.StringVar(value=current_stock)
        entry = tk.Entry(stock_dialog, textvariable=new_stock)
        entry.pack(padx=20, pady=10)

        button_ok = tk.Button(stock_dialog, text="Valider", command=lambda: stock_dialog.destroy())
        button_ok.pack(pady=5)

        stock_dialog.transient(self)
        stock_dialog.grab_set()

        self.wait_window(stock_dialog)
        return new_stock.get() 

def sort_column(self, col, reverse):
        # Trier la colonne
        items = [(self.table.set(k, col), k) for k in self.table.get_children("")]
        items.sort(reverse=reverse)
 
        # Réorganiser les éléments dans le Treeview
        for index, (val, k) in enumerate(items):
            self.table.move(k, "", index)
 
        # Mettre à jour l'ordre de tri pour la colonne suivante
        self.table.heading(col, command=lambda: self.sort_column(col, not reverse))



################################################################################################
if __name__=="__main__":
    myApp = App()
    erp = ERP()
    myApp.mainloop()

