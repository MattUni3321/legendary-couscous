#
# File: esercizio4.py
#
# Author: Matteo Napolano
#
# Date: 2026/07/15
#
# Version: 3.12
#
# Description: Esercizio 4 su Input/Output  
#
#RICOPIO IL CODICE DELL'ESERCIZIO 3
#testo copiato e incollato dell'esercizio
rubrica = {
'Paolino Paperino': {'giorno': 9,'mese': 'giugno','anno': 1934,'età': 89,'sesso': 'M','mail': 'paolino.paperin0@disney.org'},
'Ron Weasley': {'giorno': 1, 'mese': 'marzo','anno': 1980,'età': 43,'sesso': 'M','mail': 'ron_weasley80@hogwards.uk'},
'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 19, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 54, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}
#3.1:
#Partendo dal dizionario annidato rubrica, visualizzare il contenuto del dizionario stampando a schermo delle stringhe formattate che contengano la chiave ed il valor di ognuno degli elementi(Esempio: ‘Paolino Paperino’, ‘giorno’ 9, ‘mese’ ‘giugno’, …)
for el , val in rubrica.items() : #per ogni chiave (el) e valore (val) creo una coppia che li contenga (items) e lo faccio per ogni valore a cui è associata la chiave
    print("'",el,"',","'giorno'",val['giorno'],",","'mese'",val['mese'],",","'anno'",val['anno'],",","'età'",val['età'],",","'sesso'",val['sesso'],",","'mail'",val['mail']) #la struttura piena di stringhe di questo print serve semplicemente ad avere la struttura richiesta dall'esercizio
#3.2
#A partire dalla rubrica, costruire la lista delle età, ordinata in ordine crescente e visualizzare i nomi in ordine crescente di età
età_ordinate = [] #creo una lista che contenga i valori dell'età
for el,val in rubrica.items() : #per ogni valore e elemento nei valori
    età_ordinate.append([val['età'],el]) #metto in età_ordinate solo i valori riferiti all'età, associato al rispettivo nome!Prendo una lista perchè 'append' prende solo un argomento
    età_ordinate.sort() #il sort li mette in ordine crescente
    print(el,età_ordinate) #stampo una lista con gli elementi associati alla rispettiva età in ordine crescente
#3.3
#Invertire l’ordine della lista precedentemente costruita e visualizzatela
età_ordinate.reverse() #con reverse riscrivo la lista in ordine crescente al contrario
print(età_ordinate) #stampo le età in ordine
#3.4
#Utilizzare la rubrica e scrivere su schermo per OGNI membro della rubrica, il seguente messaggio:Car[o/a] [Nome],sei nat[o/a] il [giorno] di [mese] del [anno] e quindi a breve compirai [età] anni.Ti manderemo gli auguri a [mail]
for el,val in rubrica.items() : #per gli elementi e i valori rispettivamente accoppiati della rubrica
    if el != 'Ramona Flowers' and el != 'Madoka Ayukawa' : #se la persona non è femmina
        print('Caro' ,el,'sei nato il' ,val['giorno'], 'di', val['mese'], 'del' ,val['anno'], 'e quindi a breve compirai' ,val['età'], 'anni.Ti manderemo gli auguri a', val['mail']) #stampa il messaggio per i maschi
    else : #sennò per gli altri (le femmine)
        print('Cara' ,el,'sei nata il' ,val['giorno'], 'di', val['mese'], 'del' ,val['anno'], 'e quindi a breve compirai' ,val['età'], 'anni.Ti manderemo gli auguri a', val['mail']) #stampa il messaggio per le femmine
#3.5
#Utilizzando args passate in input al vostro programma una chiave [giorno, mese, anno, età, sesso, mail] e visualizzate tutto il contenuto della rubrica (valori) che corrispondono a questa chiave
import sys #importo il modulo sys
chiave = sys.argv[1] #prendo la variabile chiave che passa per tutti gli argomenti 
for val in rubrica.values() : #per i valori della rubrica 
    print(val[chiave]) #stampa il valore richiesto
print(sys.argv) #stampa la lista degli argomenti passati
#Nel punto 3.5 ho creato un blocco di istruzioni nel quale se scrivo sul terminale 'python esercizio3.py età' dove età sarebbe la chiave ed è uno dei possibili valori della rubrica mi verrà restituito l'elenco dei valori della mia chiave (primo print) e la lista con esercizio3.py e l'argomento (la chiave) scelto (secondo print)
#3.6
#Utilizzando argparse visualizzare la stringa al punto 4 SOLO per il nome fornito come opzione al vostro programma (esempio: python esercizio_3.py –nome ‘Madoka Ayukawa’ –> esegue punto 4 solo per il nome indicato)
import argparse #importo il modulo argparse
#configuro argparse
parser = argparse.ArgumentParser() 
parser.add_argument('--el') #creo l'argomento che andrà messo nel terminale
args = parser.parse_args()
el = args.el
val = rubrica[el]
#ridefinisco i valori per evitare che si presenti il KeyError se il nome non esiste o è scritto male
giorno = val['giorno']
mese = val['mese']
anno = val['anno']
eta = val['età']
mail = val['mail']
#rimetto l'if del 3.4 per ottenere ciò che mi serve per l'esercizio
if el != 'Ramona Flowers' and el != 'Madoka Ayukawa':
    print('Caro', el, ', sei nato il', giorno, 'di', mese, 'del', anno, 'e quindi a breve compirai', eta, 'anni. Ti manderemo gli auguri a', mail)
else:
    print('Cara', el, ', sei nata il', giorno, 'di', mese, 'del', anno, 'e quindi a breve compirai', eta, 'anni. Ti manderemo gli auguri a', mail)
#!Il punto 3.6 non funziona se non commento il 3.5 perchè oensa che l'elemento sia uno dei valori della chiave!
#INIZIO ESERCIZIO 4 MODIFICANDO IL PUNTO 3.7
#(3.7Utilizzando argparse introduci delle opzioni al vostro programma per eseguire i punti 1, 2, 3, 4, 5 dell’esercizio (esempio: python esercizio_3.py –lista_ordinata –> esegue il punto 2 dell’esercizio))
#4.1
#Partendo dall’esercizio 3, aggiungere una opzione al programma per generare un file di testo rubrica.txt contenente tutti gli elmenti della rubrica, uno per linea, con tutte le informazioni separate da virgole. Ad esempio:
#!Le righe nuove usate per questo punto sono la riga 84 e le righe 117-123!
import argparse
#configuro il modulo 'argparse' per ogni punto
parser = argparse.ArgumentParser()
parser.add_argument('--punto1', action = 'store_true') #se scrivo sul terminale il punto 1 allora ho true altrimenti sarà false
parser.add_argument('--punto2', action = 'store_true') #se scrivo sul terminale il punto 2 allora ho true altrimenti sarà false
parser.add_argument('--punto3', action = 'store_true') #se scrivo sul terminale il punto 3 allora ho true altrimenti sarà false
parser.add_argument('--punto4', action = 'store_true') #se scrivo sul terminale il punto 4 allora ho true altrimenti sarà false
parser.add_argument('--punto5') #Qui oltre a --punto5 devo scrivere che tipo valore (chiave) sto cercando e non si aggiunge action perchè aggiungo la chiave distinguendolo dagli altri punti
parser.add_argument('--punto4_1', action = 'store_true') #se scrivo sul terminale il punto 4_1 allora ho true altrimenti false 
args = parser.parse_args()
#se voglio farlo per il punto 1 svoglio le azioni del punto 1
if args.punto1 :
    for el , val in rubrica.items() : 
        print("'",el,"',","'giorno'",val['giorno'],",","'mese'",val['mese'],",","'anno'",val['anno'],",","'età'",val['età'],",","'sesso'",val['sesso'],",","'mail'",val['mail'])
#oppure se voglio farlo per il punto 2 svoglio le azioni del punto 2
elif args.punto2 :
    età_ordinate = []
    for el,val in rubrica.items() :
        età_ordinate.append([val['età'],el])
        età_ordinate.sort()
        print(el,età_ordinate)
#oppure se voglio farlo per il punto 3 svoglio le azioni del punto 3
elif args.punto3 :
    età_ordinate = []
    for el,val in rubrica.items() :
        età_ordinate.append([val['età'],el])
    età_ordinate.reverse()
    print(età_ordinate)
#oppure se voglio farlo per il punto 4 svoglio le azioni del punto 4
elif args.punto4 :
    for el,val in rubrica.items() :
        if el != 'Ramona Flowers' and el != 'Madoka Ayukawa' :
            print('Caro', el, 'sei nato il', val['giorno'], 'di', val['mese'], 'del', val['anno'], 'e quindi a breve compirai', val['età'], 'anni.Ti manderemo gli auguri a', val['mail'])
        else :
            print('Cara', el, 'sei nata il', val['giorno'], 'di', val['mese'], 'del', val['anno'], 'e quindi a breve compirai', val['età'], 'anni.Ti manderemo gli auguri a', val['mail'])
#oppure se voglio farlo per il punto 5 svoglio le azioni del punto 5
elif args.punto5 :
    for val in rubrica.values() :
        print(val[args.punto5])
#Per far funzionare il punto 3.7 bisogna commentare i punti 3.5 e 3.6
#creo un file rubrica.txt contenente i contatti separati da virgola, uno per riga
elif args.punto4_1 : #oppure se l'argomento è il punto 4_1
    with open("rubrica.txt", "w") as file: #apro il file rubrica.txt in modalità scrittura (w=write)
        for el, val in rubrica.items(): #per ogni nome (el) e valore (val) della rubrica
            riga = el + ", " + str(val['giorno']) + ", " + val['mese'] + ", " + str(val['anno']) + ", " + str(val['età']) + ", " + val['sesso'] + ", " + val['mail'] #unisco con la concatenazione i dati in un'unica riga di testo separato da virgole, trasformando i valori in stringhe (str[val['valore']]) perchè l'operazione va fatta con valori dello stesso tipo
            file.write(riga) #scrivo la riga appena generata all'interno del file
            print(riga) #stampa la riga          
        file.close() #è sempre meglio chiudere il file per sicurezza e per risparmiare memoria
#4.2
#Creare un file JSON che contiene la rubrica con la stessa struttura del dizionario interno al programma
import json #importa il modulo json
with open("rubrica.json", "w") as file : #apro la rubrica.json in modalità scrittura (w=write)
    json.dump(rubrica, file) #scrivo il contenuto selezionato (la rubrica) nel file oggetto
#!Non serve necessariamente che creo un file da 0 perchè se il file non esiste con questo blocco di istruzioni python crea un file nuovo con "w"!
#4.3 
#Leggere la rubrica salvata in un file formato JSON e visualizzate tutto il contenuto
with open("rubrica.json", "r") as file: #apro la rubrica.json in modalità lettura (r=read)
    dati = json.load(file)  #leggo il contenuto del file in una rubrica
print(dati) #stampo la rubrica coi dati
#Alla fine ottengo un dizionario annidato costruito con {persona: {valori} e avanti con le altre persone coi rispettivi dizionari dei valori}