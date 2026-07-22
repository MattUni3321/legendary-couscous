#
# File: progetto_personale.py
#
# Author: Matteo Napolano
#
# Date: 2026/07/20
#
# Version: 3.12
#
# Description: Progetto personale su indovina gli animali 
#

animali = {'gabbiano':{'movimento': 'vola' ,'ambiente': 'mare' , 'nutrimento principale':'pescivoro' , 'particolarità':'ladro di cibo'},
           'piccione':{'movimento':'vola' ,'ambiente':'città' , 'nutrimento principale':'granivoro' , 'particolarità':'portatore di malattie'},
           'aquila':{'movimento':'vola' ,'ambiente':'montagna' , 'nutrimento principale':'carnivoro' , 'particolarità':'ottima vista'},
           'delfino':{'movimento':'nuota' ,'ambiente':'mare' , 'nutrimento principale':'pescivoro' , 'particolarità':'intelligente'},
           'squalo':{'movimento': 'nuota' ,'ambiente': 'mare' , 'nutrimento principale':'carnivoro' , 'particolarità':'denti aguzzi'},
           'sardone':{'movimento':'nuota' ,'ambiente':'mare' , 'nutrimento principale':'planctonivoro' , 'particolarità':'buono impanato'},
           'cane':{'movimento':'cammina' ,'ambiente':'città' , 'nutrimento principale':'onnivoro' , 'particolarità':'olfatto incredibile'},
           'gatto':{'movimento':'cammina' ,'ambiente':'città' , 'nutrimento principale':'carnivoro' , 'particolarità':'agilità'},
           'stambecco':{'movimento':'cammina' ,'ambiente':'montagna' , 'nutrimento principale':'erbivoro' , 'particolarità':'arrampicata'},
           'orso':{'movimento':'cammina' ,'ambiente':'foresta' , 'nutrimento principale':'onnivoro' , 'particolarità':'matto per il miele'},
           'marmotta':{'movimento':'cammina' ,'ambiente':'montagna' , 'nutrimento principale':'erbivoro' , 'particolarità':'fischia come un cantante lirico'},
           'scimmia':{'movimento':'cammina' ,'ambiente':'foresta' , 'nutrimento principale':'onnivoro' , 'particolarità':'adora le banane'},
           'gufo':{'movimento':'vola' ,'ambiente':'foresta' , 'nutrimento principale':'carnivoro' , 'particolarità':'gira la testa completamente'},
           'camaleonte':{'movimento':'cammina' ,'ambiente':'foresta' , 'nutrimento principale':'insettivoro' , 'particolarità':'mimetismo'},
           'topo':{'movimento':'cammina' ,'ambiente':'città' , 'nutrimento principale':'onnivoro' , 'particolarità':'vive nelle fogne'},
           'lupo':{'movimento':'cammina' ,'ambiente':'foresta' , 'nutrimento principale':'carnivoro' , 'particolarità':'canta alla luna'},
           'falco':{'movimento':'vola' ,'ambiente':'montagna' , 'nutrimento principale':'carnivoro' , 'particolarità':'velocissimo per cacciare'}}
