def creeazaRezervare(id, nume, clasa, pret, checkin):
    '''
    Creeaza un dictionar pentru o rezervare
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :return: dictionarul rezervarii
    '''
    return {
        "id": id,
        "nume": nume,
        "clasa": clasa,
        "pret": pret,
        "checkin": checkin
    }

def getId(rezervare):
    return rezervare["id"]

def getNume(rezervare):
    return rezervare["nume"]

def getClasa(rezervare):
    return rezervare["clasa"]

def getPret(rezervare):
    return rezervare["pret"]

def getCheckin(rezervare):
    return rezervare["checkin"]


def toString(rezervare):
    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin: {}".format(
        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getCheckin(rezervare)

    )