from Logic.CRUD import adaugaRezervare
from Tests.testAll import runAllTests
from UI.console import runMenu


def main():
    runAllTests()
    lista = []
    lista = adaugaRezervare("1", "Martinescu", "economy", 350, "da", lista)
    lista = adaugaRezervare("2", "Popescu", "bussines", 300, "nu", lista)
    runMenu(lista)
main()