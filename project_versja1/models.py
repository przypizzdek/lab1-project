from abc import ABC, abstractmethod

class Samochody:
    def __init__(self, brend, cena, rok, droga_do_obrazu):
        self.brend = brend
        self.cena = cena
        self.rok = rok
        self.droga_do_obrazu = droga_do_obrazu

    @abstractmethod
    def znalesc(self, min_cena, max_cena, brend, typ):
        pass



class Motory(Samochody):
    lista = []
    def __init__(self, brend, cena, rok, droga_do_obrazu, pojemnosc_silnika, maks_predkosc, ma_bagaznik):
        super().__init__(brend, cena, rok, droga_do_obrazu)
        self.pojemnosc_silnika = pojemnosc_silnika
        self.maks_predkosc = maks_predkosc
        self.ma_bagaznik = ma_bagaznik
        Motory.lista.append(self)

    @classmethod
    def znalesc(self, min_cena, max_cena, brend, typ):
        sort_lista = []
        for i in Motory.lista:
            if int(i.cena) >= int(min_cena) and int(i.cena) <= int(max_cena) and str(i.brend) == str(brend):
                sort_lista.append({"cena":i.cena, "brend":i.brend, "typ":typ})
        return sort_lista


class Ciezarowki(Samochody):
    def __init__(self, brend, cena, rok, droga_do_obrazu, nosnosc, liczba_osi):
        super().__init__(brend, cena, rok, droga_do_obrazu)
        self.nosnosc = nosnosc
        self.liczba_osi = liczba_osi

    @classmethod
    def znalesc(self, min_cena, max_cena, brend, typ):
        sort_lista = []
        for i in Motory.lista:
            if int(i.cena) >= int(min_cena) and int(i.cena) <= int(max_cena) and str(i.brend) == str(brend):
                sort_lista.append({"cena": i.cena, "brend": i.brend, "typ": typ})
        return sort_lista

class Zwykle_samochody(Samochody):
    def __init__(self, brend, cena, rok, droga_do_obrazu,typ_paliwa, skrzynia_biegow):
        super().__init__(brend, cena, rok, droga_do_obrazu)
        self.typ_paliwa = typ_paliwa
        self.skrzynia_biegow = skrzynia_biegow

    @classmethod
    def znalesc(self, min_cena, max_cena, brend, typ):
        sort_lista = []
        for i in Motory.lista:
            if int(i.cena) >= int(min_cena) and int(i.cena) <= int(max_cena) and str(i.brend) == brend:
                sort_lista.append({"cena": i.cena, "brend": i.brend, "typ": typ})
        return sort_lista

motor1 = Motory("Yamaha", 15000, 2022, "yamaha_r6.jpg", 600, 240, False)
motor2 = Motory("Yamaha", 15000, 2021, "yamaha_mt07.jpg", 689, 205, False)
motor3 = Motory("Suzuki", 12000, 2023, "suzuki_gsx.jpg", 750, 220, True)
motor4 = Motory("Yamaha", 15000, 2020, "yamaha_r1.jpg", 998, 290, False)
motor5 = Motory("Honda", 18000, 2023, "honda_cbr.jpg", 1000, 280, True)
motor6 = Motory("Kawasaki", 14000, 2022, "kawasaki_ninja.jpg", 650, 230, False)
motor7 = Motory("BMW", 20000, 2023, "bmw_s1000rr.jpg", 999, 295, True)