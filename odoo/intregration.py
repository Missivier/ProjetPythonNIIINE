import xmlrpc.client
from datetime import datetime, timedelta

class ERP:
    def __init__(self, db_name=None, username=None, password=None):
        self.odoo_ipaddr = "172.31.11.2"
        self.odoo_port = "8069"
        self.odoo_url = f'http://{self.odoo_ipaddr}:{self.odoo_port}'
        self.db_name =  db_name
        self.username = username
        self.password = password
        self.nom_article = []
        self.prix_article = []
        self.reference_interne = []
        self.stock_disponible = []
        self.common = xmlrpc.client.ServerProxy(f'{self.odoo_url}/xmlrpc/2/common')
        self.models = xmlrpc.client.ServerProxy(f'{self.odoo_url}/xmlrpc/2/object')
        self.uid = 0
        self.images_stock = []

    def obtenir_informations_produits(self):
        common = xmlrpc.client.ServerProxy(f'{self.odoo_url}/xmlrpc/2/common')
        uid = common.authenticate(self.db_name, self.username, self.password, {})

        if uid:
            models = xmlrpc.client.ServerProxy(f'{self.odoo_url}/xmlrpc/2/object')

            product_ids = models.execute_kw(self.db_name, uid, self.password, 'product.product', 'search', [[]], {})
            products = models.execute_kw(self.db_name, uid, self.password, 'product.product', 'read', [product_ids],
                                        {'fields': ['name', 'list_price', 'default_code', 'qty_available', 'image_1920']})

            for product in products:
                self.nom_article.append(product['name'])
                self.prix_article.append(product['list_price'])
                self.reference_interne.append(product['default_code'])
                self.stock_disponible.append(product['qty_available'])
                self.images_stock.append(product['image_1920'])

        else:
            print('Échec de la connexion à Odoo.')


    def modifier_stock_odoo(self, default_code, new_stock):
        if self.uid:
            product_id = self.models.execute_kw(
                self.db_name, self.uid, self.password,
                'product.product', 'search',
                [[['default_code', '=', default_code]]]
            )
            if product_id:
                quant_id = self.models.execute_kw(
                    self.db_name, self.uid, self.password,
                    'stock.quant', 'search',
                    [[['product_id', '=', product_id[0]]]]
                )
                if quant_id:
                    self.models.execute_kw(
                        self.db_name, self.uid, self.password,
                        'stock.quant', 'write',
                        [quant_id, {'quantity': new_stock}]
                    )
                    print(f"Stock mis à jour avec succès pour l'article avec le default_code '{default_code}'.")
                else:
                    print(f"Le produit avec le default_code '{default_code}' n'a pas de stock.")
            else:
                print(f"Le default_code '{default_code}' n'a pas été trouvé.")
        else:
            print('Échec de la connexion à Odoo.')

    def afficher_variables(self):
        if self.nom_article:
            print("Nom des articles :", self.nom_article[0])
        if self.prix_article:
            print("Prix des articles :", self.prix_article[0])
        if self.reference_interne:
            print("Référence interne :", self.reference_interne[0])
        if self.stock_disponible:
            print("Stock disponible :", self.stock_disponible[0])


    def main(self):
        self.connexion()
        self.obtenir_informations_produits()
        self.afficher_variables()
        self.modifier_stock_odoo()

    def run(self):
        self.main()

if __name__ == "__main__":
    erp_instance = ERP()
    erp_instance.run()