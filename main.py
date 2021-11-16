from Logic.CRUD import adaugaRezervare
from Tests.testAll import runAllTests
from UI.console import runMenu


def main():
    runAllTests()
    lista = []
    lista = adaugaRezervare("1", "Martinescu", "economy", 350, "da", lista)
    lista = adaugaRezervare("2", "Popescu", "economy plus", 100, "da", lista)
    lista = adaugaRezervare("3", "Popescu", "business", 550, "da", lista)
    lista = adaugaRezervare("4", "Olariu", "economy", 200, "nu", lista)

    runMenu(lista)


main()