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

#### Presentere data

- Grafer i Python
- Nettsider (Flask/Svelte(?))
- Kart

### Vern mot kjøretidsfeil og logiske feil i programmer

#### Kjøretidsfeil

- Håndtering av feil med `try` og `except`

#### Logiske feil

- Testing med `assert`


## Vurderingskriterier

| Kategori           | Lav kompetanse (2)                                                       | God kompetanse (4)                                                                         | Utmerket kompetanse (6)                                                      |
| ------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
|                    |
| **Implementering** | implementerer enkle løsninger med programmering                          | implementerer sammensatte løsninger med programmering                                      | implementerer avanserte løsninger med programmering                          |
|                    | bruker hensiktsmessig gjenbrukbar kode                                   | bruker og tilpasser hensiktsmessig gjenbrukbar kode                                        | bruker, tilpasser og utvikler hensiktsmessig gjenbrukbar kode                |
|                    | innhenter datasett og presenterer enkle data fra disse med programmering | bearbeider datasett, gjør enkle analyser av dataene og presenterer disse med programmering | gjør sammensatte analyser av datasett og presenterer disse med programmering |
|                    | implementerer kode uten syntaksfeil                                      | ivaretar vern mot kjøretidsfeil og logiske feil i enkle og sammensatte programmer          | ivaretar vern mot kjøretidsfeil og logiske feil i avanserte programmer       |


