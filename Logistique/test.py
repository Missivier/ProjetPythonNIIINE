from PIL import Image, ImageTk

# ...

def show_image(self, event):
    # Récupération de la ligne sélectionnée
    item = self.tree.selection()[0]

    # Récupération du nom de l'article associé à la ligne sélectionnée
    article_name = self.tree.item(item, "values")[1]

    # Récupération du nom de l'image associée à l'article
    image_name = self.image_dict.get(article_name, "")

    if image_name:
        # Affichage de l'image dans un Label à l'intérieur de la même fenêtre
        image_path = f"/home/user/Documents/ProjetPythonNIIINE/photos/{image_name}"
        img = Image.open(image_path)
        img = ImageTk.PhotoImage(img)

        # Supprimer l'ancien Label s'il existe
        for widget in self.root.grid_slaves():
            if isinstance(widget, tk.Label):
                widget.destroy()

        # Création d'un widget Label pour afficher l'image à droite
        image_label = tk.Label(self.root, image=img)
        image_label.photo = img
        image_label.grid(row=0, column=1, padx=10, pady=10, rowspan=2, sticky="e")  # Ajustez la position et la colonne selon vos besoins
