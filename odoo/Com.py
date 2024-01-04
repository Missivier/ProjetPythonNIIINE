import xmlrpc.client

# Informations de connexion Odoo
url = 'http://172.31.10.239:8069'  # Remplacez par l'adresse de votre Odoo
db = 'db_cybervest'  # Remplacez par le nom de votre base de données Odoo
username = 'enzo'
password = 'jslpdl'

common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})

if uid:
    print("Réussi")
else:
    print("Échec de l'authentification")