from Domain.rezervare import getId, getNume, getClasa, getPret, getCheckin
from Logic.CRUD import adaugaRezervare, getById, stergeRezervare, modificaRezervare


def testAdaugaRezervare():
    lista = []
    lista = adaugaRezervare("1", "Martinescu", "economy", 350, "da", lista)

    assert getId(getById("1", lista)) == "1"
    assert getNume(getById("1", lista)) == "Martinescu"
    assert getClasa(getById("1", lista)) == "economy"
    assert getPret(getById("1", lista)) == 350
    assert getCheckin(getById("1", lista)) == "da"


def testStergeRezervare():
    lista = []
    lista = adaugaRezervare("1", "Martinescu", "economy", 350, "da", lista)
    lista = adaugaRezervare("2", "Popescu", "bussines", 300, "nu", lista)

    lista = stergeRezervare("1", lista)
    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

    lista = stergeRezervare("3", lista)
    assert len(lista) == 1
    assert getById("2", lista) is not None


def testModificaRezervare():
    lista = []
    lista = adaugaRezervare("1", "Martinescu", "economy", 350, "da", lista)
    lista = adaugaRezervare("2", "Popescu", "bussines", 300, "nu", lista)

    lista = modificaRezervare("1", "Irimescu", "economy plus", 200, "da", lista)
    rezervareUpdatata = getById("1", lista)
    assert getId(rezervareUpdatata) == "1"
    assert getNume(rezervareUpdatata) == "Irimescu"
    assert getClasa(rezervareUpdatata) == "economy plus"
    assert getPret(rezervareUpdatata) == 200
    assert getCheckin(rezervareUpdatata) == "da"

    rezervareNeupdatata = getById("2", lista)
    assert getId(rezervareNeupdatata) == "2"
    assert getNume(rezervareNeupdatata) == "Popescu"
    assert getClasa(rezervareNeupdatata) == "bussines"
    assert getPret(rezervareNeupdatata) == 300
    assert getCheckin(rezervareNeupdatata) == "nu"