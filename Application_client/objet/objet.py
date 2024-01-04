import xmlrpc.client

odoo_ipaddr = "172.31.10.239"
odoo_port = "8069"
odoo_url = f'http://{odoo_ipaddr}:{odoo_port}'

db_name = 'db_cybervest'
username = 'gabin'
password = 'jslpdl'
common_proxy = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(odoo_url))


class User: 
    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role
        

    def login(self, username, password):
        self.username = username
        self.password = password

    try: 
        user_odoo = common_proxy.authenticate(db_name,username, password, {})
        user_info = common_proxy.execute_kw(db_name, user_odoo, password,
                                                     'res.users', 'read', [user_odoo], {'fields': ['name', 'login', 'groups_id']})
        if user_odoo:
            print(f"Utilisateur {username} authentifié avec succès (ID: {user_odoo})")
            print(user_info) 
        else:
            print("Échec de l'authentification. Vérifiez les informations d'identification.")
                

    except xmlrpc.client.Fault as e:
        print(f"Erreur XML-RPC: {e.faultCode} - {e.faultString}")






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


   
        
