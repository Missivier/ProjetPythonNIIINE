from info_produits import obtenir_informations_produits

odoo_ipaddr = "172.31.10.239"
odoo_port = "8069"
odoo_url = f'http://{odoo_ipaddr}:{odoo_port}'
db_name = 'db_cybervest'
username = 'enzo'
password = 'jslpdl'

# Appel de la fonction pour obtenir les informations des produits
nom_article, prix_article, reference_interne, stock_disponible, nombre_articles = obtenir_informations_produits(
    odoo_url, db_name, username, password
)

