#
# File: esercizio5.py
#
# Author: Matteo Napolano
#
# Date: 2026/07/16
#
# Version: 3.12
#
# Description: Esercizio 5 sulle Regine   
#
#5.1
#Trovare 10 soluzioni per il gioco delle regine con il metodo delle permutazioni: quanto è il tempo medio necessario a trovare una soluzione?
#5.2
#Contare quanti tentativi fa il programma per trovare ogni soluzione del problema 8 regine
#Le righe 46,60,61,63,64,67 servono per il punto 5.2
#5.3
#Alcune soluzioni possono essere ripetute: fare in modo che le soluzioni siano “uniche”
#Le righe 48 e 62 servono per il punto 5.3
#5.4
#Se ci sono soluzioni ripetute, contare quante volte ogni soluzione è ripetuta
#Le righe 62 e 67 servono per il punto 5.4
import random #importa il modulo random
import time #importa il modulo time
def stessa_diagonale(x0, y0, x1, y1):
#essendo che avere la stessa diagonale vuol dire una retta con coefficiente angolare 1 o -1 verifico che dx abbia la stessa dimensione di dy
    dy = abs(y1 - y0)
    dx = abs(x1 - x0) 
    return dx == dy #se sono di dimensione uguale e il loro rapporto è quindi 1 ritorna quel valore    
def incrocia_colonne(posizioni, col) : #la precedente proprietà dev'essere verificata per ogni colonna
    for c in range(col) : #per ogni colonna
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]) : #confronto 2 regine e verifico se sono messe bene dove i valori rappresentano posizione della prima e poi della seconda regina (c colonna e indice di c sarebbe la riga)
            return True #se sono posizionate correttamente la posizione è valida
    return False #se non va bene non restituire il valore
def soluzione_valida(soluzione_posizioni) :
    for col in range(1, len(soluzione_posizioni)) : #verifico che le regine tra di loro siano messe correttamente partendo dalla seconda (da 1 a 8 non da 0 a 8) perchè la prima non può essere confrontata
        if incrocia_colonne(soluzione_posizioni, col) : #se la regina si incrocia con qualcun'altra allora non restituisco la combinazione
            return False 
    return True #se tutte le condizioni sono verificate allora la combinazione è valida
combinazioni_valide = [] #creo una lista per le combinazioni valide
tempi_soluzioni = [] #creo una lista per salvare i tempi che impiega ogni soluzione
def main5_1() :
    random_generator = random.Random() #inizializzo generatore permutazioni
    scacchiera = list(range(8)) #preparo la "possibile soluzione" con posizioni da testare creando la scacchiera quindi scriverò una lista (list) di numeri da 0 a 7 (range)
    soluzioni = 0 #creo una variabile che conterà le soluzioni valide            
    fallimenti = 0 #creo una variabile che conterà le soluzioni non valide
    start_time = time.time() #misuro il tempo impiegato per trovare la soluzione  
    duplicati = {} #creo un dizionario per i duplicati (posso fare anche una lista però sarei limitato perchè se prendessi più di 10 soluzioni mi darebbe un TypeError object non subscritable in quanto la variabile che vorrei non la posso ìnserire nelle quadre)
    while soluzioni < 10 : #finchè non trovo dieci soluzioni
        random_generator.shuffle(scacchiera) #continuo a generare possibili combinazioni da testare mescolando gli indici (shuffle)
        if soluzione_valida(scacchiera) : #se la soluzione generata è valida
            soluzione_prova = str(scacchiera) #scrivo la soluzione come stringa perchè gli elementi potrebbero cambiare
            if soluzione_prova not in combinazioni_valide : #se la soluzione non è tra quelle valide
                tempo_impiegato = time.time() - start_time #tempo impiegato sarà quello finale meno quello iniziale che non sarà sempre 0 perchè se per la prima soluzione impiegno 0.5 secondi, la seconda sarà tempo finale-0.5 sennò non conto il tempo effettivo ma la somma di tutti i tempi)
                tempi_soluzioni.append(tempo_impiegato) #salvo i tempi delle soluzioni che serviranno per calcolare la media 
                print('Soluzione trovata: ',scacchiera, 'in', tempo_impiegato, 's. in', fallimenti, 'tentativi') #se è buona la stampo
                soluzioni += 1 #ogni volta che trovo una combinazione valida incremento il numero delle soluzioni   
                start_time = time.time() #faccio ripartire nuovamente il timer
                combinazioni_valide.append(soluzione_prova) #e inserisco la nuova soluzione valida (evito ripetizioni)
            else: #oppure
                fallimenti += 1 #conta le soluzioni ripetute come un tentativo fallito incrementando di 1
                duplicati[soluzione_prova] = duplicati.get(soluzione_prova,0)+1 #4 #incremmenta di 1 le soluzioni ripetute
        else: #oppure
            fallimenti += 1 #conta i tentativi che vanno male
    tempo_medio = sum(tempi_soluzioni) / len(tempi_soluzioni) #calcolo il tempo medio sommando tutti i tempi delle soluzioni diviso la quantità dei tempi salvati
    print("Tempo medio per trovare una soluzione:", tempo_medio ,"secondi")
    print('Soluzioni ripetute: ', len(duplicati))
