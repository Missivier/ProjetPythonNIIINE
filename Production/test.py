import tkinter as tk
from pagedefaut import page_defaut

def choix_menu():
    # Appel de la fonction page_defaut() pour créer la fenêtre principale
    root = page_defaut()
    
    # Fonction pour fermer la fenêtre principale
    def fermer_fenetre():
        root.destroy()
    
    # Fonction pour effectuer une action pour le bouton "Afficher OF"
    def action_afficher_OF():
        # Exemple d'action : affichage d'un message dans la console
        print("Action pour Afficher OF exécutée !")

    # Création des boutons avec une taille de police plus grande
    button1 = tk.Button(root, text="Afficher OF", width=15, height=3, font=("Arial", 14), command=action_afficher_OF)
    button2 = tk.Button(root, text="Quitter", width=15, height=3, font=("Arial", 14), command=fermer_fenetre)
    
    # Placement des boutons au milieu de la fenêtre
    button1.place(relx=0.5, rely=0.4, anchor="center")
    button2.place(relx=0.5, rely=0.6, anchor="center")

    # Démarrage de la boucle principale
    root.mainloop()

# Appel de la fonction pour ajouter les boutons à la page par défaut
choix_menu()
