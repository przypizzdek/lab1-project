import tkinter as tk
from models import Motory,Zwykle_samochody, Ciezarowki
class interfejs():


    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Katalog samochodów")

        X = 100
        Y = 300
        self.label_typ = tk.Label(text="Typ")
        self.label_typ.place(x=X, y=Y)
        self.entry_typ = tk.Entry()
        self.entry_typ.place(x=X-50, y=Y+30)

        self.label_cena = tk.Label(text="Cena")
        self.label_cena.place(x=X, y=Y+60)
        self.entry_cena_do = tk.Entry()
        self.entry_cena_do.place(x=X-50, y=Y+120)
        self.entry_cena_od = tk.Entry()
        self.entry_cena_od.place(x=X-50, y=Y+90)

        self.label_od = tk.Label(text="od")
        self.label_od.place(x=X-80, y=Y+90)
        self.label_do = tk.Label(text="do")
        self.label_do.place(x=X-80, y=Y+120)

        self.label_brend = tk.Label(text="Brend")
        self.label_brend.place(x=X, y=Y+150)
        self.entry_brend = tk.Entry()
        self.entry_brend.place(x=X-50, y=Y+180)

        self.nacisk_znalesc = tk.Button(text="Znalesc", command=self.button_znalesc)
        self.nacisk_znalesc.place(x=X-10, y=Y+210)

        self.nacisk_pokazacWS = tk.Button(text="Pokazać wszystkie samochody")
        self.nacisk_pokazacWS.place(x=X-50, y=Y+280)

        self.label_Katalogi = tk.Label(text="Katalogi")
        self.label_Katalogi.place(x=X-10, y=Y - 200)

        self.bMotory = tk.Button(text="Motory")
        self.bMotory.place(x=X-60, y=Y - 160)
        self.bCiezarowki = tk.Button(text="Ciezarowki")
        self.bCiezarowki.place(x=X+20, y=Y - 160)
        self.bZwykle_samochody = tk.Button(text="Zwykle_samochody")
        self.bZwykle_samochody.place(x=X - 60, y=Y - 120)

        self.window.mainloop()

    def button_znalesc(self):
        min_cena = self.entry_cena_od.get()
        max_cena = self.entry_cena_do.get()
        brend = self.entry_brend.get()

        typ = self.entry_typ.get()

        lista_klasow = {
            "Motory": Motory,
            "Ciezarowki": Ciezarowki,
            "Zwykle_samochody": Zwykle_samochody}

        result_lista = []

        if typ in lista_klasow:
            Klas = lista_klasow[typ]
            result_lista = Klas.znalesc(min_cena, max_cena, brend, typ)

        X = 700
        Y = 50
        w = 0
        for i in result_lista:
            label_typw = tk.Label(text=i["typ"])
            label_typw.place(x=X, y=Y)
            label_cenaw = tk.Label(text=i["cena"])
            label_cenaw.place(x=X, y=Y + 20)
            label_typw = tk.Label(text=i["brend"])
            label_typw.place(x=X, y=Y + 40)
            X += 50
            w+=1
            if w == 5:
                Y+=200




interfejs()