#
# File: esercizio1.py
#
# Author: Matteo Napolano
#
# Date: 2026/07/13
#
# Version: 3.12
#
# Description: Esercizio 1 
#
#1.1:
#Scrivere una funzione di controllo, is_pari(n), che accetti come parametro un numero intero e restituisca True se il numero è pari, False altrimenti.
def is_pari(n) : #definisco la funzione is_pari che ha come parametro n
    for k in range(n+1) : #per k che va da 1 a n+1 visto che python conta da 0, faccio un giro e verifica che il mio numero corrisponda a 2k
        if n == 2 * k : #se corrisponde a 2k (def numero pari) allora restituisco il valore come vero
            return True         
    return False #altrimenti restituisco falso (va scritto fuori dal ciclo perchè una volta che il programma finisce il giro senza aver ottenuto la condizione dell'if allora avrò il valore come falso e quindi sarà dispari)
#se metto print(is_pari(n)) fuori dalla funzione si può verificare
#1.2
#Crea una funzione di generazione che chieda all’utente un numero intero positivo e lo restituisca come risultato della funzione. Se l’utente inserisce un numero non valido (es. negativo o zero), il ciclo deve continuare a richiederlo finché l’input non è corretto.
def number_generator() : 
    while True : #finchè la condizione è vera
        n = int(input('Inserisci un numero: ')) #chiamo n il numero intero (int) che metto nel terminale (input) dove mi apparirà la stringa inserisci un numero.Metto uno spazio per avere una forma più ordinata nel terminale
        if n > 0 : #voglio che il numero sia strettamente positivo quindi se accade ridammi il numero 
            return n            
        else :
            print('Numero non valido!Inseriscine un altro: ') #se la condizione non è vera il programma continua a farmi inserire numeri sul terminale fino a che non scrivo un numero strettamente positivo
#number_generator() per verificare la validità 
#1.3
#Scrivere una funzione che usando il numero scelto dall’utente, generi una lista seguendo questa regola: se il numero è pari, va diviso per 2; se è dispari, va moltiplicato per 3 e aggiunto 1. Il processo va ripetuto finchè si arriva a 1 o la lista abbia piu’ di 100 numeri
def math_pari_dispari(n):
    lista_numeri=[n] #creo una lista su cui poi verranno messi i numeri 
    while n != 1 and len(lista_numeri) < 100 : #finchè n diverso da 1 e la lista non ha 100 o più numeri segui la condizione.Inoltre si usa and e non or perchè in python or si ferma alla prima condizione valida senza valutare la seconda, mentre l'and controlla che entrambe siano verificate
        k = n//2 #definisci k come n/2 ricordando che // si usa perchè cerco numeri interi 
        if n == 2 * k : #se n è un numero pari
            n = n//2 #dimezzalo
        else :
            n = (n * 3) + 1 #se dispari moltiplica per 3 e aggiungi 1 
        lista_numeri.append(n) #il numero trovato lo inserisco nella lista
    return lista_numeri #alla fine mi ritorna la lista con il numero iniziale e quello ottenuto
#il ciclo continua fin quando n è diverso da 1 e la lista arriva a 100 numeri 
#mettendo print(math_pari_dispari(n)) verifico che la funzione sia corretta
#1.4
#Scrivete una funzione analizza_sequenza(lista) che riceva la lista generata e restituisca tre valori: il valore massimo raggiunto, la lunghezza della sequenza e la somma di tutti i numeri
def analizza_sequenza(lista_numeri) : #le 3 richieste sono comandi che in python esistono già
    massimo_lista = max(lista_numeri) #max calcola il massimo della lista che avevo prima
    grandezza_lista = len(lista_numeri) #len calcola quanto è lunga la lista
    somma_lista = sum(lista_numeri) #sum somma tutti i numeri presenti
    return massimo_lista , grandezza_lista , somma_lista #mi restituisce i valori richiesti.!Attenzione perchè mettendo 3 return il programma legge solo il primo quindi ne va fatto uno unico!
