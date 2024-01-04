import xmlrpc.client

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
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(odoo_url))

    # Récupération des identifiants des produits
    product_ids = models.execute_kw(db_name, uid, password, 'product.product', 'search', [[]], {})
    products = models.execute_kw(db_name, uid, password, 'product.product', 'read', [product_ids],
                                  {'fields': ['name', 'list_price', 'default_code', 'qty_available']})

    # Création de listes pour stocker les informations de chaque article
    noms_articles = []
    prix_articles = []
    references_internes = []
    stocks_disponibles = []

    # Stockage des informations dans les listes
    for product in products:
        nom_article = product['name']
        prix = product['list_price']
        reference_interne = product['default_code']
        stock_disponible = product['qty_available']

        noms_articles.append(nom_article)
        prix_articles.append(prix)
        references_internes.append(reference_interne)
        stocks_disponibles.append(stock_disponible)

    # Exemple d'accès aux informations du premier article
    if len(noms_articles) > 0:
        premier_nom_article = noms_articles[0]
        premier_prix_article = prix_articles[0]
        premiere_reference_interne = references_internes[0]
        premier_stock_disponible = stocks_disponibles[0]

        print("Informations sur le premier article:")
        print("Nom de l'article:", noms_articles[0])
        print("Prix:", premier_prix_article)
        print("Référence interne:", premiere_reference_interne)
        print("Stock disponible:", premier_stock_disponible)

else:
    print('Échec de la connexion.')
