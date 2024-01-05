import xmlrpc.client
import tkinter as tk

class ERP:
    def __init__(self):
        self.odoo_ipaddr = "172.31.10.239"
        self.odoo_port = "8069"
        self.odoo_url = f'http://{self.odoo_ipaddr}:{self.odoo_port}'
        self.db_name = 'db_cybervest'
        self.username = 'enzo'
        self.password = 'jslpdl'
        self.nom_article = []
        self.stock_disponible = []

    def obtenir_informations_produits(self):
        common = xmlrpc.client.ServerProxy(f'{self.odoo_url}/xmlrpc/2/common')
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
            print('Échec de la connexion.')

    def modifier_stock_odoo(self, default_code, new_stock):
        common = xmlrpc.client.ServerProxy(f'{self.odoo_url}/xmlrpc/2/common')
        uid = common.authenticate(self.db_name, self.username, self.password, {})

        if uid:
            models = xmlrpc.client.ServerProxy(f'{self.odoo_url}/xmlrpc/2/object')

            product_id = models.execute_kw(
                self.db_name, uid, self.password,
                'product.product', 'search',
                [[['default_code', '=', default_code]]]
            )
            if product_id:
                quant_id = models.execute_kw(
                    self.db_name, uid, self.password,
                    'stock.quant', 'search',
                    [[['product_id', '=', product_id[0]]]]
                )
                if quant_id:
                    models.execute_kw(
                        self.db_name, uid, self.password,
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
    main()
