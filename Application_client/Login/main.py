import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Style_tableau import style_tableau
#---------------------------------------------------------------------------------------------------
#===================================================================================================
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Application CyberVest")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"{self.screen_width}x{self.screen_height}+0+0")

        background_frame = tk.Frame(self, bg="#DAD7D7")
        background_frame.place(relwidth=1, relheight=1)

        # Création d'un bouton pour quitter l'application
        bouton_quit = tk.Button(self, text="Quitter", fg="#296EDF", bg="#DAD7D7", font=("Arial", 20), command=self.destroy)
        bouton_quit.place(relx=1, rely=1, anchor='se')  # Positionne le bouton en bas à droite
#---------------------------------------------------------------------------------------------------
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
#---------------------------------------------------------------------------------------------------
        # Page production
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


#---------------------------------------------------------------------------------------------------
        # Bouton déconnection
        self.button_deconnexion = tk.Button(self, text="Déconnexion", command=self.hide_prod_page)


#===================================================================================================
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "1" and password == "1":
            self.hide_login_page()
            self.show_prod_page()
            self.show_button_deconnexion()
        else:
            messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect")

    def show_page_login(self):
        self.entry_password.delete(0, tk.END)
        self.entry_username.delete(0, tk.END)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

    def show_prod_page(self):
        self.page_prod_frame.place(relx=0, rely=0, relwidth=1, relheight=0.9)
    
    def show_button_deconnexion(self):
        self.button_deconnexion.place(relx=0.92, rely=0.03)

    def hide_button_deconnexion(self):
        self.button_deconnexion.place_forget()

    def hide_login_page(self):
        self.login_frame.place_forget()

    def hide_prod_page(self):
        self.page_prod_frame.place_forget()
        self.hide_button_deconnexion()
        self.show_page_login()

################################################################################################
if __name__=="__main__":
    myApp = App()
    myApp.mainloop()

