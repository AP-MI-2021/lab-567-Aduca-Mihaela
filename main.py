from Tests.testAll import runAllTests
from UI.commandLine import mainCommandLine
from UI.console import runMenu


def main():
    runAllTests()
    lista = []
    while True:
        option = input("pentru meniu apasati 1, pentru consola apasati 2; pentru a inchide apasai x: ")
        if option == "1":
            runMenu([])
        elif option == "2":
            mainCommandLine(lista)
        elif option == "x":
            break
        else:
            print("optiune gresita")

main()