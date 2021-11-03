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
                        "bussines",
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