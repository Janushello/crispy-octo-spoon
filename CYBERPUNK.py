import random as ran
import os.path as os
import json


# gracz
class Postac:
    def __init__(self, sila, inteligencja, zwinnosc):
        self.HP = 100
        self.sila = sila
        self.inteligencja = inteligencja
        self.zwinnosc = zwinnosc
        self.naladowanycios = 0


class Gracz(Postac):
    def __init__(self, IMIE, wiek, PLEC, sila, inteligencja, zwinnosc, wplyw):
        super().__init__(sila, inteligencja, zwinnosc)
        self.IMIE = IMIE
        self.wiek = wiek
        self.PLEC = PLEC
        self.exp = 0
        self.wplyw = wplyw

    def awans(self):
        print(
            "wybierz statystykę do ulepszenia \n1 - siła\n2 -zwinność\n3 - inteligencja"
        )
        wybor = input()
        if wybor == "1":
            self.sila += 1
        elif wybor == "2":
            self.zwinnosc += 1
        elif wybor == "3":
            self.inteligencja += 1

    def __str__(self):
        return (
            "Twoje statysyki to: \nimie: "
            + str(self.IMIE)
            + "\nwiek:"
            + str(self.wiek)
            + "\nplec: "
            + str(self.PLEC)
            + "\nzdrowie: "
            + str(self.HP)
            + "\nsila: "
            + str(self.sila)
            + "\ninteligencja: "
            + str(self.inteligencja)
            + "\nzwinnosc: "
            + str(self.zwinnosc)
            + "\nwplywy: "
            + str(self.wplyw)
            + "\nexp: "
            + str(self.exp)
        )


class Przeciwnik(Postac):
    def __init__(self, frakcja, klasa, sila, inteligencja, zwinnosc):
        super().__init__(sila, inteligencja, zwinnosc)
        self.frakcja = frakcja
        self.klasa = klasa

    def __str__(self):
        return (
            "Statystyki przeciwnika: \nfrakcja: "
            + str(self.frakcja)
            + "\nklasa: "
            + str(self.klasa)
            + "\nzdrowie: "
            + str(self.HP)
            + "\nsila: "
            + str(self.sila)
            + "\ninteligencja: "
            + str(self.inteligencja)
            + "\nzwinnosc: "
            + str(self.zwinnosc)
        )

    def __del__(self):
        return True


def losowanie():
    frakcja = ran.choice(FRAKCJE)
    przeciwnicy = PRZECIWNICY[frakcja]
    return [frakcja, przeciwnicy, ran.randint()]


# poziom trudności przeciwników od najłatwiejszego jest od lewej
PRZECIWNICY = {
    "Daro": ["Banita", "Nemrod", "Kapłan"],
    "Alsnur": ["Nomad", "Hadysta", "Doksyjczyk"],
    "Taozi": ["Keneko", "Mikiri", "Onryo"],
    "Kontynuatorzy": ["Kadet", "Weteran", "Cyborg"],
}
FRAKCJE = PRZECIWNICY.keys()
EXP = [15, 30, 45]


def walka():
    staty = losowanie()
    przeciwnik = Przeciwnik(staty[0], staty[1], staty[2], staty[3], staty[4])
    while przeciwnik.HP > 0 and gracz.HP > 0:
        print("1 opis gracza i przeciwnika\n2 atak\n3 naładuj atak\n4nic nie rób")
        odp2 = input()
        if odp2 == "1":
            print(gracz)
            print(przeciwnik)
        elif odp2 == "2":
            przeciwnik.HP = przeciwnik.HP - 5 - (gracz.naladowanycios * 5)
        elif odp2 == "3":
            gracz.naladowanycios += 1
    if gracz.HP > 0:
        index = PRZECIWNICY[przeciwnik.frakcja].index(przeciwnik.klasa)
        gracz.exp += EXP[index]
        del przeciwnik
    else:
        return False
    if gracz.exp > 100:
        gracz.awans()
        gracz.exp -= 100
    return True


