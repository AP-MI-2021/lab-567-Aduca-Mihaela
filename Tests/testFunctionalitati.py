from Domain.rezervare import getClasa, getPret, getId, getNume
from Logic.CRUD import adaugaRezervare, getById
from Logic.functionalitati import trecereRezervariClasaSuperioara, ieftinireRezervari, determinarePretMaximClasa, \
    ordonareDescrescatorDupaPret, sumePentruFiecareNume


def testTrecereRezervariClasaSuperioara():
    lista = []
    lista = adaugaRezervare("1", "Martinescu", "economy", 350, "da", lista)
    lista = adaugaRezervare("2", "Popescu", "economy plus", 100 , "da", lista)
    lista = adaugaRezervare("3", "Irimescu", "business", 250, "da", lista)
    lista = trecereRezervariClasaSuperioara("Popescu", lista)

    assert getClasa(lista[0]) == "economy"
    assert getClasa(lista[1]) == "business"

testTrecereRezervariClasaSuperioara()

def testIeftinire():
    lista = []
    lista = adaugaRezervare("454", "Costachescu", "business", 400, "da", lista)
    lista = adaugaRezervare("325", "Grigore", "economy", 230, "nu", lista)

    lista = ieftinireRezervari(20, lista)

    assert getPret(lista[0]) == 320.0
    assert getPret(lista[1]) == 230.0
testIeftinire()

def testDeterminarePretMaximClasa():
    lista = []
    lista = adaugaRezervare("1", "Martinescu", "economy", 350, "da", lista)
    lista = adaugaRezervare("2", "Popescu", "economy plus", 100 , "da", lista)
    lista = adaugaRezervare("3", "Irimescu", "business", 250, "da", lista)
    lista = adaugaRezervare("4", "Mihaila", "economy", 155, "nu", lista)
    lista = adaugaRezervare("5", "Serediuc", "economy plus", 250, "da", lista)
    lista = adaugaRezervare("6", "Olariu", "business", 224, "da", lista)

    pretMaximEconomy, pretMaximEconomyPlus, pretMaximBusiness = determinarePretMaximClasa(lista)
    assert pretMaximEconomy == 350
    assert pretMaximEconomyPlus == 250
    assert pretMaximBusiness == 250
testDeterminarePretMaximClasa()

def testOrdonareDescrescatoareDupaPret():
    lista = []
    lista = adaugaRezervare("1", "Martinescu", "economy", 350, "da", lista)
    lista = adaugaRezervare("2", "Popescu", "economy plus", 100, "da", lista)
    lista = adaugaRezervare("3", "Irimescu", "business", 250, "da", lista)
    lista = ordonareDescrescatorDupaPret(lista)
    assert getId(lista[0]) == "1"
    assert getId(lista[1]) == "3"
    assert getId(lista[2]) == "2"
testOrdonareDescrescatoareDupaPret()

def testSumePentruFiecareNume():
    lista = []
    lista = adaugaRezervare("1", "Martinescu", "economy", 350, "da", lista)
    lista = adaugaRezervare("2", "Popescu", "economy plus", 100, "da", lista)
    lista = adaugaRezervare("3", "Popescu", "business", 550, "da", lista)

    rezultat = sumePentruFiecareNume(lista)
    assert rezultat["Martinescu"] == 350
    assert rezultat["Popescu"] == 650

