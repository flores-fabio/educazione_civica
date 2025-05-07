parole_sospette = { # il punteggio delle parole se è più basso sono più sospette
    "shock": -3,
    "incredibile": -2,
    "allarmante": -3,
    "esclusivo": -2,
    "segreto": -2,
    "scandalo": -3,
    "censurato": -2,
    "nessuno lo dice": -3,
    "virus": -2,
    "complotto": -4
}

parole_affidabili = { #Parole con punteggio più elevate sono parole più affidabili
    "fonte": 2,
    "ufficiale": 3,
    "ricerca": 2,
    "studio": 2,
    "dati": 2,
    "esperto": 2,
    "verificato": 3,
    "istituto": 2,
    "scientifico": 3,
    "report": 2
}

def analizza_titolo(titolo):
    """Analizza un titolo e restituisce il punteggio totale e la classificazione"""
    parole = titolo.lower().split()
    punteggio = 0

    # Analisi delle parole
    for parola in parole:
        if parola in parole_sospette:
            punteggio += parole_sospette[parola]
        elif parola in parole_affidabili:
            punteggio += parole_affidabili[parola]

    # Classificazione del punteggio
    if punteggio <= -4:
        classificazione = "Probabile fake news"
    elif -3 <= punteggio <= 1:
        classificazione = "Notizia dubbia"
    else:
        classificazione = "Notizia affidabile"

    return punteggio, classificazione

def analizza_lista(titoli):
    #analizza una lista di titoli
    for titolo in titoli:
        punteggio, classificazione = analizza_titolo(titolo)
        print(f"\nTitolo: {titolo}\nPunteggio: {punteggio} → {classificazione}")


print("FAKE NEWS ANALYZER ")
scelta = input("Vuoi analizzare un titolo o una lista di titoli? (titolo/lista): ")

if scelta == "titolo":
    titolo = input("Inserisci il titolo della notizia: ")
    punteggio, classificazione = analizza_titolo(titolo)
    print(f"\nRisultato: {classificazione} (Punteggio: {punteggio})")
elif scelta == "lista":
    titoli = []
    print("Inserisci i titoli (scrivi 'fine' per terminare):")
    while True:
        t = input("- ")
        if t.lower() == "fine":
            break
        titoli.append(t)
    analizza_lista(titoli)
else:
    print("Scelta non valida.")
