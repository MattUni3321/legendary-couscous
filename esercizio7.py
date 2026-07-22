#
# File: esercizio7.py
#
# Author: Matteo Napolano
#
# Date: 2026/07/18
#
# Version: 3.12
#
# Description: Esercizio 7  su Object Unpacking,Decoratori,Generatori e Lambda
#7.1 
#Il programma deve contenere un generatore che, dato un numero (ad esempio 7), generi la tabellina corrispondente al numero selezionato (0x7 = 0; 1x7 = 7; 2x7 = 14; ecc…);
import numpy #importo il modello del numpy
def generatore(n) : #definisco la funzione che genera un numero
    for i in range(11) : #per i che va da 0 a 10 (11 perchè python parte da 0) 
        tabellina = n * i #moltiplico il numero per ogni i e chiamo tabellina il numero trovato 
        yield n ,'x' ,i, '=', tabellina #il return per i generatori mi restituirà (se faccio una prova) i per il numero uguale al risultato
#per verificare se funziona:
n=16 #scelgo un numero
print('Tabellina del',n,':') #stampo 'tabellina del' e il numero (FACOLTATIVO)
generatore(n) #applico il generatore al numero
for riga in generatore(n) : #per ogni riga della tabellina
    print(*riga) #lo stampo.!Scrivere '*riga' serve a non avere le tabelline con x e = come stringhe e con le parentesi ((8'x'0=0)!
#7.2
#Contenere un loop che chieda in modo interattivo all’utente di indovinare il valore corrente nella tabellina selezionata
#7.3
#Gestire tutti i caratteri alfanumerici (non deve “rompersi” se l’utente sceglie una lettera) 
#7.4
#Gestire caretteri speciali o numeri decimali
#Le righe da 35 a 37 riguardano i punti 7.3 e 7.4
#7.5
#Gestire la chiusura del gioco in modo personalizzato.(Fornire il punteggio totalizzato dall'utente e concludere il gioco)
#Le righe 38,46,49,50 riguardano l'esercizio 7.5
tabellina_scelta = input('Di quale numero vuoi indovinare la tabellina?') #chiedo la tabellina da indovinare
while not tabellina_scelta.isdigit() : #finchè la risposta non è un numero
    tabellina_scelta = input('Mi dispiace ma non hai inserito un numero.Di quale numero vuoi indovinare la tabellina?') #faccio riprovare l'utente
tabellina_scelta = int(tabellina_scelta) #sicuro che non sia una lettera,un carattere speciale o un decimale, verifico che sia effettivamente un numero
punti = 0 #parto dal punteggio come 0
for riga in generatore(tabellina_scelta): #per ogni riga della tabellina per il numero richiesto
    risultato_esatto = riga[4] #il quarto elemento della riga è il risultato
    for i in range(4) : #per 'i' nei 4 elementi che sono il numero scelto, 'x', il valore della tabellina, l' '=' e il risultato
        print(riga[i], end ='') #stampo gli elementi e evito di andare a capo lasciando uno spazio vuoto (sennò gli elementi sarebbero incolonnati e nn in riga) (end) ,e mostro la domanda a cui l'utente deve rispondere
    risposta = int(input('Risposta:')) #il programma chiede all'utente la risposta alla domanda     
    if risposta == risultato_esatto : #se la risposta è esatta
        print("Esatto!") #stampo esatto
        punti += 1 #se la risposta è esatta aggiungo un punto
    else: #oppure se è sbagliato
        print("Sbagliato! La risposta corretta era:", risultato_esatto) #stampo la risposta corretta
print('Hai totalizzato', punti, 'punti!') #stampo quanti punti ha totalizzato
print('Grazie per aver giocato!') #stampo