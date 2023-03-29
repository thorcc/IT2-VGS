class Bruker:
    """Superklasse for Brukere i skolesystemet. Skal ikke brukes direkte.

    Attributter:
        epost: En string med brukers epost
        fornavn: En string med brukers fornavn
        etternavn: En string med brukers etternavn
    
    """
    def __init__(self, epost, fornavn, etternavn):
        self.epost = epost
        self.fornavn = fornavn
        self.etternavn = etternavn

    def logg_inn(self):
        print(f"{self.epost} logget inn")

    def logg_ut(self):
        print(f"{self.epost} logget ut")
    
class Lærer(Bruker):
    """Superklasse for Lærere i skolesystemet, arver fra Bruker. Skal ikke brukes direkte.

    Attributter:
        epost: En string med brukers epost
        fornavn: En string med brukers fornavn
        etternavn: En string med brukers etternavn
        lønnskonto: En string med lærerens lønnskonto
    
    """
    def __init__(self, epost, fornavn, etternavn, lønnskonto):
        super().__init__(epost, fornavn, etternavn)
        self.lønnskonto = lønnskonto

class Faglærer(Lærer):
    """Klasse for faglærere, arver fra Lærer.

    Attributter:
        epost: En string med brukers epost
        fornavn: En string med brukers fornavn
        etternavn: En string med brukers etternavn
        lønnskonto: En string med lærerens lønnskonto
    """
    def __init__(self, epost, fornavn, etternavn, lønnskonto):
        super().__init__(epost, fornavn, etternavn, lønnskonto)
        self.kompetanse = []
        self.klasser = []

class Kontaktlærer(Lærer):
    """Klasse for kontaktlærer, arver fra Lærer.

    Attributter:
        epost: En string med brukers epost
        fornavn: En string med brukers fornavn
        etternavn: En string med brukers etternavn
        lønnskonto: En string med lærerens lønnskonto
        klasse: En string med bokstavkoden for lærerens kontaktklasse (eks: STB)
        trinn: En int med klassetrinnet (1-3) for lærerens kontaktklasse
    """
    def __init__(self, epost, fornavn, etternavn, lønnskonto, klasse, trinn):
        super().__init__(epost, fornavn, etternavn, lønnskonto)
        self.klasse = klasse
        self.trinn = trinn

class Elev(Bruker):
    def __init__(self, epost, fornavn, etternavn, trinn, klasse):
        super().__init__(epost, fornavn, etternavn)
        self.trinn = trinn
        self.klasse = klasse
        self.fag = []


if __name__ == "__main__":
# Denne brukes for testing, betyr at koden inne i if-setningen
#  kun kjøres hvis vi "trykker play" på denne filen eller kjører denne fila i terminalen
    lærer1 = Kontaktlærer("navnn@viken.no", "Navn", "Navnesen", 340212314052, "STA", 3)
    lærer1.logg_inn()
    lærer1.logg_ut()
