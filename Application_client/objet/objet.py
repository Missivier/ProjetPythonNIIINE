class User: 
    def __init__(self, id, username, password, role) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.role = role
        

    def login(self, username, password):
        self.username = username
        self.password = password
        




class Page:
    def __init__(self, current_user ):
        self.current_user = current_user

    def titre(self, nomdepage):
        self.nomdepage = nomdepage

    def affichagetableau(self, tableau):
        self.tableau = tableau

    

class Article:
    def __init__(self, reference, nom, prix, stock, new_stock):
        self.reference = reference
        self.nom = nom 
        self.prix = prix
        self.stock = stock 
        self.new_stock = new_stock


    def tableaulogistique():

        
