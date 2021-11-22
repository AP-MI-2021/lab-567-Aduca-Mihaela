from Domain.rezervare import toString
from Logic.CRUD import stergeRezervare, getById, adaugaRezervare


def print_help():
    print("Comenzi disponibile: ")
    print("Ajutor: ")
    print("Adauga rezervare: adauga, id, nume, clasa, pret, checkin ")
    print("Sterge rezervare: sterge, id ")
    print("Afisare: showall ")
    print("Stop ")
    print("Parametrii trebuie separati prin virgula. ")
    print("Comenzile trebuie separate prin ; ")

def adauga(lista, parametrii):
    try:
        if len(parametrii) < 6:
            print("Parametrii insuficienti")
            return lista
        if len(parametrii) > 6:
            print("Prea multi parametrii")
            return lista
        id = str(parametrii[1])
        nume = str(parametrii[2])
        clasa = str(parametrii[3])
        pret = float(parametrii[4])
        checkin = str(parametrii[5])
        lista = adaugaRezervare(id, nume, clasa, pret, checkin, lista)
        print("Adaugare efectuata")
        return lista
    except ValueError as ve :
        print("Eroare: {}".format(ve))
        return lista

def sterge(lista, parametrii):
    try:
        if len(parametrii) < 2:
            print("Parametrii insuficienti")
            return lista
        if len(parametrii) > 2:
            print("Prea multi parametrii")
            return lista
        id = parametrii[1]
        if getById(id, lista) is None:
            raise ValueError("Nu exista rezervare cu Id-ul dat")
        print("Stergere efectuata")
        return stergeRezervare(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def showall(lista, parametrii):
    if len(parametrii)>1:
        print("Comanda Afisare nu contine alti parametrii")
    else:
        for rezervare in lista:
            print(toString(rezervare))

def mainCommandLine(lista):
    contor = True
    print("Comenzi disponibile: ")
    print("Ajutor: ")
    print("Adauga rezervare: adauga, id, nume, clasa, pret, checkin ")
    print("Sterge rezervare: sterge, id ")
    print("Afisare: showall ")
    print("Stop ")
    print("Parametrii trebuie separati prin virgula. ")
    print("Comenzile trebuie separate prin ; ")
    while contor:
        comenzi = input("Introduceti comenzile (Ajutor, Adauga, Sterge, Afisare, Stop): ")
        functii = comenzi.split(";")
        for functie in functii:
            parametrii = functie.split(",")
            if(parametrii[0] == "Ajutor"):
                print_help()
            elif parametrii[0] == "Adauga":
                lista = adauga(lista, parametrii)
            elif parametrii[0] == "Sterge":
                lista = sterge(lista, parametrii)
            elif parametrii[0] == "Afisare":
                print("Lista de rezervari este: ")
                showall(lista, parametrii)
            elif parametrii[0] == "Stop":
                contor = False
            else:
                print("Comanda incorecta! Reincercati!")