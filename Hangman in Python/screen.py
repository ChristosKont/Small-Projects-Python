# -*- coding: utf-8 -*-
def figure(i, name, lives):
    """
    Συνάρτηση που εκτυπώνει στο λάθος
    κάθε παίκτη την κρεμάλα που έχει σχηματιστει

    i --- πλήθος λαθών που έχει κάνει ο παίκτης
    name --- όνομα του εκάστοτε παίκτη, απαραίτητο για το dictionary(lives)
    lives --- dictionary που περιέχει το πλήθος ζωών του εκάστοτε παικτη

    """
    l = lives[name]

    if l == 4:
        
        if i == 1:
            print('|---------|')
            print('|         Ο')
            print('|         |')
            print('|         |')
            print('|')
            print('|')
            print('|')
        elif i == 2:
            print('|---------|')
            print('|         Ο')
            print('|       / | \ ')
            print('|         |')
            print('|       _/ \_')
            print('|')
            print('|')
        elif i == 3:
            print('|---------|')
            print('|         Ο')
            print('|       / | \ ')
            print('|         |')
            print('|       _/ \_')
            print('|      ### ###')
            print('|')
        else:
            print('|---------|')
            print('|         Ο')
            print('|       / | \ ')
            print('|         |')
            print('|       _/ \_')
            print('|      ### ###')
            print('|      f i r e')
    
    elif l == 6:
        
        if i == 1:
            print('|---------|')
            print('|         Ο')
            print('|')
            print('|')
            print('|')
            print('|')
            print('|')
        elif i == 2:
            print('|---------|')
            print('|         Ο')
            print('|       / | \ ')
            print('|')
            print('|')
            print('|')
            print('|')
        elif i == 3:
            print('|---------|')
            print('|         Ο')
            print('|       / | \ ')
            print('|         |')
            print('|')
            print('|')
            print('|')
        elif i == 4:
            print('|---------|')
            print('|         Ο')
            print('|       / | \ ')
            print('|         |')
            print('|       _/ \_')
            print('|')
            print('|')
        elif i == 5:
            print('|---------|')
            print('|         Ο')
            print('|       / | \ ')
            print('|         |')
            print('|       _/ \_')
            print('|      ### ###')
            print('|')
        elif i == 6:
            print('|---------|')
            print('|         Ο')
            print('|       / | \ ')
            print('|         |')
            print('|       _/ \_')
            print('|      ### ###')
            print('|      f i r e')

    else:
        
        if i == 1:
            print('|---------|')
            print('|         Ο')
            print('|')
            print('|')
            print('|')
            print('|')
            print('|')
        elif i == 2:
            print('|---------|')
            print('|         Ο')
            print('|         |')
            print('|         |')
            print('|')
            print('|')
            print('|')
        elif i == 3:
            print('|---------|')
            print('|         Ο')
            print('|         | \ ')
            print('|         |')
            print('|')
            print('|')
            print('|')
        elif i == 4:
            print('|---------|')
            print('|         Ο')
            print('|       / | \ ')
            print('|         |')
            print('|')
            print('|')
            print('|')
        elif i == 5:
            print('|---------|')
            print('|         Ο')
            print('|       / | \ ')
            print('|         |')
            print('|          \_')
            print('|')
            print('|')
        elif i == 6:
            print('|---------|')
            print('|         Ο')
            print('|       / | \ ')
            print('|         |')
            print('|       _/ \_')
            print('|')
            print('|')
        elif i == 7:
            print('|---------|')
            print('|         Ο')
            print('|       / | \ ')
            print('|         |')
            print('|       _/ \_')
            print('|      ### ###')
            print('|')
        else:
            print('|---------|')
            print('|         Ο')
            print('|       / | \ ')
            print('|         |')
            print('|       _/ \_')
            print('|      ### ###')
            print('|      f i r e')

    if i < l-1:
        print('\nΈχεις ακόμα %i ζωές!' %(l-i))
    elif i == l-1:
        print('\nΈχεις ακόμα 1 ζωή!')
