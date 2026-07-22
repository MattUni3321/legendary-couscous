#
# File: esercizio6.py
#
# Author: Matteo Napolano
#
# Date: 2026/07/17
#
# Version: 3.12
#
# Description: Esercizio 6:Parte 1  su Object Oriented Programming 
#6.1
#in un file separato, creare una classe rubrica che deve fare 5 azioni:
#a)aprire una rubrica leggendola da un file (JSON oppure testo) - APRI
#b)aggiungere un elemento alla rubrica - AGGIUNGI
#c)rimuovere un elemento dalla rubrica (dato il nome) - RIMUOVI
#d)salvare la rubrica su un file (JSON o testo) - SALVA
#e)stampare tutte le informazioni di un contatto (data il nome), come nell’eserczio 3 - STAMPA
#la classe rubrica deve:
#f)inizializzarsi con un dizionario (come nell’esercizio 3):
#g)avere un classmethod per inizializzarla con un file JSON
#h)deve avere un classmethod per inizializzarla con un file testo
import json #importo il modulo per i file JSON
class Rubrica : #creo la classe Rubrica 
    def __init__(self, rubrica_iniziale=None) : #inizializzo la rubrica assumendo che possa essere anche vuota
        self.nome = rubrica_iniziale #se ho la rubrica la inizializzo con quella dell'esercizio 3
    def apri_rubrica(self, esercizio3) : #apro la rubrica da un file json o un testo
        if esercizio3.endswith('.json') : #se il file finisce con json quindi è json
            with open(esercizio3, 'r') as f : #apri in modalità lettura
                self.nome = json.load(f) # carica la rubrica dal file JSON
        elif esercizio3.endswith('.txt') : #o se è un file testo
            dati = {} #creo un dizionario per i dati
            with open(esercizio3, 'r') as f : #con aperto l'esercizio 3 in modalità lettura
                self.nome = dati # carica il dizionario dal file di testo
    def aggiungi_nome(self, nome, val) : 
        if self.nome is None : #se la rubrica non è stata aperta
            print("Prima apri una rubrica") #stampo 
            return #blocco l'inserimento
        self.nome[nome] = val #o inserisce nella rubrica il nuovo contatto usando il nome
        print("Contatto", nome, "aggiunto.") #stampa il nome (FACOLTATIVO)
    def rimuovi_el(self, nome) : 
        if not self.nome: #se la rubrica è None o è un dizionario vuoto {}
            print("La rubrica è vuota.") #stampo
            return #blocco la rimozione
        if nome not in self.nome : #se l'elemento da rimuovere non esiste
            print("Il contatto", nome, "non esiste in rubrica") #stampo
            return #blocco la rimozione 
        del self.nome[nome] #sennò rimuovo il nome
        print("Contatto", nome, "rimosso.") #stampa il nome (FACOLTATIVO)
    def salva_rubrica(self, esercizio3) : 
        if not self.nome: #se la rubrica è essere vuota o non esiste (None)
            print("La rubrica è vuota.") #stampo
            return #blocco il salvataggio
        if esercizio3.endswith('.json') : #se salvo con json
            with open(esercizio3, 'w') as f : #apri in modalità scrittura
                json.dump(self.nome, f) #salvo in formato JSON 
        elif esercizio3.endswith('.txt') : #oppure se salvo con txt
            with open(esercizio3, 'w') as f : #apro in modalità scrittura
                for chiave, valore in self.nome.items() : #per ogni chiave e valore nel nome dell'oggetto corrente
                    f.write(f"{chiave}:{valore}\n") #salvo in formato testo con la formattazione f-strings 
    def stampa_dati(self, nome) :
        if not self.nome : #se la rubrica è vuota o non esiste
            print("La rubrica è vuota.") #stampo
            return #blocco la stampa
        if nome not in self.nome : #se l'elemento che voglio stampare non esiste
            print("Il contatto",nome,"non esiste in rubrica") #stampo
            return #blocco la stampa per evitare crash
        val = self.nome[nome] #sennò stampo il dizionario riferito a quel nome
        print(nome, 'giorno', val['giorno'], 'mese', val['mese'], 'anno', val['anno'], 'età', val['età'], 'sesso', val['sesso'], 'mail', val['mail']) #stampo i valori
    @classmethod #col 'classmethod' applico un metodo alla classe Rubrica
    def da_json(cls, esercizio3) : #cls è la variabile che mi permette di conoscere i metodi della classe
        with open(esercizio3, 'r') as f : #aprendo il file in modalità lettura
            dati = json.load(f) #leggo la rubrica dal file JSON
        return cls(dati) #restituisco l'oggetto della classe Rubrica già inizializzato 
    @classmethod
    def da_txt(cls, esercizio3) : 
        dati = {}  #creo il dizionario vuoto
        with open(esercizio3, 'r') as f : #apro il file in modalità lettura
            for riga in f:  #lo leggo riga per riga
                if riga.strip(): #se la riga ha spazi vuoti
                    chiave, valore_str = riga.strip().split(':', 1) #tolgo gli spazi e separo chiavi e valori (strip toglie lo spazio e split divide la stringa al primo ":"che trovo)
                    valore_valido = valore_str.replace("'", '"') #per rendere il JSON valido tolgo gli apici
                    dati[chiave] = json.loads(valore_valido) #converto la stringa in un dizionario di cui posso leggere il contenuto con loads
        return cls(dati) #restituisco l'oggetto inizializzato
#il  punto 6.2 si trova nell'altro file