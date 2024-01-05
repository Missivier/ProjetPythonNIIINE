import xmlrpc.client

class ERP: 
    def __init__(self):
        self.odoo_ipaddr = "172.31.10.239"
        self.odoo_port = "8069"
        self.odoo_url = f'http://{self.odoo_ipaddr}:{self.odoo_port}'
        self.db_name = 'db_cybervest'
        self.username = 'enzo'
        self.password = 'jslpdl'
        self.nom_article = []
        self.prix_article = []
        self.reference_interne = []
        self.stock_disponible = []

    def toto(self): 
        print("toto")

    def obtenir_informations_produits(self):
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.odoo_url))
        uid = common.authenticate(self.db_name, self.username, self.password, {})

        if uid:
            models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.odoo_url))

            # Récupération des identifiants des produits
            product_ids = models.execute_kw(self.db_name, uid, self.password, 'product.product', 'search', [[]], {})
            products = models.execute_kw(self.db_name, uid, self.password, 'product.product', 'read', [product_ids],
                                        {'fields': ['name', 'list_price', 'default_code', 'qty_available']})

            # Stockage des informations dans les listes distinctes
            for product in products:
                self.nom_article.append(product['name'])
                self.prix_article.append(product['list_price'])
                self.reference_interne.append(product['default_code'])
                self.stock_disponible.append(product['qty_available'])

        else:
            print('Échec de la connexion.')

    def ecrire_informations_produits(self):
        if len(self.nom_article) > 0:  # Vérifier si des informations sont disponibles
            # Utilisation des listes stockées dans la classe ERP
            print("Nom de l'article:", self.nom_article[0])
            print("Prix de l'article:", self.prix_article[0])
            print("Référence Interne:", self.reference_interne[0])
            print("Stock Disponible:", self.stock_disponible[0])
        else:
            print("Aucune information sur les produits disponible.")


# Utilisation de la classe ERP pour obtenir et afficher les informations sur les produits
def main():
    erp_instance = ERP()
    erp_instance.obtenir_informations_produits()
    erp_instance.ecrire_informations_produits()


if __name__ == "__main__":
    main()
