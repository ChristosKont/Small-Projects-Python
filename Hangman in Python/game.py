# -*- coding: utf-8 -*-
from utils import *
from screen import figure
from time import sleep

#Αρχικοποιήσεις μεταβλητών
players = getPlayers()
score = getScore(players)
lives = getLives(players)
play, rnd = True, 1

while play == True:

    #Έλεγχος πλήθους ενεργών παικτών
    if len(score) > 1 or rnd == 1:
        
        for c in score:

            #Αρχικοποιήσεις μεταβλητών
            oldList = []
            guess = wordSelection(getDictionary(), oldList)
            temp = list(guess)
            word = list(len(guess) * '_ ')
            i, found = 0, False
            
            sleep(1)
            nextRound(rnd, c, lives)

            #Γύρος του εκάστοτε παίκτη            
            while i < lives[c] and found == False:
                gramma = screen(word)
                sleep(1)
                
                f = gramma in guess
                if f == False:
                    i += 1
                    figure(i, c, lives)
                else:
                    pos = [x for x in range(len(temp)) if temp[x] == gramma]
                    for x in pos: word[2*x] = gramma
                    found = sum([x is '_' for x in word]) == 0
                    
            #Αποτέλεσμα γύρου του εκάστοτε παίκτη      
            if found == True:
                print('\nΣυγχαρητήρια!')
                print('Η λέξη που ψάχναμε ήταν: "%s"' %guess)
            else:
                print('\nΗ λέξη που ψάχναμε ήταν: "%s"' %guess)
            score[c] = int(found)

        #Ανανέωση σκορ μετά το τέλος κάθε γύρου
        rnd += 1
        if sum(score.values()) == 0:
            print('\nΤο παιχνίδι τερμάτησε χωρίς νικητή!')
            play = False
        else:
            score = updateScore(score)
        
    else:
        sleep(1)
        #Μετατρέπει το dict_keys σε λίστα και παίρνει το πρώτο στοιχειο
        winner = list(score.keys())[0]
        print('\nΣυγχαρητήρια! Νίκησε ο παίχτης "%s"!' %winner)
        play = False
        
