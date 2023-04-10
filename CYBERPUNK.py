import random as ran
import os.path as os

#gracz
class Postac:
    def __init__(self, sila, inteligencja, zwinnosc):
        self.HP = 100
        self.sila = sila
        self.inteligencja = inteligencja
        self.zwinnosc = zwinnosc
        self.naladowanycios = 0
    

class Gracz(Postac):
    def __init__(self, imie, wiek, plec, sila, inteligencja, zwinnosc, wplyw):
        super().__init__(sila,inteligencja,zwinnosc)
        self.imie = imie
        self.wiek = wiek
        self.plec = plec
        self.exp = 0
        self.wplyw = wplyw

    def awans(self):
        print("wybierz statystykę do ulepszenia \n1 - siła\n2 -zwinność\n3 - inteligencja")
        wybor = input()
        if wybor == "1":
            self.sila +=1
        elif wybor == "2":
            self.zwinnosc+=1
        elif wybor== "3":
            self.inteligencja+=1


    def __str__(self):
            return "Twoje statysyki to: \nimie: "+str(self.imie)+"\nwiek:"+str(self.wiek)+"\nplec: "+str(self.plec)+"\nzdrowie: "+str(self.HP)+"\nsila: "+str(self.sila)+"\ninteligencja: "+str(self.inteligencja)+"\nzwinnosc: "+str(self.zwinnosc)+"\nwplywy: "+str(self.wplyw)+"\nexp: "+str(self.exp)


class Przeciwnik(Postac):
    def __init__(self, frakcja, klasa, sila, inteligencja, zwinnosc):
        super().__init__(sila,inteligencja,zwinnosc)
        self.frakcja = frakcja
        self.klasa = klasa


    def __str__(self):
        return "Statystyki przeciwnika: \nfrakcja: "+str(self.frakcja)+"\nklasa: "+str(self.klasa)+"\nzdrowie: "+str(self.HP)+"\nsila: "+str(self.sila)+"\ninteligencja: "+str(self.inteligencja)+"\nzwinnosc: "+str(self.zwinnosc)

    
    def __del__(self):
        return True

# poziom trudności przeciwników od najłatwiejszego jest od lewej
przeciwnicyDaro = ['Banita', 'Nemrod', 'Kapłan'] 
przeciwnicyAlsnur = ['Nomad', 'Hadysta', 'Doksyjczyk']
przeciwnicyTaozi = ['Keneko', 'Mikiri', 'Onryo']#japonia
przeciwnicyKontynuatorzy = ['Kadet', 'Cyborg', 'Weteran']
Frakcje = ['Alsnur', 'Taozi', 'Daro', 'Kontynuatorzy']


def walka():
    frakcja = ran.choice(Frakcje)
    if frakcja == 'Alsnur':
        pstaty = [ran.choice(przeciwnicyAlsnur), ran.randint(1,gracz.sila+1), ran.randint(1,gracz.inteligencja+1), ran.randint(1,gracz.zwinnosc+1)]
        przeciwnik = Przeciwnik(frakcja,pstaty[0],pstaty[1],pstaty[2],pstaty[3])
    elif frakcja == 'Taozi':
        pstaty = [ran.choice(przeciwnicyTaozi), ran.randint(1,gracz.sila+1), ran.randint(1,gracz.inteligencja+1), ran.randint(1,gracz.zwinnosc+1)]
        przeciwnik = Przeciwnik(frakcja,pstaty[0],pstaty[1],pstaty[2],pstaty[3])
    elif frakcja == 'Daro':
        pstaty = [ran.choice(przeciwnicyDaro), ran.randint(1,gracz.sila+1), ran.randint(1,gracz.inteligencja+1), ran.randint(1,gracz.zwinnosc+1)]
        przeciwnik = Przeciwnik(frakcja,pstaty[0],pstaty[1],pstaty[2],pstaty[3])
    elif frakcja == 'Kontynuatorzy':
        pstaty = [ran.choice(przeciwnicyKontynuatorzy), ran.randint(1,gracz.sila+1), ran.randint(1,gracz.inteligencja+1), ran.randint(1,gracz.zwinnosc+1)]
        przeciwnik = Przeciwnik(frakcja,pstaty[0],pstaty[1],pstaty[2],pstaty[3])
    while przeciwnik.HP>0 and gracz.HP>0:
        print("1 opis gracza i przeciwnika\n2 atak\n3 naładuj atak\n4nic nie rób")
        odp2 = input()
        if odp2 == "1":
            print(gracz)
            print(przeciwnik)
        elif odp2 == "2":
            przeciwnik.HP=przeciwnik.HP - 5-(gracz.naladowanycios*5)
        elif odp2 == "3":
            gracz.naladowanycios+=1
    if gracz.HP>0:
        if frakcja == 'Alsnur':
            gracz.exp+=15*((1+przeciwnicyAlsnur.index(przeciwnik.klasa)))
        elif frakcja == 'Taozi':
            gracz.exp+=15*((1+przeciwnicyTaozi.index(przeciwnik.klasa)))
        elif frakcja == 'Daro':
            gracz.exp+=15*((1+przeciwnicyDaro.index(przeciwnik.klasa)))
        elif frakcja == 'Kontynuatorzy':
            gracz.exp+=15*((1+przeciwnicyKontynuatorzy.index(przeciwnik.klasa)))
        del przeciwnik
    else :
        return False
    if gracz.exp>100:
        gracz.awans()
        gracz.exp-=100
    return True

