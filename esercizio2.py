#
# File: esercizio2.py
#
# Author: Matteo Napolano
#
# Date: 2026/07/14
#
# Version: 3.12
#
# Description: Esercizio 2 sui Data Containers 
#
testo = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
'''
#2.1
#Conta le righe non vuote che compongono l’estratto
caratteri = list(testo) #creo una lista con tutti gli elementi che compongono il testo
print(testo.split('\n')) #divido il testo in righe usando '\n' che è il simbolo per andare a capo
frasi = testo.split('\n')  #chiamo frasi il testo diviso
#siccome nelle frasi ho ancora le righe vuote uso un ciclo while
while '' in frasi : #finchè ho le righe vuote nelle frasi
    frasi.remove('') #rimuovo gli elementi vuoti 
print('Righe non vuote: ', len(frasi)) #stampa stringa con numero righe non vuote
#l'unico print utile in questo esercizio è il secondo, l'altro serve solo a capire cosa succede
#2.2 
#Contate le parole che compongono l’estratto
numero_parole = [] #creo una lista inizialmente vuota per le parole
for riga in frasi : #per le frasi dentro la lista delle frasi
    parole = riga.split('\n') #divido le frasi in parole usando '\n' che è il simbolo dello spazio
    if len(parole) != 0 : #se la lunghezza è diversa da 0, cioè se ho uno spazio vuoto
        numero_parole.append(riga) #restituisco il risultato ottenuto e lo aggiungo alla lista
print(testo.split()) #stampa la lista delle parole (FACOLTATIVO) 
print('Parole del testo: ', len(testo.split())) #stampa il numero di parole
#2.3
#Conta i caratteri alfanumerici che compongono l’estratto
numero_caratteri = [] #creo una lista vuota per i caratteri
for carattere in caratteri : #per i caratteri nella lista dei caratteri
    if carattere != " " and carattere != "\n" and carattere != "," and carattere != "." and carattere != "-" and carattere != "!" and carattere != ";" and carattere != "'" and carattere != ":" : #se trovo un carattere diverso da uno di questi 
        numero_caratteri.append(carattere) #lo aggiungo alla lista numero_caratteri
print('Caratteri: ', numero_caratteri) #stampo lista numero caratteri (FACOLTATIVO)
print('Caratteri: ', len(numero_caratteri)) #stampo numero caratteri
#2.4
#Chiedere all’utente una lettera e contate quante volte compare nel testo
lettera_scelta = input('Quale lettera vuoi contare? ') #creo una variabile che sarà la scelta della lettera dell'utente
if lettera_scelta != " " and lettera_scelta != "\n" and lettera_scelta != "," and lettera_scelta != "." and lettera_scelta != "-" and lettera_scelta != "!" and lettera_scelta != ";" and lettera_scelta != "'" : #se la scelta è una lettera (non un carattere speciale)
    quanta_lettera = [] #creo una lista che conterrà la lettera ripetuta un certo numero di volte
    for carattere in caratteri : #per ogni carattere dei caratteri
        if carattere.lower() == lettera_scelta.lower(): #se il carattere è una lettera maiuascols e corrisponde a una lettera minuscola presente lo trasformo in minuscolo.Questo lo faccio perchè devo tenere conto di maiuscole e minuscole in quanto io so che sono lo stesso carattere ma per Python sono diversi
            quanta_lettera.append(carattere) #quelli che verificano la condizione li aggiungo alla lista quanta_lettera
    print('La lettera compare: ', len(quanta_lettera) ,'volte') #stampo le stringhe con la lunghezza della lista che mi darà il numero di volte in cui la lettera si ripete
#2.5
#Sostituisci tutte le parole day, water e about con la parola PYTHON in tutti i versi
parole = testo.split() #ridefinisco parole perchè sennò il programma considera "parole" del punto 2.2 che fa una cosa diversa a quella che mi serve
x=0 #prendo una x che stabilisca gli indici della lista
for parola in parole : #delle parole nel testo diviso in parole
    if  "day" in parola.lower() or "water" in parola.lower() or "about" in parola.lower() : #se trovo day,water o about, maiuscoli o minuscoli che siano (.lower)
         parole[x] = 'PYTHON' #sostituisci la parola di quell'indice con PYTHON
    x = x + 1 #confronta la parola successiva
print(parole) #stampa il testo diviso in parole aggiornato
#!Tutti i punti che seguono si baseranno sul testo iniziale e non su quello modificato col punto 2.5!
#2.6
#Riscrivere il testo in modo che tutte le parole in posizione dispari siano scritte in maiuscolo
def trasformare_testo(testo) : 
    lista_parole = testo.split() #chiamo lista_parole il testo diviso 
    for i in range(len(lista_parole) ): #per ogni parola della lista  
        if i % 2 == 1 : #se l'indice è dispari 
            lista_parole[i] = lista_parole[i].upper() #scrivo le parole tutte in maiuscolo
    return " ".join(lista_parole) #restituisco le parole unite e quindi anzichè avere la lista di parole divise, ho il testo
testo_modificato = trasformare_testo(testo) #definisco il testo modificato come il testo con le parole aggiornate  
print(testo_modificato) #stampa il testo modificato
#2.7
#Riscrivere il testo invertendo l’ordine delle frasi dal basso all’alto.
def riscrivi_testo(testo) :
    frasi_ordinate = [] #creo una lista contenente le frasi ordinate
    for frase in frasi : #per ogni frase delle frasi
        if len(frase) > 0 : #se la frase non è vuota 
            frasi_ordinate.append(frase) #la aggiungo alle frasi
    frasi_ordinate.reverse() #inverto l'ordine dall'ultima frase alla prima
    return "\n".join(frasi_ordinate) #metto le frasi invertite in un unico testo
testo_modificato = riscrivi_testo(testo) #chiamo "testo_modificato" il testo con applicata la funzione "riscrivi_testo"
print(testo_modificato) #stampo il testo_modificato
#2.8
#Riscrivere il testo in modo che il secondo verso di ogni strofa sia scritto a specchio (cioè al contrario carattere per carattere: Ad esempio, questa frase’ –> ‘esarf atseuq ,oipmese dA’)
def testo_specchiato(testo) :
    caratteri.reverse() #inverto l'ordine andando dall'ultimo carattere al primo
    return "".join(caratteri) #metto i caratteri invertiti in un unico testo
testo_modificato = testo_specchiato(testo) #chiamo "testo_modificato" il testo con applicata la funzione "testo_specchia"
print(testo_modificato) #stampo il test_modificato
#2.9
#Trova eventuali parole che compaiono in tutte le strofe
for i in [",", ".", "!", ";", "'"] : #per ogni carattere tra quelli della lista
    while i in caratteri : #finchè i è un carattere speciale 
        caratteri.remove(i) #lo rimuovo
testo_pulito = "".join(caratteri) #ricompongo il testo coi caratteri rimasti
strofe_complete = testo_pulito.split("\n\n") #divido il testo ogni volta che c'è uno spazio vuoto (un "\n" per andare a capo e uno per la riga vuota)
strofe = [] #creo una lista che avrà le strofe senza spazi vuoti
for s in strofe_complete : #per s nelle strofe_complete 
    if len(s.strip()) > 0 : #se la lunghezza di s non è 0 o meno, allora cancello le strofe vuote perchè con strip elimino gli spazi e gli 'a capo' 
        strofe.append(s) #aggiungo alla lista delle strofe quelle non vuote
#scrivo le strofe come liste di parole
s1 = strofe[0].split() #prendo la strofa nella prima posizione della lista "strofe" e la divido in parole
s2 = strofe[1].split()
s3 = strofe[2].split()
s4 = strofe[3].split()
parole_comuni = set(s1).intersection(s2, s3, s4) #trasformo lista in un insieme per evitare ripetizioni all'interno della stessa lista e la interseco alle altre 
print('Parole comuni: ' , list(parole_comuni)) #stampo la lista con le parole comuni
#2.10
#Crea la lista univoca di tutte le parole che compaiono nel testo, ordinala per lunghezza delle parole e visualizzala
testo_1 = testo.lower() #creo un testo con le parole tutte minuscole così da evitare il problema delle maiuscole e minuscole
parole = testo_1.split() #creo una lista di queste parole
parole_pulite = [parola.strip(",").strip(".").strip(":").strip("!") for parola in parole] #rimuovo con strip tutti i caratteri speciali uno alla volta (tranne - e ' che ho considerato fossero parte della parola) per considerare la lunghezza effettiva (se mettessi and o or non funzionerebbe perchè guarderebbe solo la prima condizione (and) o la prima vera (or))
parole_univoche_set = set(parole_pulite) #creo prima un set per togliere in modo da togliere i duplicati e ottrnere subito le parole univoche
parole_univoche_lista= list(parole_univoche_set) #rendo il set una lista in quanto gli elementi del set non è ordinato e quindi non posso riordinare gli elementi alll'interno
parole_univoche_lista.sort(key = len , reverse = True) #con sort riordino la lista in ordine crescente sulla base della caratteristica che scelgo.Qui la caratteristica è la lunghezza (key=len) e essendo che se faccio il print, con sort le parole sono dalla più breve alla più lunga, uso reverse e le riscrivo al contrario per ottenere l'ordine desiderato
print(parole_univoche_lista) #visualizzo la lista
#2.11
#Crea un dizionario che mappi OGNI carattere (chiave) con la sua occorrenza nel testo (valore) e visualizzatelo
caratteri_dizionario = {} #creo un dizionario vuoto che conterrà gli elementi del dizionario
for carattere in testo : #controllo ogni carattere nel testo
    if carattere in caratteri_dizionario : #se il carattere nel dizionario
        caratteri_dizionario[carattere] += 1 #incremento di 1 il numero di elementi del dizionario (a+=1 equivale a a=a+1) 
    else :
        caratteri_dizionario[carattere] = 1 #se invece è la prima volta che lo vedo gli associo il valore 1 
print(caratteri_dizionario) #visualizzo il dizionario finale
#!Le chiavi sono uniche però i valori si ripetono.In un dizionario è importante l'unicità delle chiavi e non dei valori!
#2.12
#Create un dizionario come il precedente per i soli caratteri alfanumerici (no caratteri speciali), ignorando maiuscole e minuscole
caratteri_alfanumerici_dizionario = {} #creo un dizionario vuoto che conterrà gli elementi del dizionario
for carattere in numero_caratteri : #controllo ogni carattere nei caratteri alfanumerici(questi caratteri si trovano in numero_caratteri per l'esercizio 2.3)
    if carattere in caratteri_alfanumerici_dizionario : #se il carattere alfanumerico è nel dizionario
        caratteri_alfanumerici_dizionario[carattere] += 1 #incremento di 1 il numero di elementi del dizionario (a+=1 equivale a a=a+1) 
    else:
        caratteri_alfanumerici_dizionario[carattere] = 1 #se invece è la prima volta che lo vedo gli associo la chiave 1 
print(caratteri_alfanumerici_dizionario) #visualizzo il dizionario finale