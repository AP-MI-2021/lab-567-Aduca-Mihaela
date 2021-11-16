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


def uiAdaugareRezervare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        clasa = input("Dati clasa: ")
        pret = float(input("Dati pretul: "))
        checkin = input("Dati stadiul checkin-ului: ")

        rezultat = adaugaRezervare(id, nume, clasa, pret, checkin, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista


def uiStergereRezervare(lista, undoList, redoList):
    id = input("Dati id-ul rezervarii de sters: ")

    rezultat = stergeRezervare(id, lista)
    undoList.append(lista)
    redoList.clear()
    return rezultat



def uiModificareRezervare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul rezervarii de modificat: ")
        nume = input("Dati noul nume: ")
        clasa = input("Dati noua clasa: ")
        pret = float(input("Dati noul pret: "))
        checkin = input("Dati noul checkin: ")

        rezultat = modificaRezervare(id, nume, clasa, pret, checkin, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista

def uiTrecereRezervare(lista, undoList, redoList):
    try:
        numeCitit = input("Dati numele pentru care se vor aplica schimbarile: ")

        rezultat = trecereRezervariClasaSuperioara(numeCitit, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista


def uiIeftinireRezervare(lista, undoList, redoList):
    try:
        procentaj = float(input("Dati procentajul cu care se va face ieftinirea: "))

        rezultat = ieftinireRezervari(procentaj, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista


def uiDeterminarePretMaximPeClasa(lista):
    pretMaximEconomy, pretMaximEconomyPlus, pretMaximBusiness = determinarePretMaximClasa(lista)
    print("Pretul maxim la clasa economy este " + str(pretMaximEconomy))
    print("Pretul maxim la clasa economy_plus este " + str(pretMaximEconomyPlus))
    print("Pretul maxim la clasa business este " + str(pretMaximBusiness))


def uiOrdoneazaDescrescatorDupaPret(lista):
    return ordonareDescrescatorDupaPret(lista)

def uiSumePretPentruNume(lista):
    rezultat = sumePentruFiecareNume(lista)
    for nume in rezultat:
        print("{} are suma de {}".format(nume, rezultat[nume]))


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
            undoList.append(lista)
            lista = uiAdaugareRezervare(lista, undoList, redoList)
        elif optiune == "2":
            lista = uiStergereRezervare(lista, undoList, redoList)
        elif optiune == "3":
            lista = uiModificareRezervare(lista, undoList, redoList)
        elif optiune == "4":
            lista = uiTrecereRezervare(lista, undoList, redoList)
        elif optiune == "5":
            lista = uiIeftinireRezervare(lista, undoList, redoList)
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