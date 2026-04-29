from abc import ABC, abstractmethod

class Samochody:
    def __init__(self, brend, cena, rok, droga_do_obrazu):
        self.brend = brend
        self.cena = cena
        self.rok = rok
        self.droga_do_obrazu = droga_do_obrazu

    @abstractmethod
    def znalesc(self, min_cena, max_cena, brend):
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
    def znalesc(self, min_cena, max_cena, brend):
        sort_lista = []
        if min_cena == '':
            min_cena = 0
        if max_cena == '':
            max_cena = 999999999

        for i in Motory.lista:
            if (int(i.cena) >= int(min_cena) or min_cena == 0) and (int(i.cena) <= int(max_cena) or max_cena == 999999999) and (str(i.brend) == str(brend) or brend == ''):
                sort_lista.append({"cena":i.cena, "brend":i.brend, "typ": "Motory"})
        return sort_lista


class Ciezarowki(Samochody):
    lista = []
    def __init__(self, brend, cena, rok, droga_do_obrazu, nosnosc, liczba_osi):
        super().__init__(brend, cena, rok, droga_do_obrazu)
        self.nosnosc = nosnosc
        self.liczba_osi = liczba_osi
        Ciezarowki.lista.append(self)

    @classmethod
    def znalesc(self, min_cena, max_cena, brend):
        sort_lista = []
        if min_cena == '':
            min_cena = 0
        if max_cena == '':
            max_cena = 999999999

        for i in Ciezarowki.lista:
            if (int(i.cena) >= int(min_cena) or min_cena == 0) and (int(i.cena) <= int(max_cena) or max_cena == 999999999) and (str(i.brend) == str(brend) or brend == ''):
                sort_lista.append({"cena": i.cena, "brend": i.brend, "typ": "Ciezarowki"})
        return sort_lista

class Zwykle_samochody(Samochody):
    lista = []
    def __init__(self, brend, cena, rok, droga_do_obrazu,typ_paliwa, skrzynia_biegow):
        super().__init__(brend, cena, rok, droga_do_obrazu)
        self.typ_paliwa = typ_paliwa
        self.skrzynia_biegow = skrzynia_biegow
        Zwykle_samochody.lista.append(self)

    @classmethod
    def znalesc(self, min_cena, max_cena, brend):
        sort_lista = []
        if min_cena == '':
            min_cena = 0
        if max_cena == '':
            max_cena = 999999999

        for i in Zwykle_samochody.lista:
            if (int(i.cena) >= int(min_cena) or min_cena == 0) and (
                    int(i.cena) <= int(max_cena) or max_cena == 999999999) and (
                    str(i.brend) == str(brend) or brend == ''):
                sort_lista.append({"cena": i.cena, "brend": i.brend, "typ": "Zwykle_samochody"})
        return sort_lista

motor1 = Motory("Yamaha", 15000, 2021, "yamaha_r6.jpg", 600, 240, False)
motor2 = Motory("Yamaha", 15000, 2022, "yamaha_mt07.jpg", 689, 205, False)
motor3 = Motory("Suzuki", 12000, 2024, "suzuki_gsx.jpg", 750, 220, True)
motor4 = Motory("Yamaha", 15000, 2022, "yamaha_r1.jpg", 998, 290, False)
motor5 = Motory("Honda", 18000, 2019, "honda_cbr.jpg", 1000, 280, True)
motor6 = Motory("Kawasaki", 14000, 2015, "kawasaki_ninja.jpg", 650, 230, False)
motor7 = Motory("BMW", 20000, 2014, "bmw_s1000rr.jpg", 999, 295, True)
Ciezarowka1 = Ciezarowki("Yamaha", 18000, 2022, "yamaha_r6.jpg", 600, 2)
Ciezarowka2 = Ciezarowki("Yamaha", 1000, 2021, "yamaha_mt07.jpg", 689, 5)
Ciezarowka3 = Ciezarowki("Suzuki", 12670, 2023, "suzuki_gsx.jpg", 750, 4)
Ciezarowka4 = Ciezarowki("Yamaha", 25099, 2020, "yamaha_r1.jpg", 998, 2)
Ciezarowka5 = Ciezarowki("Honda", 17067, 2023, "honda_cbr.jpg", 1000, 8)
Ciezarowka6 = Ciezarowki("Kawasaki", 14500, 2022, "kawasaki_ninja.jpg", 650, 2)
Ciezarowka7 = Ciezarowki("BMW", 27600, 2023, "bmw_s1000rr.jpg", 999, 6)
Zwykly_samochod1 = Zwykle_samochody("Yamaha", 18000, 2022, "yamaha_r6.jpg", 600, 2)
Zwykly_samochod2 = Zwykle_samochody("Yamaha", 1000, 2021, "yamaha_mt07.jpg", 689, 5)
Zwykly_samochod3 = Zwykle_samochody("Suzuki", 12670, 2023, "suzuki_gsx.jpg", 750, 4)
Zwykly_samochod4 = Zwykle_samochody("Yamaha", 25099, 2020, "yamaha_r1.jpg", 998, 2)
Zwykly_samochod5 = Zwykle_samochody("Honda", 17067, 2023, "honda_cbr.jpg", 1000, 8)
Zwykly_samochod6 = Zwykle_samochody("Kawasaki", 14500, 2022, "kawasaki_ninja.jpg", 650, 2)
