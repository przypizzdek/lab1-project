from abc import ABC, abstractmethod
import json

class Samochody:
    def __init__(self, brend, cena, rok, droga_do_obrazu,model):
        self.brend = brend
        self.cena = cena
        self.rok = rok
        self.droga_do_obrazu = droga_do_obrazu
        self.model = model

    @abstractmethod
    def znalesc(self, min_cena, max_cena, brend,model,rok):
        pass

    @abstractmethod
    def Tworzenie_obiektow_z_pliku(self):
        pass

class Motory(Samochody):
    lista = []
    def __init__(self, brend, cena, rok,droga_do_obrazu,model, engine_size,power):
        super().__init__(brend, cena, rok,droga_do_obrazu,model)
        self.droga_do_obrazu = droga_do_obrazu
        self.engine_size = engine_size
        self.power = power
        Motory.lista.append(self)

    @classmethod
    def znalesc(self, min_cena, max_cena, brend, model, rok):
        if min_cena == '':
            min_cena = 0
        if max_cena == '':
            max_cena = 999999999

        sort_lista = []
        for i in Motory.lista:
            if ((int(i.cena) >= int(min_cena) or min_cena == 0) and (int(i.cena) <= int(max_cena) or max_cena == 999999999)and (str(i.brend) == str(brend) or brend == '')
                and (str(i.model) == str(model) or model == '') and (str(i.rok) == str(rok) or rok == '')):
                sort_lista.append({"cena":i.cena, "brend":i.brend, "typ": "Motory", "model":i.model,"rok":i.rok})
        return sort_lista

    @classmethod
    def Tworzenie_obiektow_z_pliku(self):
        with open("Motory_data.json", "r", encoding="utf-8") as f:
            dane = json.load(f)
            for motor in dane:
                Motory(
                    brend = motor.get("make", ""),
                    rok =  motor.get("year", 0),
                    cena = 10000,
                    droga_do_obrazu = "",
                    engine_size = motor.get("engine_size", ""),
                    power = motor.get("power", ""),
                    model = motor.get("model", "")
                )


class Electrocary(Samochody):
    lista = []
    def __init__(self, brend, cena, rok, droga_do_obrazu,model, battery_kwh,charge_power):
        super().__init__(brend, cena, rok, droga_do_obrazu,model)
        self.charge_power = charge_power
        self.battery_kwh = battery_kwh
        Electrocary.lista.append(self)

    @classmethod
    def znalesc(self, min_cena, max_cena, brend,model, rok):
        sort_lista = []
        if min_cena == '':
            min_cena = 0
        if max_cena == '':
            max_cena = 999999999

        for i in Electrocary.lista:
            if ((int(i.cena) >= int(min_cena) or min_cena == 0) and (
                    int(i.cena) <= int(max_cena) or max_cena == 999999999) and (
                    str(i.brend) == str(brend) or brend == '')
                    and (str(i.model) == str(model) or model == '') and (str(i.rok) == str(rok) or rok == '')):
                sort_lista.append({"cena": i.cena, "brend": i.brend, "typ": "Electrocary", "model": i.model, "rok": i.rok})
        return sort_lista

    @classmethod
    def Tworzenie_obiektow_z_pliku(self):
        with open("Motory_data.json", "r", encoding="utf-8") as f:
            dane = json.load(f)
            for motor in dane:
                Motory(
                    brend=motor.get("make", ""),
                    rok=motor.get("year", 0),
                    cena=10000,
                    droga_do_obrazu="",
                    engine_size=motor.get("engine_size", ""),
                    power=motor.get("power", ""),
                    model=motor.get("model", "")
                )

class Zwykle_samochody(Samochody):
    lista = []
    def __init__(self, brend, cena, rok, droga_do_obrazu,model):
        super().__init__(brend, cena, rok, droga_do_obrazu,model)
        Zwykle_samochody.lista.append(self)

    @classmethod
    def znalesc(self, min_cena, max_cena, brend,model, rok):
        sort_lista = []
        if min_cena == '':
            min_cena = 0
        if max_cena == '':
            max_cena = 999999999

        for i in Zwykle_samochody.lista:
            if ((int(i.cena) >= int(min_cena) or min_cena == 0) and (
                    int(i.cena) <= int(max_cena) or max_cena == 999999999) and (
                    str(i.brend) == str(brend) or brend == '')
                    and (str(i.model) == str(model) or model == '') and (str(i.rok) == str(rok) or rok == '')):
                sort_lista.append({"cena": i.cena, "brend": i.brend, "typ": "Zwykle_samochody", "model": i.model, "rok": i.rok})
        return sort_lista

    @classmethod
    def Tworzenie_obiektow_z_pliku(self):
        with open("Motory_data.json", "r", encoding="utf-8") as f:
            dane = json.load(f)
            for motor in dane:
                Motory(
                    brend=motor.get("make", ""),
                    rok=motor.get("year", 0),
                    cena=10000,
                    droga_do_obrazu="",
                    engine_size=motor.get("engine_size", ""),
                    power=motor.get("power", ""),
                    model=motor.get("model", "")
                )


motor1 = Motory("Yamaha", 15000, 2021, "yamaha_r6.jpg", 600, 240, False, )
motor2 = Motory("Yamaha", 15000, 2022, "yamaha_mt07.jpg", 689, 205, False)
motor3 = Motory("Suzuki", 12000, 2024, "suzuki_gsx.jpg", 750, 220, True)
motor4 = Motory("Yamaha", 15000, 2022, "yamaha_r1.jpg", 998, 290, False)
motor5 = Motory("Honda", 18000, 2019, "honda_cbr.jpg", 1000, 280, True)
motor6 = Motory("Kawasaki", 14000, 2015, "kawasaki_ninja.jpg", 650, 230, False)
motor7 = Motory("BMW", 20000, 2014, "bmw_s1000rr.jpg", 999, 295, True)
Electrocar1 = Electrocary("Yamaha", 18000, 2022, "yamaha_r6.jpg", 622, 2,1000)
Electrocar2 = Electrocary("Yamaha", 1000, 2021, "yamaha_mt07.jpg", 644, 5,1000)
Electrocar3 = Electrocary("Suzuki", 12670, 2023, "suzuki_gsx.jpg", 744, 4,1000)
Electrocar4 = Electrocary("Yamaha", 25099, 2020, "yamaha_r1.jpg", 955, 2,1000)
Electrocar5 = Electrocary("Honda", 17067, 2023, "honda_cbr.jpg", 1066, 8,1000)
Electrocar6 = Electrocary("Kawasaki", 14500, 2022, "kawasaki_ninja.jpg", 650, 2,1000)
Electrocar7 = Electrocary("BMW", 27600, 2023, "bmw_s1000rr.jpg", 999, 6,1000)
Zwykly_samochod1 = Zwykle_samochody("Yamaha", 18000, 2022, "yamaha_r6.jpg", 600)
Zwykly_samochod2 = Zwykle_samochody("Yamaha", 1000, 2021, "yamaha_mt07.jpg", 689)
Zwykly_samochod3 = Zwykle_samochody("Suzuki", 12670, 2023, "suzuki_gsx.jpg", 750)
Zwykly_samochod4 = Zwykle_samochody("Yamaha", 25099, 2020, "yamaha_r1.jpg", 998)
Zwykly_samochod5 = Zwykle_samochody("Honda", 17067, 2023, "honda_cbr.jpg", 1000)
Zwykly_samochod6 = Zwykle_samochody("Kawasaki", 14500, 2022, "kawasaki_ninja.jpg", 650)
