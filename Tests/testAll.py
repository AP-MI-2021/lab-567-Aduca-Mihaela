from Tests.testCRUD import testAdaugaRezervare, testStergeRezervare, testModificaRezervare
from Tests.testDomain import testRezervare


def runAllTests():
    testRezervare()
    testAdaugaRezervare()
    testStergeRezervare()
    testModificaRezervare()