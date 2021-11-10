from Domain.rezervare import getClasa, getPret, getId, getNume
from Logic.CRUD import adaugaRezervare
from Logic.functionalitati import trecereRezervariClasaSuperioara, ieftinireRezervari, determinarePretMaximClasa, \
    ordonareDescrescatorDupaPret, sumePentruFiecareNume


def testTrecereRezervariClasaSuperioara():
    lista = []
    lista = adaugaRezervare("1", "Martinescu", "economy", 350, "da", lista)
    lista = adaugaRezervare("2", "Popescu", "economy plus", 100 , "da", lista)
    lista = adaugaRezervare("3", "Irimescu", "business", 250, "da", lista)
    lista = trecereRezervariClasaSuperioara("Popescu", lista)

    assert getClasa(lista[0]) == "economy plus"
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
    lista = sumePentruFiecareNume(lista)
    assert getNume(lista[0]) == 350
    assert getNume(lista[1]) == 100
testSumePentruFiecareNume()

