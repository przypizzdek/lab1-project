import tkinter as tk
from models import Motory,Zwykle_samochody, Ciezarowki
class interfejs():

    biezacy_typ = ''
    przeszla_lista = []
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Katalog samochodów")

        X = 100
        Y = 300
        #self.label_typ = tk.Label(text="Typ")
        #self.label_typ.place(x=X, y=Y)
        #self.entry_typ = tk.Entry()
        #self.entry_typ.place(x=X-50, y=Y+30)

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

        self.nacisk_znalesc = tk.Button(text="Znalesc", command=self.znalesc_call_back)
        self.nacisk_znalesc.place(x=X-10, y=Y+210)



        self.label_Katalogi = tk.Label(text="Katalogi")
        self.label_Katalogi.place(x=X-10, y=Y - 200)

        self.bMotory = tk.Button(text="Motory",command=self.Motory_call_back)
        self.bMotory.place(x=X-60, y=Y - 160)
        self.bCiezarowki = tk.Button(text="Ciezarowki",command=self.Ciezarowki_call_back)
        self.bCiezarowki.place(x=X+20, y=Y - 160)
        self.bZwykle_samochody = tk.Button(text="Zwykle_samochody",command=self.Zwykle_samochody_call_back)
        self.bZwykle_samochody.place(x=X - 60, y=Y - 120)
        self.nacisk_pokazacWS = tk.Button(text="Pokazać wszystkie samochody", command=self.PokazacWS_call_back)
        self.nacisk_pokazacWS.place(x=X - 50, y=Y -80)

        self.window.mainloop()

    def PokazacWS_call_back(self):
        self.button_znalesc("0x76xc8e7r8rt621")

    def znalesc_call_back(self):
        if interfejs.biezacy_typ == '':
            print("hghg")
        else:
            self.button_znalesc(interfejs.biezacy_typ)

    def Motory_call_back(self):
        self.button_znalesc("Motory")

    def Ciezarowki_call_back(self):
        self.button_znalesc("Ciezarowki")

    def Zwykle_samochody_call_back(self):
        self.button_znalesc("Zwykle_samochody")

    def button_znalesc(self, typ):

        if len(interfejs.przeszla_lista) != 0:
             X1 = 700
             Y1 = 50
             w1 = 0
             for i in interfejs.przeszla_lista:
                 label_typw = tk.Label(text='                                  ')
                 label_typw.place(x=X1, y=Y1)
                 label_cenaw = tk.Label(text='                                  ')
                 label_cenaw.place(x=X1, y=Y1 + 20)
                 label_typw = tk.Label(text='                                  ')
                 label_typw.place(x=X1, y=Y1 + 40)
                 X1 += 150
                 w1+=1
                 if w1 == 5:
                     Y1+=200
                     X1 = 700
                     w1 = 0

        interfejs.biezacy_typ = typ

        min_cena = self.entry_cena_od.get()
        max_cena = self.entry_cena_do.get()
        brend = self.entry_brend.get()

        lista_klasow = {
            "Motory": Motory,
            "Ciezarowki": Ciezarowki,
            "Zwykle_samochody": Zwykle_samochody}

        result_lista = []


        if typ == "0x76xc8e7r8rt621":
            for n in lista_klasow:
                Klas = lista_klasow[n]
                for i in Klas.znalesc(min_cena, max_cena, brend):
                    result_lista.append(i)
        elif typ in lista_klasow:
            Klas = lista_klasow[typ]
            result_lista = Klas.znalesc(min_cena, max_cena, brend)

        interfejs.przeszla_lista = result_lista

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
            X += 150
            w+=1
            if w == 5:
                Y+=200
                X = 700
                w = 0



interfejs()