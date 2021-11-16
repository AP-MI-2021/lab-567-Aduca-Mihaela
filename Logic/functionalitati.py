from copy import deepcopy

from Domain.rezervare import getNume, getClasa, creeazaRezervare, getId, getPret, getCheckin


def trecereRezervariClasaSuperioara(numeCitit, lista):
    '''
    trece totalitatea rezervarilor facute pe un nume citit, la o clasa superioara
    :param numeCitit: string
    :param lista: lista de rezervari
    :return:
    '''
    listaNoua = []
    for rezervare in lista:
        if numeCitit == getNume(rezervare):
            if getClasa(rezervare) == "economy":
                rezervareNoua = creeazaRezervare(
                    getId(rezervare),
                    getNume(rezervare),
                    "economy plus",
                    getPret(rezervare),
                    getCheckin(rezervare)
                )
                listaNoua.append(rezervareNoua)
            elif getClasa(rezervare) == "economy plus":
                    rezervareNoua = creeazaRezervare(
                        getId(rezervare),
                        getNume(rezervare),
                        "business",
                        getPret(rezervare),
                        getCheckin(rezervare)
                    )
                    listaNoua.append(rezervareNoua)
            else:
                rezervareNoua = creeazaRezervare(
                    getId(rezervare),
                    getNume(rezervare),
                    getClasa(rezervare),
                    getPret(rezervare),
                    getCheckin(rezervare)
                )
                listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua

def ieftinireRezervari(procentaj, lista):
    '''
    Ieftineste rezervarile care au checkin-ul facut cu un procentaj dat
    :param procentaj: procentajul dat
    :param lista: o lista de rezervari
    :return: lista dupa ieftinire
    '''
    if procentaj > 100:
        raise ValueError("Nu se pot face modificari cu un procentaj peste 100!")
    if procentaj < 0:
        raise ValueError("Nu se pot afce modificari cu un procentaj sub 0!")
    listaNoua = []
    for rezervare in lista:
        if getCheckin(rezervare) == "da":
            rezervareNoua = creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                getClasa(rezervare),
                getPret(rezervare) - (procentaj/100*getPret(rezervare)),
                getCheckin(rezervare)
            )
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua


def determinarePretMaximClasa(lista):
    '''
    Determinarea pretului maxim pentru fiecare clasa.
    :param lista: lista de rezervari
    :return: returneaza pretul maxim
    '''

    pretMaxEconomy = 0
    pretMaxEconomyPlus = 0
    pretMaxBusiness = 0

    for rezervare in lista:
        if getClasa(rezervare) == "economy" and getPret(rezervare) > pretMaxEconomy:
            pretMaxEconomy = getPret(rezervare)
        elif getClasa(rezervare) == "economy plus" and getPret(rezervare) > pretMaxEconomyPlus:
            pretMaxEconomyPlus = getPret(rezervare)
        elif getClasa(rezervare) == "business" and getPret(rezervare) > pretMaxBusiness:
            pretMaxBusiness = getPret(rezervare)

    return pretMaxEconomy, pretMaxEconomyPlus, pretMaxBusiness


def ordonareDescrescatorDupaPret(lista):
    '''
    Ordoneaza rezervarile descrescator dupa pret.
    :param lista: o lista de rezervari
    :return: o noua lista, dupa ordonare
    '''
    listaNoua = []
    listaNoua = deepcopy (lista)
    for i in range(0, len(listaNoua) - 1):
        for j in range(i + 1, len(listaNoua)):

            if getPret(listaNoua[i]) < getPret(listaNoua[j]):
                aux = listaNoua[j]
                listaNoua[j] = listaNoua[i]
                listaNoua[i] = aux
    return listaNoua

def sumePentruFiecareNume(lista):
    '''
    Afiseaza suma preturilor pentru fiecare nume.
    :param lista: o lista de rezervari
    :return: suma preturilor pentru fiecare nume
    '''
    preturi  = {}

    for rezervare in lista:
        nume = getNume(rezervare)
        pret = getPret(rezervare)
        if nume in preturi:
            preturi[nume] = preturi[nume] + pret
        else:
            preturi[nume] = pret
    return preturi