import xmlrpc.client


odoo_ipaddr = "172.31.10.239"
odoo_port = "8069"
odoo_url = f'http://{odoo_ipaddr}:{odoo_port}'

db_name = 'db_cybervest'

username = 'gabin'
password = 'jslpdl'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(odoo_url))
version = common.version()

uid = common.authenticate(db_name, username, password, {})


#---------------------------------------------------------------------------------------




#---------------------------------------------------------------------------------------


print("Connexion ODOO")
print(f"@URL={odoo_url}")

print(f"Odoo version = {version}")


if uid: 
    print('Connexion réussie; Utilisateur:', uid)
else: 
    print('Echec de la connexion.')


models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(odoo_url))


partner_ids = models.execute_kw(db_name, uid, password, 'res.partner', 'search', [[]], {})
partners = models.execute_kw(db_name, uid, password, 'res.partner', 'read', [partner_ids], {'fields': ['name']})


print(partners) 

