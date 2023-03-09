# Implementering

## Prosjektforslag

- Hente data fra et API, bearbeide det med Python og presentere det på en nettside med Flask og HTML
- [En liste med gratis API-er (https://github.com/public-apis/public-apis)](https://github.com/public-apis/public-apis)
- Eksempel: En værapp som henter værdata fra [https://api.met.no/](https://api.met.no/) sitt API

## Innhold
  
### Løsninger med programmering

- Python
- Javascript(?)

### Gjenbrukbar kode

- Dokumentasjon av kode med Docstrings
  - https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings
- Funksjoner med dokumentasjon
- Klasser med dokumentasjon

### Innhente, analysere og presentere data

**Gjøremål:**

1. Les [Aunivers: 3A Tegning av grafer](https://aunivers.no/fagpakker/realfag/informasjonsteknologi-1-2/it-2/3-databehandling/3a-tegning-av-grafer?nof=1) og gjør oppgave 1 - 16 (alle)
2. Lag en notat om hvordan plotting fungerer i Python, ta med minst to kodeeksempler. Notatet skal legges i IT2-mappen.
   - Tips: Lag tabeller i markdown med [https://www.tablesgenerator.com/markdown_tables](https://www.tablesgenerator.com/markdown_tables) 
3. Les [Aunivers: 3B Reelle datasett](https://aunivers.no/fagpakker/realfag/informasjonsteknologi-1-2/it-2/3-databehandling/3b-reelle-datasett) og gjør oppgave 1 - 13 (alle)
4. Lag en notat om hvordan innhenting av data fungerer i Python, ta med minst to kodeeksempler. Notatet skal legges i IT2-mappen.
5. Bonus: [Aunivers: Eksempel: API-er](https://aunivers.no/fagpakker/realfag/informasjonsteknologi-1-2/it-2/3-databehandling/eksempel-api-er)
6. Bonus: [Aunivers: Eksempel: Kart og data](https://aunivers.no/fagpakker/realfag/informasjonsteknologi-1-2/it-2/3-databehandling/eksempel-kart-og-data)

#### Tegne grafer (presentere data)

I Python kan vi bruke biblioteket `matplotlib` til å tegne grafer.
`matplotlib` må installeres med `pip`, slik:

windows:
```bash
pip install matplotlib
```

mac:
```bash
pip3 install matplotlib
```

Eksempel: et enkelt plott  

```python
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [10, 20, 25, 10, 12]

plt.plot(x, y)  # oppretter graf
plt.show()      # viser graf
```

#### Innhente data

- Lese data fra fil

````python
# Lese data fra json-fil
import json
fil = open("data.json")
data = json.load(fil)
fil.close()
````

- Hente data fra API


````python
# Hente data fra API
import requests

respons = requests.get("https://eksempel.no")
data = respons.json()
````

#### Analysere data

- Hente ut relevant informasjon fra data
- Sortere og filtrere data
- ++

> Mye frihet her


### Vern mot kjøretidsfeil og logiske feil i programmer

#### Kjøretidsfeil

- Håndtering av feil med `try` og `except`

```python
print("Velkommen til Valutakalkulatoren")

# hvis kodeblokken under try gir en feilmelding, kjøres koden under except
try:
  euro = float(input("€: "))
  dollar = euro * 1.07
  print(f"{euro}€ = ${dollar}")
except:
  print("FEIL: Ukjent input")
```

```python
# tips: en kombinasjon av en while-løkke og try-except 
#       kan brukes for å få riktig brukerinput
while True:
    try:
        alder = int(input("din alder: "))
        break
    except:
        print("alder må være et heltall, prøv igjen")

fødselsår = 2022 - alder
print(f"du er født i {fødselsår}")
```

#### Logiske feil

- [Testing med `assert`](https://www.w3schools.com/python/ref_keyword_assert.asp)

```python
def areal(h,b):
  return h*b

def omkrets(h,b):
  return h+h+b

# hvis testen er True, fortsetter koden
assert areal(2,3) == 6

# hvis testen er False, kommer en AssertionError feilmelding:
assert omkrets(2,3) == 10
```


- [Enhetstesting med Unittest-biblioteket](https://docs.python.org/3/library/unittest.html)

```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```


## Vurderingskriterier

| Kategori           | Lav kompetanse (2)                                                       | God kompetanse (4)                                                                         | Utmerket kompetanse (6)                                                      |
| ------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
|                    |
| **Implementering** | implementerer enkle løsninger med programmering                          | implementerer sammensatte løsninger med programmering                                      | implementerer avanserte løsninger med programmering                          |
|                    | bruker hensiktsmessig gjenbrukbar kode                                   | bruker og tilpasser hensiktsmessig gjenbrukbar kode                                        | bruker, tilpasser og utvikler hensiktsmessig gjenbrukbar kode                |
|                    | innhenter datasett og presenterer enkle data fra disse med programmering | bearbeider datasett, gjør enkle analyser av dataene og presenterer disse med programmering | gjør sammensatte analyser av datasett og presenterer disse med programmering |
|                    | implementerer kode uten syntaksfeil                                      | ivaretar vern mot kjøretidsfeil og logiske feil i enkle og sammensatte programmer          | ivaretar vern mot kjøretidsfeil og logiske feil i avanserte programmer       |


