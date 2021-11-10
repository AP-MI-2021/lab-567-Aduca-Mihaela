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
    for i in range(0, len(lista)):
        for j in range(i, len(lista)):
            pretCurent = getPret(lista[i])
            pretUrmator = getPret(lista[j])
            if pretUrmator > pretCurent:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

def sumePentruFiecareNume(lista):
    preturi  = {}
    for rezervare in lista:
        nume = getNume(rezervare)
        pret = getPret(rezervare)
        if nume in preturi:
            preturi[nume]  = preturi[nume] + float(pret)
        else:
            preturi[nume] = float(pret)
    return preturi