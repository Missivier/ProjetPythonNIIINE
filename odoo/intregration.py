import xmlrpc.client

class ERP: 
    def __init__(self, callback_function = None):
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

         # Fonction de rappel pour la mise à jour de l'interface utilisateur (Tkinter)
        self.callback_function = callback_function

    def connect_odoo_signals(self):
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.odoo_url))
        uid = common.authenticate(self.db_name, self.username, self.password, {})

        if uid:
            models = xmlrpc.client.ServerProxy(f'{self.odoo_url}/xmlrpc/2/object')

            quant_ids = models.execute_kw(self.db_name, uid, self.password, 'stock.quant', 'search', [[]], {})
            quants = models.execute_kw(self.db_name, uid, self.password, 'stock.quant', 'read', [quant_ids],
                                        {'fields': ['product_id', 'quantity']})

            for quant in quants:
                product_id = quant['product_id'][0] if quant['product_id'] else False
                product = models.execute_kw(self.db_name, uid, self.password, 'product.product', 'read', [product_id],
                                            {'fields': ['default_code']})
                default_code = product[0]['default_code'] if product else ""
                self.nom_article.append(default_code)
                self.stock_disponible.append(quant['quantity'])

        else:
            print('Échec de la connexion à Odoo.')

    def on_odoo_record_write(self, model, record_id):
        # Cette fonction sera appelée lorsqu'un enregistrement est modifié dans Odoo
        # Mettez à jour les informations sur les produits
        self.obtenir_informations_produits()
        self.update_table()
        # Appeler la fonction de rappel pour mettre à jour l'interface utilisateur (Tkinter)
        if self.callback_function:
            self.callback_function()

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

    def afficher_interface_modification_stock(self):
        root = tk.Tk()
        root.title("Modification du Stock")

        label_default_code = tk.Label(root, text="Default Code de l'article à modifier :")
        label_default_code.pack()

        default_code_entry = tk.Entry(root)
        default_code_entry.pack()

        label_new_stock = tk.Label(root, text="Nouveau stock :")
        label_new_stock.pack()

        new_stock_entry = tk.Entry(root)
        new_stock_entry.pack()

        def modifier():
            default_code = default_code_entry.get()
            new_stock = new_stock_entry.get()

            try:
                new_stock = int(new_stock)
                self.modifier_stock_odoo(default_code, new_stock)
            except ValueError:
                print("Veuillez entrer une valeur numérique pour le nouveau stock.")

        button = tk.Button(root, text="Modifier", command=modifier)
        button.pack()

        root.mainloop()


def main():
    erp_instance = ERP()
    erp_instance.obtenir_informations_produits()
    erp_instance.afficher_interface_modification_stock()


if __name__ == "__main__":
    erp_instance = ERP()
    erp_instance.run()