#':{'movimento': ,'ambiente': , 'nutrimento principale': , 'particolarità':}
print("Benvenuto a 'L'INDOVINO DEGLI ANIMALI!'") #benvenuto al gioco
input("Digita 'GIOCA' per iniziare: ") #se scrivo GIOCA parte il gioco
print('Scegli uno fra questi animali e lo indovinerò:gabbiano/piccione/aquila/delfino/squalo/sardoni/cane/gatto/stambecco/orso/marmotta/scimmia/gufo/camaleonte/topo/lupo/falco') #scelgo un animale da fare indovinare al programma
candidati = list(animali.keys()) #prendo la chiave della lista animali e la chiamo candidati
animale_scelto = "" #l'animale inizialmente il programma non lo conosce perchè lo scopre domandando e scartando in base ai valori dell'animale
risposta_1 = input('Come si muove? cammina/vola/nuota? ') #chiedo all'utente come si muove
if risposta_1 == 'cammina': #se la risposta è cammina
    risposta_2 = input('Dove vive? città/foresta/mare/montagna: ') #chiedo all'utente dove vive?
    if risposta_2 == 'città' : #se la risposta è città
        risposta_3 = input('Di cosa si nutre principalmente?pescivoro/granivoro/insettivoro/onnivoro/erbivoro/carnivoro/planctonivoro: ')
        if risposta_3 == 'carnivoro' : #se la risposta è carnivoro
            animale_scelto = 'gatto' #l'animale è gatto
        elif risposta_3 == 'onnivoro' : #oppure se la risposta è onnivoro
            risposta_4 = input('Quale è una sua particolarità? olfatto increbile/vive nelle fogne') #chiedo all'utente quale è una sua particolarità
            if risposta_4 == 'olfatto incredibile' : #se la risposta è olfatto incredibile
                animale_scelto = 'cane' #l'animale è cane
            elif risposta_4 == 'vive nelle fogne' : #oppure se la risposta è vive nelle fogne
                animale_scelto = 'topo' #l'animale è topo
    elif risposta_2 == 'foresta' : #oppure se la risposta è foresta
        risposta_3 = input('Di cosa si nutre principalmente?pescivoro/granivoro/insettivoro/onnivoro/erbivoro/carnivoro/planctonivoro: ')
        if risposta_3 == 'carnivoro' : #se la risposta è carnivoro
            animale_scelto = 'lupo' #l'animale è lupo
        elif risposta_3 == 'onnivoro' : #oppure se la risposta è onnivoro
            risposta_4 = input('Quale è una sua particolarità? matto per il miele/adora le banane') #chiedo all'utente quale è una sua particolarità
            if risposta_4 == 'matto per il miele' : #se la risposta è matto per il miele
                animale_scelto = 'orso' #l'animale è orso
            elif risposta_4 == 'adora le banane' : #oppure se la risposta è adora le banane
                animale_scelto = 'scimmia' #l'animale è scimmia
        elif risposta_3 == 'insettivoro' : #oppure se la risposta è insettivoro
            animale_scelto = 'camaleonte' #l'animale è camaleonte
    elif risposta_2 == 'montagna' : #oppure se la risposta è montagna
        risposta_4 = input('Quale è una sua particolarità? arrampicata/fischia come un cantante lirico') #chiedo all'utente quale è una sua particolarità
        if risposta_4 == 'arrampicata' : #se la risposta è arrampicata
            animale_scelto = 'stambecco' #l'animale è stambecco
        elif risposta_4 == 'fischia come un cantante lirico' : #oppure se la risposta è fischia come un cantante lirico
            animale_scelto = 'marmotta' #l'animale è marmotta
elif risposta_1 == 'vola': #oppure se la risposta è vola
    risposta_2 = input('Dove vive? città/foresta/mare/montagna: ') #chiedo all'utente dove vive?
    if risposta_2 == 'città': #se la risposta è città
    risposta_3 = input('Di cosa si nutre principalmente?pescivoro/granivoro/insettivoro/onnivoro/erbivoro/carnivoro/planctonivoro: ')
        if risposta_3 == 'granivoro': #se la risposta è granivoro
            animale_scelto = 'piccione' #l'animale è piccione
    elif risposta_2 == 'foresta' : #oppure se la risposta è foresta
        animale_scelto = 'gufo' #l'animale è gufo
    elif risposta_2 == 'mare' : #oppure se la risposta è mare
        animale_scelto = 'gabbiano' #l'animale è gabbiano
    elif risposta_2 == 'montagna' : #oppure se la risposta è montagna
        risposta_4 = input('Quale è una sua particolarità? ottima vista/velocissimo per cacciare') #chiedo all'utente quale è una sua particolarità
        if risposta_4 == 'ottima vista' : #se la risposta è ottima vista
            animale_scelto = 'aquila' #l'animale è aquila
        elif risposta_4 == 'velocissimo per cacciare': #oppure se la risposta è
            animale_scelto = 'falco' #l'animale è falco
elif risposta_1 == 'nuota': #oppure se la risposta è nuota
    risposta_3 = input('Di cosa si nutre principalmente?pescivoro/granivoro/insettivoro/onnivoro/erbivoro/carnivoro/planctonivoro: ')
    if risposta_3 == 'pescivoro': #se la risposta è pescivoro
        animale_scelto = 'delfino' #l'animale è delfino
    elif risposta_3 == 'carnivoro': #oppure se la risposta è carnivoro
        animale_scelto = 'squalo' #l'animale è squalo
    elif risposta_3 == 'planctonivoro': #oppure se la risposta è planctonivoro
        animale_scelto = 'sardone' #l'animale è sardone
if animale_scelto != "": #se l'animale scelto è diverso da nessuno 
    print("L'animale è:", animale_scelto) #stampo che l'animale è quello scelto 
print('Non esiste animale che non riesca a indovinare!') #stampo 
input("Digita 'RIGIOCA' per fare un'altra partita: ") #propongo all'utente un'altra partita
risposta_3 = input('Di cosa si nutre principalmente?pescivoro/granivoro/insettivoro/onnivoro/erbivoro/carnivoro/planctonivoro: ')
