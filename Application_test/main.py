# main.py
import sys
sys.path.insert(0,'odoo')
from intregration import ERP
from tkinter import Tk
from view import HomeView


class Appli:
    def __init__(self, root):
        self.root = root
        self.root.title("Mon Application Tkinter")

if __name__ == "__main__":
    erp = ERP()
    erp.toto()
    root = Tk()
    app = Appli(root)
    root.mainloop()
