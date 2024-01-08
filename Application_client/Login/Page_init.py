import tkinter as tk
def page_init(self):
#Creation de la page
        self.title("Application CyberVest")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"{self.screen_width}x{self.screen_height}+0+0")

        background_frame = tk.Frame(self, bg="#DAD7D7")
        background_frame.place(relwidth=1, relheight=1)

        # Création d'un bouton pour quitter l'application
        bouton_quit = tk.Button(self, text="Quitter", fg="#296EDF", bg="#DAD7D7", font=("Arial", 20), command=self.destroy)
        bouton_quit.place(relx=1, rely=1, anchor='se')  # Positionne le bouton en bas à droite