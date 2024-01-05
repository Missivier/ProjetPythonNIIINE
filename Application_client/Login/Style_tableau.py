import tkinter as tk
import tkinter.ttk as ttk
def style_tableau(self):    
# Appliquer le quadrillage
    style = ttk.Style()
    style.configure("mystyle.Treeview", rowheight=30)
    style.map("mystyle.Treeview", background=[("selected", "#bce0ff")])
    style.configure("mystyle.Treeview", background="white", fieldbackground="white", foreground="black", font=('Arial', 10), borderwidth=0)
    self.tableau.configure(style="mystyle.Treeview")

    # Appliquer le style aux colonnes
    for col in ("Colonne 1", "Colonne 2", "Colonne 3", "Colonne 4", "Colonne 5", "Colonne 6", "Validation"):
        self.tableau.column(col, width=250, anchor=tk.CENTER)

    # Configuration des lignes de quadrillage
    self.tableau.tag_configure('oddrow', background='white')
    self.tableau.tag_configure('evenrow', background='#f0f0f0')

    # Appliquer le quadrillage aux lignes
    row_count = 0
    for child in self.tableau.get_children():
        if row_count % 2 == 0:
            self.tableau.item(child, tags=('evenrow',))
        else:
            self.tableau.item(child, tags=('oddrow',))
        row_count += 1