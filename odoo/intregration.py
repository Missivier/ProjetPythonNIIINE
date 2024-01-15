import xmlrpc.client
import base64
from datetime import datetime, timedelta
 
class ERP:
    def __init__(self, db_name=None, username=None, password=None):
        self.odoo_ipaddr = "172.31.11.2"
        self.odoo_port = "8069"
        self.odoo_url = f'http://{self.odoo_ipaddr}:{self.odoo_port}'
        self.db_name = db_name
        self.username = username
        self.password = password
        self.nom_article = []
        self.prix_article = []
        self.reference_interne = []
        self.stock_disponible = []
        self.common = xmlrpc.client.ServerProxy(f'{self.odoo_url}/xmlrpc/2/common', allow_none=True)
        self.models = xmlrpc.client.ServerProxy(f'{self.odoo_url}/xmlrpc/2/object', allow_none=True)
        self.uid = 0
        self.images_stock = []
        self.ordres_fabrication = []
        self.dates_ordres_fabrication = []
        self.quantite_a_produire = []
        self.qty_producing = []
 
    def connexion(self):
        self.uid = self.common.authenticate(self.db_name, self.username, self.password, {})
        if self.uid:
            print('Connexion réussie. UID utilisateur:', self.uid)
        else:
            print('Échec de la connexion.')
        return self.uid
 
    def obtenir_informations_produits(self):
        if self.uid:
            product_ids = self.models.execute_kw(
                self.db_name, self.uid, self.password,
                'product.product', 'search', [[]], {}
            )
            products = self.models.execute_kw(
                self.db_name, self.uid, self.password,
                'product.product', 'read', [product_ids],
                {'fields': ['name', 'list_price', 'default_code', 'qty_available', 'image_1920']}
            )
 
            for product in products:
                self.nom_article.append(product['name'])
                self.prix_article.append(product['list_price'])
                self.reference_interne.append(product['default_code'])
                self.stock_disponible.append(product['qty_available'])
                self.images_stock.append(product['image_1920'])
        else:
            print('Échec de la connexion à Odoo.')
 
    def obtenir_informations_ordres_fabrication(self):
        ordres_fabrication = []
        dates_ordres_fabrication = []
        quantite_a_produire = []
        qty_producing = []
 
        if self.uid:
            mo_ids = self.models.execute_kw(
                self.db_name, self.uid, self.password,
                'mrp.production', 'search',
                [[['state', 'not in', ['cancel', 'done']]]]
            )
            mos = self.models.execute_kw(
                self.db_name, self.uid, self.password,
                'mrp.production', 'read', [mo_ids],
                {'fields': ['name', 'date_planned_start', 'product_qty', 'qty_producing']}
            )
 
            for mo in mos:
                ordres_fabrication.append(mo['name'])
                dates_ordres_fabrication.append(mo['date_planned_start'])
                quantite_a_produire.append(mo['product_qty'])
                qty_producing.append(mo['qty_producing'])
        else:
            print('Échec de la connexion à Odoo.')
 
        return ordres_fabrication, dates_ordres_fabrication, quantite_a_produire, qty_producing
    
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
 
    def modifier_quantite_en_cours_production(self, ordre_fabrication, new_qty_producing):
        if self.uid:
            mo_id = self.models.execute_kw(
                self.db_name, self.uid, self.password,
                'mrp.production', 'search',
                [[['name', '=', ordre_fabrication]]]
            )
            if mo_id:
                self.models.execute_kw(
                    self.db_name, self.uid, self.password,
                    'mrp.production', 'write',
                    [mo_id, {'qty_producing': new_qty_producing}]
                )
                print(f"Quantité en cours de production mise à jour avec succès pour l'ordre de fabrication '{ordre_fabrication}'.")
            else:
                print(f"L'ordre de fabrication '{ordre_fabrication}' n'a pas été trouvé.")
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
 
    def run(self):
        self.connexion()
        self.obtenir_informations_produits()
        self.afficher_variables()
 
        # Obtention des informations des ordres de fabrication
        ordres, dates, quantites, qty_producing = self.obtenir_informations_ordres_fabrication()
 
        # Utilisez ces informations comme nécessaire
        print("Ordres de fabrication :", ordres)
        print("Dates des ordres de fabrication :", dates)
        print("Quantités à produire :", quantites)
        print("Quantités en cours de production :", qty_producing)
 
if __name__ == "__main__":
    erp_instance = ERP(db_name='db_cybervest', username='enzo', password='jslpdl')
    erp_instance.run()