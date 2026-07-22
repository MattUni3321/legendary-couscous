#
# File: esercizio8.py
#
# Author: Matteo Napolano
#
# Date: 2026/07/19
#
# Version: 3.12
#
# Description: Esercizio 8 sulla Gestione errori 
#8.0
#Scrivere un programma per “il gioco dell’impiccato” in cui:
#a)leggete una lista di parole da un file JSON
#b)scegliete una parola a caso con cui giocare dalla lista letta, tramite random
#c)chiedete continuamente all’utente di inserire una lettera o di indovinare la parola, fino al termine del gioco in cui si esauriscono i tentativi o si indovina la parola
#!O verifico un approccio o verifico un altro quindi commentare uno dei 2 per avviare il programma!
#8.1Scrivere il programma con un approccio totalmente LBYL
#!Il programma ha un approccio LBYL perchè verifica tutte le condizioni necessarie prima di compiere l'azione!
import json #importo il modulo json
import random #importo il modulo random
with open('esercizio8.json', 'r') as e_8 : #apro il file esercizio 8 come e_8 in modalità lettura
    esercizio8 = json.load(e_8) #carico il contenuto del file json
parola_casuale = random.choice(esercizio8) #scelgo una parola dalla lista del file
lettera = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #creo una lista per le lettere
list_parola = [i for i in parola_casuale] #creo una lista formata dalle lettere che compongono la parola
impiccato = ["_" for i in range(len(parola_casuale))] #scrivo il numero dei trattini che corrisponde alla lunghezza della parola scelta (len mi da il numero delle lettere che compongono la parola e range fa avviare il for tante volte quanto il numero delle lettere creando'_','_','_')
vite = 10 #parto da 10 vite
print(''.join(impiccato)) #unisco la lista e quindi i trattini creati
while "_" in impiccato and vite>0 : #finchè ci sono ancora trattini e le vite sono più di 0
    risposta = input("Inserisci una lettera:")#chiedo all'utente di inserire una lettera
    indice = list_parola.index(risposta) #questo serve a generare un errore che sarà poi risolto con l'approccio EAFP (tolta la riga, inserendo un carattere speciale o un numero mi toglie una vita) e l'index scorre la lista e la confronta:se il carattere della risposta è una lettera (sta nella lista 'lettera') continuo altrimenti genero un ValueError perchè il valore non è valido
    if risposta == parola_casuale: #se la risposta è la parola scelta
        print("PAROLA TROVATA") #stampo 'PAROLA TROVATA'
        impiccato = list_parola #e scrivo la parola indovinata
    if len(risposta) == 1 : #oppure se l'utente propone una lettera (len==1)
        if risposta in list_parola: #se la lettera è giusta
            for el in range(len(list_parola)) : #controllo ogni lettera della lista
                if list_parola[el] == risposta : #se un elemento della lista è la lettera proposta dall'utente
                    impiccato[el] = risposta #sostituisco la lettera nella sequenza di trattini
        else : #oppure se la lettera non c'è
            vite -= 1 #tolgo una vita
    else : #oppure se la parola proposta dall'utente è sbagliata 
        vite -=2 #tolgo 2 vite
        print('La parola è sbagliata') #e stampo che la parola è sbagliata
    print(''.join(impiccato)) #dopo aver verificato le condizioni ristampo la parola aggiornata e unita (senza join otterrei la lista)
    print('vite:',vite) #stampo il numero di vite
if vite > 0 : #se le vite ci sono ancora 
    print("Complimenti, hai vinto!")  #dico all'utente che ha vinto
else : #oppure se i tentativi sono finiti
    print("Hai perso! La parola era:", parola_casuale) #dico all'utente che ha perso
#8.2
#Riscrivere il programma con un approccio totalmente EAFP
#!Il programma ha un approccio EAFP perchè provo a fare un'azione (try) prevedendo che possa essere sbagliata (exception)
import json #come prima importo il modulo json
import random #e il modulo random
with open('esercizio8.json', 'r') as in_file : #apro il file esercizio 8 come e_8
    esercizio8 = json.load(in_file) #carico il contenuto
parola_casuale = random.choice(esercizio8) #scelgo una parola a caso
list_parola = [i for i in parola_casuale] #creo una lista formata dalle lettere che compongono la parola
impiccato = ["_" for i in range(len(parola_casuale))] #scrivo il numero dei trattini che corrisponde alla lunghezza della parola scelta (len mi da il numero delle lettere che compongono la parola e range fa avviare il for tante volte quanto il numero delle lettere creando'_','_','_')
vite = 10 #parto da 10 vite
lettera = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #creo una lista per le lettere
print(''.join(impiccato)) #unisco la lista e quindi i trattini creati
while "_" in impiccato and vite > 0 : #finchè ci sono ancora trattini (parole da indovinare) e le vite sono più di 0
    risposta = input("Inserisci una lettera:") #chiedo all'utente di inserire una lettera
    try:
        if len(risposta) == 1 : #oppure se l'utente propone una lettera (len==1)
            if not risposta.isalpha() : #se la risposta non è una lettera
                raise ValueError #se ho un ValueError vado direttamente all'except
            elif risposta in list_parola : #oppure se la lettera è giusta
                    for el in range(len(list_parola)) : #controllo ogni lettera della lista
                        if list_parola[el] == risposta : #se un elemento della lista è la lettera proposta dall'utente
                            impiccato[el]=risposta #sostituisco la lettera nella sequenza di trattini
            else : #oppure se la lettera non c'è
                vite -= 1 #tolgo una vita        
        if risposta == parola_casuale : #se la risposta è la parola scelta
            print("PAROLA TROVATA") #stampo 'PAROLA TROVATA'
            impiccato = list_parola #e scrivo la parola indovinata
        else : #oppure se la parola proposta dall'utente è sbagliata
            if len(risposta) > 1 :
                vite -=2 #tolgo 2 vite
                print('La parola è sbagliata') #e stampo che la parola è sbagliata 
    except ValueError : #Se ottengo un ValueError 
        print('Il carattere scelto non è valido') #lo gestisco dicendo che il carattere non è valido

    print(''.join(impiccato)) #dopo aver verificato le condizioni ristampo la parola aggiornata e unita (senza join otterrei la lista)
    print('vite:',vite) #stampo il numero di vite
if vite > 0: #se le vite ci sono ancora 
    print("Complimenti, hai vinto!")  #dico all'utente che ha vinto
else: #oppure se i tentativi sono finiti
    print("Hai perso! La parola era:", parola_casuale) #dico all'utente che ha perso 
#ma perchè raise ValueError?
#poi servono 2 if per farlo funzionare?