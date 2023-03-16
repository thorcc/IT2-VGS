# Overskrift - Eks: Vern mot kjøretidsfeil

> 3-4 setninger om hva det er

Når en bruker gjør noe uforutsett i et program, kan det føre til kjøretidsfeil. 
Da er det viktig at programmet håndterer feilen på riktig måte.
I Python kan kjøretidsfeil håndteres med nøkkelordene try og except.
Python forsøker å kjøre kodeblokken som ligger under `try:`, hvis python får en feilmelding, vil den kjøre kodeblokken som ligger under `except:`.

## Eksempler

> Ett eller flere kode- eller bildeeksempler

```python
try:
    alder = int(input("Alder: "))
    fødselsår = 2022 - alder
    print(f"Fødselsår: {fødselsår}")
except:
    print("Feil: alder må være et heltall")

print("koden fortsetter")
```

```python
while True:
    try:
        alder = int(input("Alder: "))
        break
    except:
        print("Alder må være et heltall, prøv igjen")
fødselsår = 2022 - alder
print(f"fødselsår: {fødselsår}")
```

## Bruk i større programmer

> Lenke til Github-repo der du bruker konseptet i et større program

- [Bildegenerator](https://github.com/thorcc/openai-bildegenerator/blob/master/app.py)
