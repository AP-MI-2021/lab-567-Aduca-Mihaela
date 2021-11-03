from Domain.rezervare import creeazaRezervare, getId, getNume, getClasa, getPret, getCheckin


def testRezervare():
    rezervare = creeazaRezervare("1", "Martinescu", "economy", 350, "da")
    assert getId(rezervare) == "1"
    assert getNume(rezervare) == "Martinescu"
    assert getClasa(rezervare) == "economy"
    assert getPret(rezervare) == 350
    assert getCheckin(rezervare) == "da"