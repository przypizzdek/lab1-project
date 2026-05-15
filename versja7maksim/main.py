import tkinter as tk
import customtkinter as ctk
from models import Motory,Zwykle_samochody, Electrocary
from reque import Wczytywanie_danych
class interfejs():

    biezacy_typ = ""

    label = []

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Katalog samochodów")

        X = 100
        Y = 300
        
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

        self.label_model = tk.Label(text="Model")
        self.label_model.place(x=X, y=Y + 210)
        self.entry_model = tk.Entry()
        self.entry_model.place(x=X - 50, y=Y + 240)

        self.label_rok = tk.Label(text="Year")
        self.label_rok.place(x=X, y=Y + 270)
        self.entry_rok = tk.Entry()
        self.entry_rok.place(x=X - 50, y=Y + 300)

        self.nacisk_znalesc = tk.Button(text="Znalesc", command=self.znalesc_call_back)
        self.nacisk_znalesc.place(x=X-10, y=Y+480)



        self.label_Katalogi = tk.Label(text="Katalogi")
        self.label_Katalogi.place(x=X-10, y=Y - 200)

        self.bMotory = tk.Button(text="Motory",command=self.Motory_call_back)
        self.bMotory.place(x=X-60, y=Y - 160)
        self.bCiezarowki = tk.Button(text="Electrocary",command=self.Electrocary_call_back)
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

    def Electrocary_call_back(self):
        self.button_znalesc("Electrocary")

    def Zwykle_samochody_call_back(self):
        self.button_znalesc("Zwykle_samochody")

    def button_znalesc(self, typ):

        if len(interfejs.label) != 0:
            for i in interfejs.label:
                i.destroy()
            interfejs.label.clear()

        interfejs.biezacy_typ = typ

        min_cena = self.entry_cena_od.get()
        max_cena = self.entry_cena_do.get()
        brend = self.entry_brend.get()
        model = self.entry_model.get()
        rok = self.entry_rok.get()

        battery_capacity = ""
        charge_power = ""
        engine_size = ""
        power = ""

        lista_klasow = {
            "Motory": Motory,
            "Electrocary": Electrocary,
            "Zwykle_samochody": Zwykle_samochody}

        result_lista = []

        x= 0
        if typ == "0x76xc8e7r8rt621":
            for n in lista_klasow:
                Klas = lista_klasow[n]
                for i in Klas.znalesc(min_cena, max_cena, brend,model, rok):
                    result_lista.append(i)
        elif typ in lista_klasow:
            flag = Wczytywanie_danych(typ, brend, model, rok, battery_capacity, charge_power, engine_size, power)
            Klas = lista_klasow[typ]
            if flag == 0:
                Klas.Tworzenie_obiektow_z_pliku()
            result_lista = Klas.znalesc(min_cena, max_cena, brend,model, rok)



        X = 700
        Y = 50
        w = 0
        for i in result_lista:
            label_typw = tk.Label(text=i["typ"])
            label_typw.place(x=X, y=Y)
            label_cenaw = tk.Label(text=i["cena"])
            label_cenaw.place(x=X, y=Y + 20)
            label_brendw = tk.Label(text=i["brend"])
            label_brendw.place(x=X, y=Y + 40)
            label_modelw = tk.Label(text=i["model"])
            label_modelw.place(x=X, y=Y + 60)
            label_rokw = tk.Label(text=i["rok"])
            label_rokw.place(x=X, y=Y + 80)

            interfejs.label.append(label_typw)
            interfejs.label.append(label_cenaw)
            interfejs.label.append(label_brendw)
            interfejs.label.append(label_modelw)
            interfejs.label.append(label_rokw)
            X += 150
            w+=1
            if w == 5:
                Y+=200
                X = 700
                w = 0



interfejs()