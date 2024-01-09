        # Page admin
import tkinter as tk

def page_admin(self):
        #Création de la page
        self.page_admin_frame = tk.Frame(self,bg="#DAD7D7")
        #Creation bouton pour aller page prod
        self.Button_prod = tk.Button(self.page_admin_frame, text="Production",fg="black", bg="#DAD7D7", font=("Arial", 20), command=self.show_prod_page_admin)
        self.Button_prod.place(relx=0.3, rely=0.5, anchor="center")
        #Creation bouton pour aller page logistique
        self.Button_logis = tk.Button(self.page_admin_frame, text="Logistique",fg="black", bg="#DAD7D7", font=("Arial", 20), command=self.show_logis_page_admin)
        self.Button_logis.place(relx=0.5, rely=0.5, anchor="center")
        #Creation bouton pour aller page commerce
        self.Button_commerce = tk.Button(self.page_admin_frame, text="Commerce",fg="black", bg="#DAD7D7", font=("Arial", 20),command=self.show_commerce_page_admin)
        self.Button_commerce.place(relx=0.7, rely=0.5, anchor="center")
#------------------------------------------------------------------------