if __name__ == "__main__": #serve a far partire il programma principale
    main5_1()
#5.5
#Generalizzare il programma per risolvere una scacchiera di qualunque dimensione NxN
#Le righe nuove o modificate sono la 91 e la 93 e non sevre ripetere le funzioni già scritte ma l'ho fatto per mettere in evidenza che il punto chiedeva una dimensione diversa
def stessa_diagonale(x0, y0, x1, y1) :
#essendo che avere la stessa diagonale vuol dire una retta con coefficiente angolare 1 o -1 verifico che dx abbia la stessa dimensione di dy
    dy = abs(y1 - y0)
    dx = abs(x1 - x0) 
    return dx == dy #se sono di dimensione uguale e il loro rapporto è quindi 1 ritorna quel valore    
def incrocia_colonne(posizioni, col) : #la precedente proprietà dev'essere verificata per ogni colonna
    for c in range(col) : #per ogni coordinata della riga e della colonna (x,y)
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]) : #confronto 2 regine e verifico se sono messe bene dove i valori rappresentano riga e colonna della posizione della prima e poi della seconda regina
            return True #se sono posizionate correttamente la posizione è valida
    return False #se non va bene non restituire il valore
def soluzione_valida(soluzione_posizioni) :
    for col in range(1, len(soluzione_posizioni)) : #verifico che le regine tra di loro siano messe correttamente partendo dalla seconda (da 1 a 8 non da 0 a 8) perchè la prima non può essere confrontata
        if incrocia_colonne(soluzione_posizioni, col) : #se la regina si incrocia con qualcun'altra allora non restituire la combinazione
            return False 
    return True #se tutte le condizioni sono verificate allora la ocmbinazione è valida
combinazioni_valide = [] #creo una lista per le combinazioni valide
tempi_soluzioni = [] #creo una lista per salvare i tempi che impiega ogni soluzione
def main5_5() :
    N = int(input("Inserisci la dimensione della scacchiera (N): ")) #chiedo all'utente la dimensione da mettere (int perchè dev'essere un numero intero)
    random_generator = random.Random() #inizializzo generatore permutazioni
    scacchiera = list(range(N)) #preparo la "possibile soluzione" con posizioni da testare creando la scacchiera quindi scriverò una lista (list) di numeri da 0 a N-1 (range)
    soluzioni = 0 #creo una variabile che conterà le soluzioni valide            
    start_time = time.time() #misuro il tempo impiegato per trovare la soluzione  
    while soluzioni < 10 : #finchè non trovo dieci soluzioni
        random_generator.shuffle(scacchiera) #continuo a generare possibili combinazioni da testare mescolando gli indici (shuffle)
        if soluzione_valida(scacchiera): #se la soluzione generata è valida
            soluzione_prova = str(scacchiera) #scrivo la soluzione come stringa perchè gli elementi potrebbero cambiare
            if soluzione_prova not in combinazioni_valide : #se la soluzione non è tra quelle valide
                tempo_impiegato = time.time() - start_time #tempo impiegato sarà quello finale meno quello iniziale che non sarà sempre 0 perchè se per la prima soluzione impiegno 0.5 secondi, la seconda sarà tempo finale-0.5 sennò non conto il tempo effettivo ma la somma di tutti i tempi)
                tempi_soluzioni.append(tempo_impiegato) #salvo i tempi delle soluzioni che serviranno per calcolare la media 
                print('Soluzione trovata: ',scacchiera) #se è buona lo stampo
                soluzioni += 1 #ogni volta che trovo una combinazione valida incremento il numero delle soluzioni   
                start_time = time.time() #faccio ripartire nuovamente il timer
                combinazioni_valide.append(soluzione_prova) #e inserisco la nuova soluzione valida (evito ripetizioni)
if __name__ == "__main__" : #serve a far partire il programma principale
    main5_5()
#5.6
#Trovare quale è la scacchiera con lato N più grande possibile per cui si riesce a trovare 1 soluzione in meno di 15s
def cerca_singola_soluzione(N) : 
    random_generator = random.Random() #creo un generatore di numeri casuali che userò per mescolare la scacchiera
    scacchiera = list(range(N)) #creo una lista da 0 a N-1 
    start_time = time.time() #misuro il tempo impiegato per trovare la soluzione  
    while True : #finchè non trovo una soluzione_valida
        random_generator.shuffle(scacchiera) #continuo a generare combinazioni casuali 
        if soluzione_valida(scacchiera) : #se la soluzione è valida
            tempo_impiegato = time.time() - start_time #tempo impiegato sarà quello finale meno quello iniziale che non sarà sempre 0 perchè se per la prima soluzione impiegno 0.5 secondi, la seconda sarà tempo finale-0.5 sennò non conto il tempo effettivo ma la somma di tutti i tempi)
            return tempo_impiegato #restituisco il tempo impiegato