def wczytaj():
    while True:
        zap = input(
            "wpisz nazwę zapisu lub wpisz 2 aby cofnąć(po wciśnięciu enter domyślna nazwa będzie zapis)"
        )
        if zap == "":
            zap = "zapis"
            print("działa if")
            break

        elif zap == "2":
            return 2
        zap = zap + ".json"
        print(zap)
    zap = zap + ".json"
    if os.exists(zap):
        print("znajduje plik i dodaje rozszerzenie")
    else:
        print("Nie ma pliku o takiej nazwie.")

    with open(zap, "r") as plik:
        data = json.load(plik)
        profil = [
            data["imie"],
            data["wiek"],
            data["plec"],
            data["sila"],
            data["zwinnosc"],
            data["inteligencja"],
            data["wplyw"],
            data["exp"],
        ]
    return profil


def wstep():
    with open("wstep1.txt", "r") as file:
        wstep = file.read()
    print(wstep)
    IMIE = input("Imię: ")
    while True:
        wiek = input("Wiek (18-50):")
        if 18 <= int(wiek) <= 50:
            break
        else:
            print("Wprowadź poprawny wiek.")
    while True:
        PLEC = input("Płeć (m/k): ")
        if PLEC == "m" or PLEC == "k":
            break
        else:
            print("Wprowadź poprawną płeć.")
    profil = [IMIE, wiek, PLEC, 1, 1, 1, 0]
    print(
        "twoje statystyki domyślnie wynoszą \nsiła 1\ninteligencja 1\nzwinność 1\n wpływ 0\nz każdym wiekiem będziesz mógł wyznaczyć 2 punkty rozwoju na ulepszenie statystyk"
    )
    print("strażnik z krzywym spojrzeniem i przepuszcza cię dalej")
    return profil


# wczytywanie
while True:
    wczytanie = input("czy chcesz wczytać zapis? \n1 tak \n2 nie\n")
    if wczytanie == "1":
        ust = wczytaj()
        if ust == 2:
            pass
        else:
            gracz = Gracz(
                ust[0],
                int(ust[1]),
                ust[2],
                int(ust[3]),
                int(ust[4]),
                int(ust[5]),
                int(ust[6]),
            )
            break
    elif wczytanie == "2":
        ust = wstep()
        gracz = Gracz(
            ust[0],
            int(ust[1]),
            ust[2],
            int(ust[3]),
            int(ust[4]),
            int(ust[5]),
            int(ust[6]),
        )
        break
    else:
        print("wybierz 1 lub 2")


# gra

while True:
    print("co chcesz zrobić?")
    print("1. sprawdź opis postaci" "\n2. walka \n3 wyjście")
    wybormenu = input()
    if wybormenu == "1":
        print(gracz)
    if wybormenu == "2":
        if walka():
            pass
        else:
            wczytaj()
    if wybormenu == "3":
        break

# zapis
print("czy chcesz zapisać grę")
print("1 tak\n2 nie\nenter aby zapisać pod domyślną nazwą zapis\n")
while True:
    pyt1 = input()
    if pyt1 == "1":
        while True:
            zap = input("wpisz nazwę zapisu:")
            if zap != "":
                with open(zap + ".json", "w", encoding="utf-8") as f:
                    data = {
                        "imie": gracz.IMIE,
                        "wiek": gracz.wiek,
                        "plec": gracz.PLEC,
                        "sila": gracz.sila,
                        "zwinnosc": gracz.zwinnosc,
                        "inteligencja": gracz.inteligencja,
                        "wplyw": gracz.wplyw,
                        "exp": gracz.exp,
                    }
                    zapis = json.dumps(data)
                    f.write(zapis)
                f.close()
                break
            else:
                print("nie wpisano nazwy")
    elif pyt1 == "":
        zap = "zapis.json"
        with open(zap, "w", encoding="utf-8") as f:
            data = {
                "imie": gracz.IMIE,
                "wiek": gracz.wiek,
                "plec": gracz.PLEC,
                "sila": gracz.sila,
                "zwinnosc": gracz.zwinnosc,
                "inteligencja": gracz.inteligencja,
                "wplyw": gracz.wplyw,
                "exp": gracz.exp,
            }
            zapis = json.dumps(data)
            f.write(zapis)
            break
    elif pyt1 == "2":
        break
    else:
        print("wybierz 1, 2 lub enter")
