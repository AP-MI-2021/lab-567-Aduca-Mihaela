from Domain.rezervare import toString
from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare
from Logic.functionalitati import trecereRezervariClasaSuperioara, ieftinireRezervari


def printMenu():
    print("1. Adauga rezervare")
    print("2. Sterge rezervare")
    print("3. Modifica rezervare")
    print("4. Trecerea tuturor rezervarilor facute pe un nume citit, la o clasa superioara")
    print("5. Ieftinirea rezervarilor la care s-a facut checkin cu un procentaj citit")
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
    procentaj = float(input("Dati procentajul cu care se va face ieftinirea: "))
    return ieftinireRezervari(procentaj, lista)

def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))


def runMenu(lista):
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
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")