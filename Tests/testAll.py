from Tests.testCRUD import testAdaugaRezervare, testStergeRezervare, testModificaRezervare
from Tests.testDomain import testRezervare
from Tests.testFunctionalitati import testTrecereRezervariClasaSuperioara, testIeftinire, testDeterminarePretMaximClasa, \
    testOrdonareDescrescatoareDupaPret, testSumePentruFiecareNume


def runAllTests():
    testRezervare()
    testAdaugaRezervare()
    testStergeRezervare()
    testModificaRezervare()
    testTrecereRezervariClasaSuperioara()
    testIeftinire()
    testDeterminarePretMaximClasa()
    testOrdonareDescrescatoareDupaPret()
    testSumePentruFiecareNume()



