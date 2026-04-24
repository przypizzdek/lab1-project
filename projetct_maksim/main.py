import tkinter as tk
from models import Motory,Ciezarowki,Zwykle_samochody
class interfejs():


    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Katalog samochodów")

        self.label_typ = tk.Label(text="Typ")
        self.label_typ.place(x=1400, y=50)
        self.entry_typ = tk.Entry()
        self.entry_typ.place(x=1350, y=80)

        self.label_cena = tk.Label(text="Cena")
        self.label_cena.place(x=1400, y=110)
        self.entry_cena_do = tk.Entry()
        self.entry_cena_do.place(x=1350, y=140)
        self.entry_cena_od = tk.Entry()
        self.entry_cena_od.place(x=1200, y=140)

        self.label_od = tk.Label(text="od")
        self.label_od.place(x=1180, y=140)
        self.label_do = tk.Label(text="do")
        self.label_do.place(x=1327, y=140)

        self.label_brend = tk.Label(text="Brend")
        self.label_brend.place(x=1400, y=170)
        self.entry_brend = tk.Entry()
        self.entry_brend.place(x=1350, y=200)

        self.nacisk_znalesc = tk.Button(text="Znalesc", command=self.button_znalesc)
        self.nacisk_znalesc.place(x=1400, y=230)

        self.nacisk_pokazacWS = tk.Button(text="Pokazać wszystkie samochody")
        self.nacisk_pokazacWS.place(x=1350, y=300)

        self.window.mainloop()

    def button_znalesc(self):
        min_cena = self.entry_cena_od.get()
        max_cena = self.entry_cena_do.get()
        brend = self.entry_brend.get()

        typ = self.entry_typ.get()

        lista_klasow = {
            "Motory":Motory,
            "Ciezarowki":Ciezarowki,
            "Zwykle_samochody":Zwykle_samochody}

        if typ in lista_klasow:
            Klas = lista_klasow[typ]
            lista = Klas.znalesc(min_cena, max_cena, brend, typ)


        X=700
        Y=50
        for i in lista:
            label_typw = tk.Label(text=i["typ"])
            label_typw.place(x=X, y=Y)
            label_cenaw = tk.Label(text=i["cena"])
            label_cenaw.place(x=X, y=Y+10)
            label_typw = tk.Label(text=i["brend"])
            label_typw.place(x=X, y=Y+20)
            X+=50







interfejs()