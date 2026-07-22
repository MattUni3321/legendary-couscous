#
# File: esercizio3.py
#
# Author: Matteo Napolano
#
# Date: 2026/07/15
#
# Version: 3.12
#
# Description: Esercizio 3 sulla Command Line 
#
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
    età_ordinate.append([val['età'],el]) #metto in età_ordinate solo i valori riferiti all'età, associati al rispettivo nome!Prendo una lista perchè 'append' prende solo un argomento
    età_ordinate.sort() #con sort li metto in ordine crescente
    print(el,età_ordinate) #stampo una lista con gli elementi associati alla rispettiva età in ordine crescente
#3.3
#Invertire l’ordine della lista precedentemente costruita e visualizzatela
età_ordinate.reverse() #con reverse riscrivo la lista disposta prima in ordine crescente al contrario
print(età_ordinate) #stampo le età in ordine
#3.4
#Utilizzare la rubrica e scrivere su schermo per OGNI membro della rubrica, il seguente messaggio:Car[o/a] [Nome],sei nat[o/a] il [giorno] di [mese] del [anno] e quindi a breve compirai [età] anni.Ti manderemo gli auguri a [mail]
for el,val in rubrica.items() : #per gli elementi e i valori rispettivamente accoppiati della rubrica
    if el != 'Ramona Flowers' and el != 'Madoka Ayukawa' : #se la persona non è femmina
        print('Caro' ,el,'sei nato il' ,val['giorno'], 'di', val['mese'], 'del' ,val['anno'], 'e quindi a breve compirai' ,val['età'], 'anni.Ti manderemo gli auguri a', val['mail']) #stampo il messaggio per i maschi
    else : #sennò per gli altri (le femmine)
        print('Cara' ,el,'sei nata il' ,val['giorno'], 'di', val['mese'], 'del' ,val['anno'], 'e quindi a breve compirai' ,val['età'], 'anni.Ti manderemo gli auguri a', val['mail']) #stampo il messaggio per le femmine
#3.5
#Utilizzando args passate in input al vostro programma una chiave [giorno, mese, anno, età, sesso, mail] e visualizzate tutto il contenuto della rubrica (valori) che corrispondono a questa chiave
import sys #importo il modulo sys
chiave = sys.argv[1] #prendo la variabile chiave che passa per tutti gli argomenti d'indice 1 perchè l'argv[0] è python
for val in rubrica.values() : #per ogni valore della rubrica 
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
#!Il punto 3.6 non funziona se non commento il 3.5 perchè pensa che l'elemento sia uno dei valori della chiave!
#3.7
#Utilizzando argparse introduci delle opzioni al vostro programma per eseguire i punti 1, 2, 3, 4, 5 dell’esercizio (esempio: python esercizio_3.py –lista_ordinata –> esegue il punto 2 dell’esercizio)
import argparse
#configuro il modulo 'argparse' per ogni punto
parser = argparse.ArgumentParser()
parser.add_argument('--punto1', action='store_true') #se scrivo sul terminale il punto 1 allora ho true altrimenti sarà false
parser.add_argument('--punto2', action='store_true') #se scrivo sul terminale il punto 2 allora ho true altrimenti sarà false
parser.add_argument('--punto3', action='store_true') #se scrivo sul terminale il punto 3 allora ho true altrimenti sarà false
parser.add_argument('--punto4', action='store_true') #se scrivo sul terminale il punto 4 allora ho true altrimenti sarà false
parser.add_argument('--punto5') #qui oltre a "--punto5" devo scrivere che tipo valore (chiave) sto cercando e non si aggiunge action perchè aggiungo la chiave distinguendolo dagli altri punti
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
    età_ordinate.sort
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