# aggiungendo print(analizza_sequenza(math_pari_dispari(n))) posto testare la funzione e il terminale mi darà una tupla (lista con parentesi tonde) coi valori richiesti 
#1.5
#Scrivere una funzione ricerca(lista) che scorra la lista e stampi solo i numeri della sequenza che sono divisibili per 5. Se non ce ne sono, va stampato un messaggio dedicato.
def ricerca(lista_numeri) :
    lista_numeri_divisibili_per_5 = 0 #creo una lista dove mettere i numeri divisibili per 5 inizialmente vuota
    for n in lista_numeri : #per ogni numero della lista_numeri
        if n % 5 == 0 : #se n diviso per 5 ha resto 0 (def divisibile per 5)
            print('Numero valido: ', n) #stampa la stringa con a fianco il numero verificato
            lista_numeri_divisibili_per_5 = lista_numeri_divisibili_per_5 + 1 #incremento la lista dei numeri divisibili per 5 di 1
    if lista_numeri_divisibili_per_5 == 0 : #se invece la lista dei numeri divisibili per 5 è vuota.!Si mette l'if anzichè l'else perchè mettendo else mi stamperà anche i numeri non divisibili per 5 per ogni numero che trova ma qui serve solo un messaggio se non ce n'è nemmeno uno!
            print('Nessun numero è divisibile per 5') #stampa la stringa 
#per controllare basta fare ricerca(math_pari_dispari(n))
#1.6
#Unite il tutto in un main program che chieda all’inizio all’utente quanti numeri vuole testare. Usate uno o più loop per chiedere all’utente i numeri da analizzare e per eseguire i punti precedenti per ogni numero. Alla fine stampate un riepilogo che mostri quale numero iniziale ha generato la sequenza più lunga.
def main() :
    quanti_numeri = int(input('Quanti numeri vuoi testare? ')) #prima chiedo all'utente (input) quanti numeri interi (int) vuole testare
    max_lunghezza = 0 #creo una varibile per il massimo della lunghezza che inizialmente è 0 e sarà poi il numero di elementi del numero testato che mi darà la lista più grande 
    numero_vincente = None #creo una variabile per il numero vincente che dopo tutti i confronti sarà quella del numero con la lista più lunga
    for i in range(quanti_numeri) : #per ogni numero che l'utente mi da devo confrontare:
        numero_iniziale = number_generator() #variabile per il numero che devo confrontare su cui appplicherò la prima funzione (number_generator) per ottenere un numero positivo
        sequenza = math_pari_dispari(numero_iniziale) #da quel numero con l'altra funzione creo la lista 
        print('La sequenza generata è: ' , sequenza) #creo una stringa che mi stampi la stringa con la sequenza (FACOLTATIVO)
        il_max, la_lunghezza, la_somma = analizza_sequenza(sequenza) #definisco le variabili per la sequenza del numero iniziale che sarà valutata nella funzione analizza_sequenza 
        print('Massimo:' , il_max , 'Lunghezza:' , la_lunghezza , 'Somma:' , la_somma) #anche qui il print coi valori ottenuti è FACOLTATIVO
        quanti_divisibili = ricerca(sequenza) #variabile per la quantità dei numeri divisibili per 5 per il numero iniziale che si trova valutando la sequenza del numero iniziale nella funzione ricerca
        print('Totale divisibili per 5:' , quanti_divisibili) #mi da il numero dei numeri divisibili per 5 (FACOLTATIVO)
#confronto per trovare il numero con la lunghezza più grande
        if la_lunghezza > max_lunghezza : #se la lunghezza del numero è più grande del massimo
            max_lunghezza = la_lunghezza #la lunghezza del numero diventa la massima lunghezza
            numero_vincente = numero_iniziale #e il numero che sto considerando diventa il numero vincente
    print('Il numero vincente è: ', numero_vincente) #stampa qual'è il numero vincente (NON FACOLTATIVO)
main() #faccio avviare l'applicazione della funzione.!Non serve mettere il print perchè c'è già la funzione!
#!in sintesi nell'esercizio 1.6 è lo svolgimento dei punti 1.2,1.3,1.4,1.5 dando la possibilità direttamente all'utente di scegliere senza dover inserire nel programma un numero da testare.Inoltre come detto nella funzione l'unico print che conta per l'esercizio è quello del numero vincente mentre gli altri servono per verificare che la funzione main funzioni correttamente.!