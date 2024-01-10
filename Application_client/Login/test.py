import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tableau avec Image")
        self.geometry("800x400")

        self.left_frame = tk.Frame(self)
        self.left_frame.pack(side="left", padx=10, pady=10)

        self.right_frame = tk.Frame(self)
        self.right_frame.pack(side="right", padx=10, pady=10)

        self.data = [
            ("123456", "Veste bouée", "249.90", "25", "veste_bouee.png"),
            ("123457", "Veste parachute", "544.90", "30", "veste_parachute.png"),
            ("123458", "Veste chauffante", "119.90", "20", "veste_chauffante.png"),
            ("123459", "Veste réfrigérée", "129.90", "20", "veste_refrigeree.png"),
        ]

        self.table = ttk.Treeview(self.left_frame, columns=("Code", "Nom", "Prix", "Stock"), show="headings")
        self.table.heading("Code", text="Code")
        self.table.heading("Nom", text="Nom")
        self.table.heading("Prix", text="Prix")
        self.table.heading("Stock", text="Stock")
        self.table.bind("<ButtonRelease-1>", self.show_image)
        self.table.bind("<Double-ButtonRelease-1>", self.edit_stock)

        for item in self.data:
            self.table.insert("", "end", values=item)

        self.table.pack()

        self.image_label = tk.Label(self.right_frame)
        self.image_label.pack()

    def show_image(self, event):
        selection = self.table.selection()
        if selection:
            item = self.table.item(selection[0])
            image_name = item['values'][4]
            try:
                image_path = f"/home/user/Documents/ProjetPythonNIIINE/Application_client/Image/{image_name}"  # Modifier le chemin vers votre dossier
                img = tk.PhotoImage(file=image_path)
                self.image_label.config(image=img)
                self.image_label.image = img
            except tk.TclError:
                # Gérer une éventuelle erreur si le chemin est incorrect ou si le fichier image est corrompu
                print("Erreur lors du chargement de l'image")

    def edit_stock(self, event):
        col = self.table.identify_column(event.x)
        row = self.table.identify_row(event.y)

        if col == '#4':  # Vérification de la colonne Stock (colonne n°4)
            item = self.table.item(row)
            current_stock = item['values'][3]

            new_stock = self.create_stock_dialog(current_stock)

            if new_stock is not None:
                index = self.table.index(row)
                self.data[index] = (
                    item['values'][0],
                    item['values'][1],
                    item['values'][2],
                    new_stock,
                    item['values'][4]
                )

                for row in self.table.get_children():
                    self.table.delete(row)

                for data_row in self.data:
                    self.table.insert("", "end", values=data_row)

    def create_stock_dialog(self, current_stock):
        stock_dialog = tk.Toplevel(self)
        stock_dialog.title("Modifier le stock")
        stock_dialog.geometry("300x100")

        new_stock = tk.StringVar(value=current_stock)
        entry = tk.Entry(stock_dialog, textvariable=new_stock)
        entry.pack(padx=20, pady=10)

        button_ok = tk.Button(stock_dialog, text="Valider", command=lambda: stock_dialog.destroy())
        button_ok.pack(pady=5)

        stock_dialog.transient(self)
        stock_dialog.grab_set()

        self.wait_window(stock_dialog)
        return new_stock.get()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
