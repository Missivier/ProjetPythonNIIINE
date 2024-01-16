import sys
from tkinter import Tk
sys.path.insert(0, 'odoo')
from intregration import ERP
from view import HomeView

class Appli:
    def __init__(self, root):
        self.root = root
        self.root.title("Mon Application Tkinter")
        self.root.screen_width = self.root.winfo_screenwidth()
        self.root.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.root.screen_width}x{self.root.screen_height}+0+0")
          
        HomeView(self.root).grid(row=0, column=0, padx=10, pady=10, columnspan=5)

    def toggle_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', not self.root.attributes('-fullscreen'))

if __name__ == "__main__":
<<<<<<< HEAD
    erp = ERP(db_name='db_cybervest') #username='alexandre', password='jslpdl') 
=======
>>>>>>> 4486606a39262938d3bdf768f4f4f0b2b6f465a7
    root = Tk()
    erp_instance = ERP(db_name='db_cybervest') #username='enzo', password='jslpdl')
    erp_instance.connexion(username='enzo', password='jslpdl')
    app = Appli(root)
    root.mainloop()