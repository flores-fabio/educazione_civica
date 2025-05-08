parole_sospette = {
    "shock": 5,
    "incredibile": 4,
    "nessuno lo dice": 5,
    "censurato": 4,
    "clamoroso": 5,
    "scandalo": 4,
    "teoria del complotto": 5,
    "segreto": 4,
    "non vogliono che tu sappia": 5,
    "allarme": 3,
    "bomba": 4,
    "urgente": 4,
    "mai visto": 5,
    "assurdo": 3,
    "mistero": 4,
    "non te lo dicono": 5,
    "cospirazione": 5,
    "manipolazione": 4,
    "agenda nascosta": 5,
    "governo ombra": 5,
    "verità nascosta": 5,
    "bugia dei media": 5,
    "clickbait": 4,
    "bufala": 5,
    "fake": 5
}

parole_affidabili = {
    "fonte": 5,
    "verificato": 5,
    "studio": 4,
    "ricerca": 4,
    "ufficiale": 5,
    "dati": 4,
    "autorizzato": 5,
    "confermato": 5,
    "documentato": 4,
    "esperto": 3,
    "istituto": 4,
    "ministero": 5,
    "organizzazione": 4,
    "scientifico": 5,
    "statistiche": 4,
    "peer-reviewed": 5,
    "analisi": 4,
    "prove": 5,
    "trasparente": 3,
    "fonte attendibile": 5,
    "intervista": 3,
    "pubblicazione": 4,
    "agenzia": 4,
    "ufficio stampa": 4,
    "documento ufficiale": 5
}

def analizza_titolo(titolo):
    parole = titolo.lower().split()
    punteggio = 0

    for parola in parole:
        if parola in parole_sospette:
            punteggio += parole_sospette[parola]
        elif parola in parole_affidabili:
            punteggio += parole_affidabili[parola]

    if punteggio <= -4:
        classificazione = "Probabile fake news"
    elif -3 <= punteggio <= 1:
        classificazione = "Notizia dubbia"
    else:
        classificazione = "Notizia affidabile"

    return punteggio, classificazione

def analizza_lista(titoli):

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
