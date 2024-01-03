def page_of(root):

    def deconnexion():
        title_frame.place_forget()
        border.place_forget()
        tableau.place_forget()
        page_login(root)

    # Création du tableau
    tableau = ttk.Treeview(root, columns=("Colonne 1", "Colonne 2", "Colonne 3", "Colonne 4", "Colonne 5", "Colonne 6", "Validation"), show="headings")

    # Configurer les en-têtes de colonnes
    tableau.heading("Colonne 1", text="N° OF")
    tableau.heading("Colonne 2", text="Référence")
    tableau.heading("Colonne 3", text="Quantité")
    tableau.heading("Colonne 4", text="Date")
    tableau.heading("Colonne 5", text="Heure")
    tableau.heading("Colonne 6", text="Status")
    tableau.heading("Validation", text="Validation")

    # Placer le tableau dans la fenêtre principale
    tableau.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.7)

    # Fonction pour valider chaque ligne
    def valider_ligne(row_id):
        # Faites quelque chose pour valider la ligne ici
        print(f"Ligne validée: {row_id}")

    # Insérer des données dans le tableau
    for i in range(10):  # Par exemple, ajout de 10 lignes de données fictives
        tableau.insert("", "end", values=(f"Ligne {i+1} - Colonne 1", f"Ligne {i+1} - Colonne 2", f"Ligne {i+1} - Colonne 3", f"Ligne {i+1} - Colonne 4", f"Ligne {i+1} - Colonne 5", f"Ligne {i+1} - Colonne 6", ""))
        # Ajouter un bouton de validation dans la colonne "Validation" pour chaque ligne
        tableau.insert("", "end", values=("", ""), tags=("button",)) # Ajout d'un tag pour identifier les boutons

    # Associer une fonction à exécuter lorsqu'un bouton de validation est cliqué
    tableau.tag_configure("button", foreground="blue", background="white", font=("Arial", 10, "underline"))
    tableau.bind("<Button-1>", lambda event: valider_ligne(tableau.identify_row(event.y)))

    # Ajout d'une barre de titre en haut de la page
    border = tk.Frame(root, bg="black")
    border.place(relx=0, rely=0.11, relwidth=1, relheight=0.01)

    # Ajout d'une barre de titre en haut de la page
    title_frame = tk.Frame(root, bg="#DAD7D7")
    title_frame.place(relx=0.1, rely=0, relwidth=1, relheight=0.1)

    # Positionnement horizontal du label au centre
    title_label = tk.Label(title_frame, text="Liste des OF", font=("Arial", 16), bg="#DAD7D7")
    title_label.place(relx=0.4, rely=0.5, anchor="center")  # Centrer horizontalement

    # Ajout d'un bouton à droite du cadre
    button_right = tk.Button(title_frame, text="Déconnexion", command=deconnexion)
    button_right.place(relx=0.85, rely=0.5, anchor="center")  # Centrer horizontalement