def wczytaj(zap):
    ust = []
    with open(zap, 'r') as plik:
        for z in plik.readlines():
            ust.append(z.strip())
        plik.close()
    if len(ust) != 7:
        print("zapis został uszkodzony czy chcesz wczytać inny zapis?")
        print("tak/nie")
        if input() == "nie":
            ust = wstep()
        elif input() == "tak":
            return False
    return ust

wstep1 = "Rozpoczynasz swoją przygodę jako zwykły człowiek, ale szybko odkrywasz, że aby przetrwać w tym świecie, musisz zdobyć siłę i "
"umiejętności, których nie da się zdobyć w sposób naturalny. Wkraczasz więc na ścieżkę cybernetycznej modyfikacji, w której twoje ciało i umysł "
"stają się jednym z technologią. Zyskujesz zdolności, których wcześniej nie miałeś, ale równocześnie tracisz swoją ludzkość.Musisz teraz dokonywać "
"trudnych wyborów, czy pozostać przy swoich ideałach i wartościach, czy też poddać się technologicznej rewolucji. Czy pozostaniesz człowiekiem, czy "
"też stworzysz siebie na nowo jako hybrydę człowieka i maszyny? Czy będziesz walczył z systemem, czy też stanie się jego częścią?"
"Przechodząc obok niego, słyszysz jedynie twardy, zimny głos: \"ID, teraz.\" Odpowiadasz na jego żądanie, czując jego wzrok na sobie, "
"badający każdy ruch, jakby patrzył na potencjalnego wroga. "
wstep2 = "\"Nie z tej okolicy, co?\" kontynuuje, po czym robi chwilową przerwę, patrząc na ciebie z zainteresowaniem. \"Nie widzę zbyt wielu ludzi "
"z pustkowi. Co cię tu sprowadza?\" Pytanie brzmi proste, ale w jego tonie słychać subtelny sygnał ostrzegawczy."

drzewko_sily=[]
drzewko_zwinnosci=[]
drzewko_inteligencji=[]
drzewko_wplywu=[]


def wstep():

    print(wstep1)
    imie = input("Imię: ")
    while True:
        wiek = input("Wiek (18-50):")
        if 18 <= int(wiek) <= 50:
            break
        else:
            print("Wprowadź poprawny wiek.")
    while True:
        plec = input("Płeć (m/k): ")
        if plec == "m" or plec == 'k':
            break
        else:
            print("Wprowadź poprawną płeć.")
    profil = [imie, wiek, plec, 1, 1, 1, 0]
    print(
        "twoje statystyki domyślnie wynoszą \nsiła 1\ninteligencja 1\nzwinność 1\n wpływ 0\nz każdym wiekiem będziesz mógł wyznaczyć 2 punkty rozwoju na ulepszenie statystyk")
    print("strażnik z krzywym spojrzeniem i przepuszcza cię dalej")
    return profil

ust = '0'
zap = "zapis"
#wczytywanie
while True:
    wczytanie = input("czy chcesz wczytać zapis? \n1 tak \n2 nie\n")
    if wczytanie == '1':
        while True:
            zap = input("wpisz nazwę zapisu lub wpisz 2 aby cofnąć(po wciśnięciu enter domyślna nazwa będzie zapis)")
            if zap == "":
                zap = 'zapis'
            elif zap == '2':
                break
            if os.exists(zap + '.txt'):
                zap = zap + '.txt'
                ust = wczytaj(zap)
                if len(ust)==7:
                    break

            else:
                print("Nie ma pliku o takiej nazwie.")
    elif wczytanie == '2':
        ust = wstep()
        break
    else:
        print("Wpisz 1 lub 2")
    if zap != "2" or len(ust) == 7:
        break
gracz = Gracz(ust[0], int(ust[1]), ust[2], int(ust[3]), int(ust[4]), int(ust[5]), int(ust[6]))

#gra

while True:
    print("co chcesz zrobić?")
    print("1. sprawdź opis postaci"
          "\n2. walka \n3 wyjście")
    wybormenu = input()
    if wybormenu == "1":
        print(gracz)
    if wybormenu == "2":
        if walka():
            pass
        else:
            wczytaj(zap)
    if wybormenu == "3":
        break

#zapis
print("czy chcesz zapisać grę")
pyt1 = input("1 tak\n2 nie\nenter aby zapisać pod domyślną nazwą zapis\n")
if pyt1 == '1':
    while True:
        zap = input("wpisz nazwę zapisu:")+'.txt'
        if ord("0")<=ord(zap)<=ord("9"):
            with open(zap, 'w', encoding="utf-8") as f:
                f.write(f'{gracz.imie}\n')
                f.write(f'{gracz.wiek}\n')
                f.write(f'{gracz.plec}\n')
                f.write(f'{gracz.sila}\n')
                f.write(f'{gracz.inteligencja}\n')
                f.write(f'{gracz.zwinnosc}\n')
                f.write(f'{gracz.wplyw}')
                f.close()
        else:
            print("nie wykorzystuj cyfr (możesz liczby)")
elif pyt1 == '':
    zap = 'zapis.txt'
    with open(zap, 'w', encoding="utf-8") as f:
        f.write(f'{gracz.imie}\n')
        f.write(f'{gracz.wiek}\n')
        f.write(f'{gracz.plec}\n')
        f.write(f'{gracz.sila}\n')
        f.write(f'{gracz.inteligencja}\n')
        f.write(f'{gracz.zwinnosc}\n')
        f.write(f'{gracz.wplyw}')
        f.close()

