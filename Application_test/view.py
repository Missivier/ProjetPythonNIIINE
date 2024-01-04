# views.py

from tkinter import Frame, Label, Button

class BaseView(Frame):
    """Classe de base pour les vues."""
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

class HomeView(BaseView):
    """Vue pour la page d'accueil."""
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.label = Label(self, text="Bienvenue sur la page d'accueil !")
        self.label.pack(pady=10)
        self.button = Button(self, text="Aller à la fonctionnalité", command=self.show_feature_view)
        self.button.pack(pady=10)

    def show_feature_view(self):
        """Affiche la vue de la fonctionnalité."""
        self.pack_forget()  # Cache la vue actuelle
        FeatureView(self.master).pack(expand=True, fill='both')  # Affiche la vue de la fonctionnalité

class FeatureView(BaseView):
    """Vue pour une fonctionnalité spécifique."""
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.label = Label(self, text="Ceci est la fonctionnalité spécifique.")
        self.label.pack(pady=10)
        self.button = Button(self, text="Retour à la page d'accueil", command=self.show_home_view)
        self.button.pack(pady=10)

    def show_home_view(self):
        """Retourne à la page d'accueil."""
        self.pack_forget()  # Cache la vue actuelle
        HomeView(self.master).pack(expand=True, fill='both')  # Affiche la page d'accueil

# Ajoute d'autres classes de vue au besoin