def testUndoRedo():
    # 1. lista goala
    lista = []
    undoList = []
    redoList = []

    # 2.adaugam prima rezervare
    rezultat = adaugaRezervare("1", "Martinescu", "economy", 350, "da", lista)
    undoList.append(lista)
    lista = rezultat

    # 3.adaugam a doua rezervare
    rezultat = adaugaRezervare("2", "Popescu", "business", 100, "da", lista)
    undoList.append(lista)
    lista = rezultat

    # 4.adaugam a treia rezervare
    rezultat = adaugaRezervare("3", "Popescu", "business", 550, "da", lista)
    undoList.append(lista)
    lista = rezultat

    # 5. primul undo scoate ultima rezervare adaugata
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"
    assert getId(lista[0]) == "1"

    # 6. inca un undo scoate penultima rezervare adaugata
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undoList == [[]]

    # 7. inca un undo scoate prima rezervare adaugata
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 0
    assert undoList == []

    # 8. inca un undo care nu face nimic
    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList
    assert len(lista) == 0
    assert undoList == []

    # 9. se adauga trei rezervari
    rezultat = adaugaRezervare("1", "Martinescu" , "economy", 100, "da", lista)
    undoList.append(lista)
    lista = rezultat
    redoList.clear()

    rezultat = adaugaRezervare("2", "Popescu", "business", 120, "nu", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = adaugaRezervare("3", "Iliescu", "economy plus", 125, "nu", lista)
    undoList.append(lista)
    lista = rezultat

    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3

    # 10. se face redo (fara sa faca nimic)
    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3

    # 11. se fac 2 undo-uri
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"
    assert getId(lista[0]) == "1"

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undoList == [[]]

    # 12. se face redo
    undoList.append(lista)
    lista = redoList.pop()
    assert len(redoList) == 1
    assert len(undoList) == 2
    assert len(lista) == 2

    # 13. se face redo
    undoList.append(lista)
    lista = redoList.pop()
    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3

    # 14. se fac 2 undo-uri
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"
    assert getId(lista[0]) == "1"

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undoList == [[]]

    # 15. se adauga a patra rezervare
    rezultat = adaugaRezervare("4", "Olariu", "economy plus", 250, "da", lista)
    undoList.append(lista)
    lista = rezultat
    redoList.clear()

    # 16. se face redo (fara sa faca nimic)
    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(lista) == 2
    assert len(undoList) == 2

    # 17. se face undo
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert len(undoList) == 1
    assert len(redoList) == 1

    # 18. se face undo
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 0
    assert len(undoList) == 0
    assert len(redoList) == 2

    # 19. se face 2 redo-uri
    undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 1

    undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 2
    assert len(redoList) == 0

    # 20. se face ultimul redo, care nu face nimic
    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(lista) == 2
    assert len(redoList) == 0
    assert len(undoList) == 2


def testUndoRedoTrecereClasaSuperioara():
    # 1. lista goala
    lista = []
    undoList = []
    redoList = []

    # 2. se adauga prima rezervare
    rezultat = adaugaRezervare("1", "Martinescu", "economy", 100, "da", lista)
    undoList.append(lista)
    lista = rezultat

    # 3. se adauga a doua rezervare
    rezultat = adaugaRezervare("2", "Popescu", "business", 320, "nu", lista)
    undoList.append(lista)
    lista = rezultat

    # 4. se adauga a treia rezervare
    rezultat = adaugaRezervare("3", "Iliescu", "economy plus", 225, "nu", lista)
    undoList.append(lista)
    lista = rezultat

    # 5. se modifica clasa
    rezultat = trecereRezervariClasaSuperioara("Martinescu", lista)
    undoList.append(lista)
    lista = rezultat
    assert getClasa(getById("1", lista)) == "economy plus"

    # 6. primul undo intoarce la clasa originala
    redoList.append(lista)
    lista = undoList.pop()
    assert getClasa(getById("1", lista)) == "economy"

    # 7. se face redo
    undoList.append(lista)
    lista = redoList.pop()
    assert getClasa(getById("1", lista)) == "economy plus"

def testUndoRedoIeftinire():
    # 1. lista goala
    lista = []
    undoList = []
    redoList = []

    # 2. se adauga prima rezervare
    rezultat = adaugaRezervare("1", "Martinescu", "economy", 100, "da", lista)
    undoList.append(lista)
    lista = rezultat

    # 3. se adauga a doua rezervare
    rezultat = adaugaRezervare("2", "Popescu", "business", 120, "nu", lista)
    undoList.append(lista)
    lista = rezultat

    # 4. se adauga a treia rezervare
    rezultat = adaugaRezervare("3", "rezervare3", "economy plus", 125, "nu", lista)
    undoList.append(lista)
    lista = rezultat

    # 5. se aplica ieftinirea
    rezultat = ieftinireRezervari(10, lista)
    undoList.append(lista)
    lista = rezultat
    assert getPret(getById("1", lista)) == 90
    assert getPret(getById("2", lista)) == 120
    assert getPret(getById("3", lista)) == 125

    # 6. primul undo intoarce la pretul original
    redoList.append(lista)
    lista = undoList.pop()
    assert getPret(getById("1", lista)) == 100
    assert getPret(getById("2", lista)) == 120
    assert getPret(getById("3", lista)) == 125

    # 7. se face redo
    undoList.append(lista)
    lista = redoList.pop()
    assert getPret(getById("1", lista)) == 90
    assert getPret(getById("2", lista)) == 120
    assert getPret(getById("3", lista)) == 125


def testUndoRedoOrdonareDupaPret():
    # 1. lista goala
    lista = []
    undoList = []
    redoList = []

    # 2. se adauga prima rezervare
    rezultat = adaugaRezervare("1", "Martinescu", "economy", 100, "da", lista)
    undoList.append(lista)
    lista = rezultat

    # 3. se adauga a doua rezervare
    rezultat = adaugaRezervare("2", "Popescu", "business", 220, "nu", lista)
    undoList.append(lista)
    lista = rezultat

    # 4. se adauga a treia rezervare
    rezultat = adaugaRezervare("3", "Iliescu", "economy plus", 225, "nu", lista)
    undoList.append(lista)
    lista = rezultat

    # 5. se ordoneaza lista
    rezultat = ordonareDescrescatorDupaPret(lista)
    undoList.append(lista)
    lista = rezultat
    assert getId(lista[0]) == "3"
    assert getId(lista[1]) == "2"
    assert getId(lista[2]) == "1"

    # 6. primul undo intoarce la lista originala
    redoList.append(lista)
    lista = undoList.pop()
    assert getId(lista[0]) == "1"
    assert getId(lista[1]) == "2"
    assert getId(lista[2]) == "3"

    # 7. se face redo
    undoList.append(lista)
    lista = redoList.pop()
    assert getId(lista[0]) == "3"
    assert getId(lista[1]) == "2"
    assert getId(lista[2]) == "1"