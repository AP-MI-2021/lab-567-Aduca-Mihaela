from Logic.CRUD import adaugaRezervare
from Tests.testAll import runAllTests
from UI.commandLine import mainCommandLine
from UI.console import runMenu


def main():
    runAllTests()
    lista = []
    lista = adaugaRezervare("1", "Martinescu", "economy", 350, "da", lista)
    lista = adaugaRezervare("2", "Popescu", "economy plus", 100, "da", lista)
    #lista = adaugaRezervare("3", "Popescu", "business", 550, "da", lista)
    #lista = adaugaRezervare("4", "Olariu", "economy", 200, "nu", lista)
    while True:
        print("Tastati 1 pentru meniu.")
        print("Tastati 2 pentru comenzi.")
        print("Introduceti: ")
        optiune = input()
        if optiune == "1":
            runMenu(lista)
        elif optiune == "2":
            lista = mainCommandLine(lista)




main()