import xmlrpc.client

def toto():
    print("toto")
    
odoo_ipaddr = "172.31.10.239"
odoo_port = "8069"
odoo_url = f'http://{odoo_ipaddr}:{odoo_port}'

db_name = 'db_cybervest'
username = 'gabin'
password = 'jslpdl'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(odoo_url))
uid = common.authenticate(db_name, username, password, {})



if uid: 
    print('Connexion réussie; Utilisateur:', uid)
else: 
    print('Echec de la connexion.')


user = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(odoo_url))


partner_ids = user.execute_kw(db_name, uid, password, 'res.partner', 'search', [[]], {})
partners = user.execute_kw(db_name, uid, password, 'res.partner', 'read', [partner_ids], {'fields': ['name']})


print(partners)

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

    print("Nombre d'article dans la base de données:", nombre_articles)

    # Exemple d'accès aux informations du premier article
    if len(nom_article) > 0:
        premier_nom_article = nom_article[0]
        premier_prix_article = prix_article[0]
        premiere_reference_interne = reference_interne[0]
        premier_stock_disponible = stock_disponible[0]

        print("Informations sur le premier article:")
        print("Nom de l'article:", premier_nom_article)
        print("Prix:", premier_prix_article)
        print("Référence interne:", premiere_reference_interne)
        print("Stock disponible:", premier_stock_disponible)

else:
    print('Échec de la connexion.')
