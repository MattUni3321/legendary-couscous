#
# File: esercizio6.py
#
# Author: Matteo Napolano
#
# Date: 2026/07/17
#
# Version: 3.12
#
# Description: Esercizio 6:Parte 2  su Object Oriented Programming 
#6.2
#In un file separato importate la classe rubrica appena creata e scrivete un programma che in modo interattivo chieda all’utente di quale delle 5 operazioni della classe rubrica svolgere. Se l’azione richiesta non esiste, il programma continua a chiedere l’azione da svolgere finchè non viene indicata la stringa “EXIT”
import esercizio6_1 #importo la classe dal file esercizio6_1.py perchè non è necessario importare altri elementià dal file
mia_rubrica = esercizio6_1.Rubrica() #creo l'oggetto della rubrica iniziale
while True: #finchè l'utente non scrive "EXIT"
    azione = input("Operazione (APRI, AGGIUNGI, RIMUOVI, SALVA, STAMPA, EXIT): ") #crea un input per poter scegliere le varie azioni (con .strip().upper volendo posso far sì che l'opzione sia valida anche se scrivo l'azione in minuscolo) 
    if azione == "EXIT" : #il programma continuerà a chiedermi la domanda dell'input se l'operazione non esiste quindi se scrivo EXIT sul terminale
        break #il programma si chiude
    elif azione == "APRI" : #oppure se voglio aprire un contatto rispondo 'APRI' al terminale
        mia_rubrica.apri_rubrica(input("Nome file da aprire: ")) #il programma la apre e mi chiede che file voglio aprire
    elif azione == "AGGIUNGI" : #oppure se voglio aggiungere una rubrica rispondo 'AGGIUNGI' al terminale
        nome = input("Nome contatto: ") #il programma mi chiede quale nome (elemento) voglio aggiungere
        #chiedo all'utente i singoli dati del nome perchè la rubrica contiene anche i valori rispettivi all'elemento.!Dove viene richiesto un numero l'input deve potersi convertire in un intero!
        giorno = int(input("Giorno di nascita (numero): ")) 
        mese = input("Mese di nascita: ")
        anno = int(input("Anno di nascita: "))
        eta = int(input("Età: "))
        sesso = input("Sesso (M/F): ").strip().upper()
        mail = input("Indirizzo Email: ")
        dati = {'giorno': giorno, 'mese': mese, 'anno': anno, 'età': eta, 'sesso': sesso, 'mail': mail} #metto i dati in un dizionario
        mia_rubrica.aggiungi_nome(nome, dati) #inserisco il contatto nella rubrica
    elif azione == "RIMUOVI" : #oppure se voglio togliere una contatto rispondo 'RIMUOVI' al terminale
        mia_rubrica.rimuovi_el(input("Nome contatto da rimuovere: ")) #chiedo il contatto che l'utente vuole rimuovere
    elif azione == "SALVA" : #oppure se voglio salvare una rubrica rispondo 'SALVA' al terminale
        mia_rubrica.salva_rubrica(input("Nome file per salvare: ")) #chiedo il nome del file da salvare che dev'essere in json o txt come impostato nel punto 6.1 
    elif azione == "STAMPA" : #oppure se voglio stampare un contatto rispondo 'STAMPA' al terminale
        mia_rubrica.stampa_dati(input("Nome contatto da stampare: ")) #chiedo il nome del contatto da stampare
    else :
        print(f"L'azione" ,azione,"non esiste. Riprova.") #oppure se l'azione che vorrei fare non esiste dico all'utente di riprovare finchè non rispondo 'EXIT'
#Per controllare le azioni devo sempre aprire e poi:
#per AGGIUNGI: aggiungi e salva
#per RIMUOVI: rimuovi e salva
#per SALVA: salva
#per STAMPA: stampa e salva
