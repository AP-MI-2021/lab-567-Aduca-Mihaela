from Domain.rezervare import toString
from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare
from Logic.functionalitati import trecereRezervariClasaSuperioara, ieftinireRezervari, determinarePretMaximClasa, \
    ordonareDescrescatorDupaPret, sumePentruFiecareNume


def printMenu():
    print("1. Adauga rezervare")
    print("2. Sterge rezervare")
    print("3. Modifica rezervare")
    print("4. Trecerea tuturor rezervarilor facute pe un nume citit, la o clasa superioara")
    print("5. Ieftinirea rezervarilor la care s-a facut checkin cu un procentaj citit")
    print("6.Determinarea prețului maxim pentru fiecare clasă")
    print("7.Ordonarea rezervărilor descrescător după preț.")
    print("8.Afișarea sumelor prețurilor pentru fiecare nume.")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare rezervari")
    print("x. Iesire")


def uiAdaugareRezervare(lista):
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    clasa = input("Dati clasa: ")
    pret = float(input("Dati pretul: "))
    checkin = input("Dati stadiul checkin-ului: ")
    return adaugaRezervare(id, nume, clasa, pret, checkin, lista)


def uiStergereRezervare(lista):
    id = input("Dati id-ul rezervarii de sters: ")
    return stergeRezervare(id, lista)



def uiModificareRezervare(lista):
    id = input("Dati id-ul rezervarii de modificat: ")
    nume = input("Dati noul nume: ")
    clasa = input("Dati noua clasa: ")
    pret = float(input("Dati noul pret: "))
    checkin = input("Dati noul checkin: ")
    return modificaRezervare(id, nume, clasa, pret, checkin, lista)

def uiTrecereRezervare(lista):
    numeCitit = input("Dati numele pentru care se vor aplica schimbarile: ")
    return trecereRezervariClasaSuperioara(numeCitit, lista)

def uiIeftinireRezervare(lista):
    try:
        procentaj = float(input("Dati procentajul cu care se va face ieftinirea: "))
        return ieftinireRezervari(procentaj, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiDeterminarePretMaximPeClasa(lista):
    try:
        pretMaximEconomy, pretMaximEconomyPlus, pretMaximBusiness = determinarePretMaximClasa(lista)
        print("Pretul maxim la clasa economy este " + str(pretMaximEconomy))
        print("Pretul maxim la clasa economy_plus este " + str(pretMaximEconomyPlus))
        print("Pretul maxim la clasa business este " + str(pretMaximBusiness))
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiOrdoneazaDescrescatorDupaPret(lista):
    return ordonareDescrescatorDupaPret(lista)

def uiSumePretPentruNume(lista):
    return sumePentruFiecareNume(lista)


def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))


def runMenu(lista):
    undoList = []
    redoList = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugareRezervare(lista)
        elif optiune == "2":
            lista = uiStergereRezervare(lista)
        elif optiune == "3":
            lista = uiModificareRezervare(lista)
        elif optiune == "4":
            lista = uiTrecereRezervare(lista)
        elif optiune == "5":
            lista = uiIeftinireRezervare(lista)
        elif optiune == "6":
            lista = uiDeterminarePretMaximPeClasa(lista)
        elif optiune == "7":
            lista = uiOrdoneazaDescrescatorDupaPret(lista)
        elif optiune == "8":
            lista = uiSumePretPentruNume(lista)
        elif optiune == "u":
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("Nu se poate face undo! ")
        elif optiune == "r":
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print("Nu se poate face redo! ")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")