def main5_6() :    
    N = 4 #parto da 4 perchè è la più piccola scacchiera che mi da soluzioni
    ultimo_N_valido = None #creo una variabile inizialmente vuota (None) che mi dica chi è l'ultimo N valido
    ultimo_tempo = 0 #e ne creo una per il tempo
    while True : #finchè non trovo la dimensione più grande che fornisce 1 soluzione in meno di 15 secondi 
        tempo = cerca_singola_soluzione(N) #creo una variabile che cerca la soluzione per la dimensione
        print('Test su scacchiera', N,'x',N,'Risolta in',tempo ,'secondi.')
        if tempo < 15: #se il tempo è meno di 15 secondi
            ultimo_N_valido = N #la dimensione valida sarà l'ultima
            ultimo_tempo = tempo #il tempo valido sarà l'ultimo
            N += 1  # provo ad aumentare la dimensione finchè la condizione è verificata 
        else: #oppure
            print('La dimensione N massima risolvibile sotto i 15 secondi è: N = ',ultimo_N_valido) #stampa l'N finale
            print('Tempo impiegato per N=',ultimo_N_valido,':' ,ultimo_tempo,': s.') #stampa il suo tempo
            break #bisogna chiudere l'else sennò fa un loop
if __name__ == "__main__" : #come prima chiamo il main
    main5_6()  #attenzione che i main hanno nomi diversi per evitare di avere dei KeyError e quindi per usare il main corretto
#!Ogni volta la dimensione che avvio il programma varia per come è costruito il programma (in genere N>15)!
#5.7
#Ogni soluzione è ‘simmetrica’ per rotazioni della scacchiera 8x8 di 90, 180 e 270 gradi. Scrivere delle funzioni che, una volta trovata una soluzione alla scacchiera, costruiscano le 4 soluzioni simmetriche per rotazione. Trovate 5 soluzioni “uniche” e le rispettive soluzioni simmetriche per rotazione per una scacchiera 8x8
def ruota_90(soluzione) :
    N = len(soluzione)
    nuova = [0 for i in range(N)] #creo una lista di 0 e la ripeto N-1 volte 
    for col in range(N) : #per le colonne di N dimensione
        riga = soluzione[col] #chiamo l'elemento della colonna della soluzione, riga
        nuova[N - 1 - riga] = col #posiziono la colonna nella riga corrispondente
    return nuova #restituisco la nuova soluzione
def ruota_180(soluzione) : #qui ribalto completamente la scacchiera
    N = len(soluzione)
    nuova = [0 for i in range(N)] #creo una lista di 0 e la ripeto N-1 volte 
    for col in range(N): #per le colonne di N dimensione
        riga = soluzione[col] #chiamo l'elemento della colonna della soluzione riga
        nuova[N - 1 - col] = N - 1 - riga #posiziono la riga nella colonna corrispondente
    return nuova #restituisci la nuova soluzione
def ruota_270(soluzione) :
    N = len(soluzione)
    nuova = [0 for i in range(N)] #creo una lista di 0 e la ripeto N volte 
    for col in range(N) : #per le colonne di N dimensione
        riga = soluzione[col] #chiamo l'elemento della colonna della soluzione 'riga'
        nuova[riga] = N - 1 - col  #posiziono la colonna nella riga corrispondente
    return nuova #restituisco la nuova soluzione
def main5_7() :
    soluzioni = 0 #creo una variabile che stabilirà il numero delle soluzioni valide trovate   
    scacchiera = list(range(8)) #preparo la "possibile soluzione" creando la scacchiera (lista da 0 a 8)
    N = len(scacchiera)
    random_generator = random.Random() #inizializzo generatore permutazioni
    duplicati = {} #creo un dizionario per i duplicati         
    while soluzioni < 5 : #finchè le soluioni sono meno di 5
        random_generator.shuffle(scacchiera) #continuo a mescolare le posizioni
        if soluzione_valida(scacchiera) : #se ho la soluzione valida della scacchiera
            soluzione_prova = str(scacchiera) #scrivo la soluzione come stringa per poterla memorizzare
            soluzioni += 1 #incremento il numero di soluzioni uniche trovate
            print('Soluzioni uniche: ',soluzioni)
            print('Soluzione originale (0°): ', scacchiera,)
            print('Soluzione ruotata (90°):  ', ruota_90(scacchiera))                
            print('Soluzione ruotata (180°): ', ruota_180(scacchiera))
            print('Soluzione ruotata (270°): ', ruota_270(scacchiera))                
            combinazioni_valide.append(soluzione_prova) #inserisco la nuova soluzione valida                                
        else : #oppure
            pass 
if __name__ == "__main__" : 
    main5_7()
#Per fare prima meglio commentare il punto 5.6 per verificare gli altri esercizi
#giusto l'ultimo punto?