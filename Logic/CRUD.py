from Domain.rezervare import creeazaRezervare, getId


def adaugaRezervare(id, nume, clasa, pret, checkin,  lista):
    '''
    adauga o rezervare intr-o lista
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :param lista: lista de rezervari
    :return: o lista continand vechile rezervari si noua rezervare.
    '''
    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    if clasa != "economy" and clasa != "economy plus" and clasa != "business":
        raise ValueError("Clasele posibile sunt economy, economy plus si business!")
    if pret < 0:
        raise ValueError("Pretul nu poate fi negativ!")
    if checkin != "da" and checkin != "nu":
        raise ValueError("Checkin-ul poate sa aiba doar valorile da sau nu!")
    rezervare = creeazaRezervare(id, nume, clasa, pret, checkin)
    return lista + [rezervare]

def getById(id, lista):
    '''
    da elementul din lista cu un id dat
    :param id: string
    :param lista: lista de rezervari
    :return: rezervarea care are id-ul dat sau None, daca nu exista
    '''

    for rezervare in lista:
        if getId(rezervare) == id:
            return rezervare
    return None

def stergeRezervare(id, lista):
    '''
    sterge rezervarea cu id-ul dat dintr-o lista
    :param id: string
    :param lista: lista de rezervari
    :return:
    '''
    if getById(id, lista) is None:
        raise ValueError("Rezervarea cu acest id nu exista!")
    return [rezervare for rezervare in lista if getId(rezervare) != id]

def modificaRezervare(id, nume, clasa, pret, checkin,  lista):
    '''
    modifica o rezervare cu un id dat
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :param lista: lista de rezervari
    :return:
    '''
    if getById(id, lista) is None:
        raise ValueError("Rezervarea cu acest id nu exista!")
    if clasa != "economy" and clasa != "economy plus" and clasa != "business":
        raise ValueError("Clasele posibile sunt economy, economy plus si business!")
    if pret < 0:
        raise ValueError("Pretul nu poate fi negativ!")
    if checkin != "da" and checkin != "nu":
        raise ValueError("Checkin-ul poate sa aiba doar valorile da sau nu!")
    listaNoua = []
    for rezervare in lista:
        if getId(rezervare) == id:
            rezervareNoua = creeazaRezervare(id, nume, clasa, pret, checkin)
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua