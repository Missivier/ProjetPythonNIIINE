import xmlrpc.client

def modifier_stock_produit(odoo_url, db_name, username, password, product_id, new_stock):
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(odoo_url))
    uid = common.authenticate(db_name, username, password, {})

    if uid:
        print('Connexion réussie; Utilisateur:', uid)
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(odoo_url))

        # Mise à jour du stock du produit
        product_data = {
            'qty_available': new_stock,
        }
        models.execute_kw(db_name, uid, password, 'product.product', 'write', [[product_id], product_data])

        print("Quantité en stock mise à jour avec succès pour le produit ID:", product_id)
    else:
        print('Échec de la connexion.')

# Exemple d'utilisation pour modifier la quantité en stock d'un produit spécifique
if __name__ == "__main__":
    odoo_ipaddr = "172.31.10.239"
    odoo_port = "8069"
    odoo_url = f'http://{odoo_ipaddr}:{odoo_port}'
    db_name = 'db_cybervest'
    username = 'enzo'
    password = 'jslpdl'
    
    # ID du produit à mettre à jour
    product_id_to_update = 1  # Remplacez ceci par l'ID réel du produit que vous souhaitez mettre à jour
    new_stock_quantity = 50  # Nouvelle quantité en stock à définir
    
    # Appel de la fonction pour modifier le stock du produit spécifié
    modifier_stock_produit(odoo_url, db_name, username, password, product_id_to_update, new_stock_quantity)
