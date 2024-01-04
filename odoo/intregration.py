
import xmlrpc.client

class ERP: 
    def __init__(self):
        odoo_ipaddr = "172.31.10.239"
        odoo_port = "8069"
        odoo_url = f'http://{odoo_ipaddr}:{odoo_port}'
        db_name = 'db_cybervest'
        username = 'enzo'
        password = 'jslpdl'



    def obtenir_informations_produits(odoo_url, db_name, username, password):

        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(odoo_url))
        uid = common.authenticate(db_name, username, password, {})

        if uid:
            print('Connexion réussie; Utilisateur:', uid)
            models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(odoo_url))

            # Récupération des identifiants des produits
            product_ids = models.execute_kw(db_name, uid, password, 'product.product', 'search', [[]], {})
            products = models.execute_kw(db_name, uid, password, 'product.product', 'read', [product_ids],
                                        {'fields': ['name', 'list_price', 'default_code', 'qty_available']})

            # Création de listes pour stocker les informations de chaque article
            nom_article = []
            prix_article = []
            reference_interne = []
            stock_disponible = []

            # Stockage des informations dans les listes
            for product in products:
                nom = product['name']
                prix = product['list_price']
                ref_interne = product['default_code']
                stock = product['qty_available']

                nom_article.append(nom)
                prix_article.append(prix)
                reference_interne.append(ref_interne)
                stock_disponible.append(stock)

            nombre_articles = len(nom_article)

            return nom_article, prix_article, reference_interne, stock_disponible, nombre_articles

        else:
            print('Échec de la connexion.')
            return [], [], [], [], 0
