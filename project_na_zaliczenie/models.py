from abc import ABC, abstractmethod

class Samochody:
    def __init__(self, brend, cena, rok, droga_do_obrazu):
        self.brend = brend
        self.cena = cena
        self.rok = rok
        self.droga_do_obrazu = droga_do_obrazu

    @abstractmethod
    def znalesc(self):
        pass




class Motory(Samochody):
    def __init__(self, brend, cena, rok, droga_do_obrazu, pojemnosc_silnika, maks_predkosc, ma_bagaznik):
        super().__init__(brend, cena, rok, droga_do_obrazu)
        self.pojemnosc_silnika = pojemnosc_silnika
        self.maks_predkosc = maks_predkosc
        self.ma_bagaznik = ma_bagaznik


class Ciezarowki(Samochody):
    def __init__(self, brend, cena, rok, droga_do_obrazu, nosnosc, liczba_osi):
        super().__init__(brend, cena, rok, droga_do_obrazu)
        self.nosnosc = nosnosc
        self.liczba_osi = liczba_osi

class Zwykle_samochody(Samochody):
    def __init__(self, brend, cena, rok, droga_do_obrazu,typ_paliwa, skrzynia_biegow):
        super().__init__(brend, cena, rok, droga_do_obrazu)
        self.typ_paliwa = typ_paliwa
        self.skrzynia_biegow = skrzynia_biegow

