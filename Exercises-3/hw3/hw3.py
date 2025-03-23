
#--------------------- Askisi 1 -----------------------------

def pick_cherries_onebyone():
    """Emfanizei string pou briskontai se fwliasmenes listes.

    Prepei na exei to akolou8o apotelesma:

    >>> pick_cherries_onebyone()
    cherry1
    cherry2
    cherry3
    cherry4
    Yay!!!
    """
    cherry_field = ['cherry1', ['cherry2', ['cherry3', ['cherry4', ['Yay!!!', None]]]]]

    print(cherry_field________________)
    print(cherry_field________________)
    print(cherry_field________________)
    print(cherry_field________________)
    print(cherry_field________________)


    
#--------------------- Askisi 2 -----------------------------

def pick_cherries_iter(field):
    """Emfanizei string pou briskontai se fwliasmenes listes.

    field -- lista me fwliasmena string. Ka8e lista exei dyo stoixeia: to prwto einai
             string kai to deutero einai eite lista ths idias morfhs 'h None. 
             (Opws kai h cherry_field sto swma ths synarthshs pick_cherries_onebyone().

    Paradeigmata:

    >>> cherry_field = ['cherry1', ['cherry2', ['cherry3', ['cherry4', ['Yay!!!', None]]]]]
    >>> pick_cherries_iter(cherry_field)
    cherry1
    cherry2
    cherry3
    cherry4
    Yay!!!
    >>> pick_cherries_iter(['Hello', ['world', None]])
    Hello
    world
    """
    _______________________
    _______________________
    _______________________
    _______________________

    while _________________
        ___________________
        print(____________)
        ___________________


#--------------------- Askisi 3 -----------------------------

def pick_cherries_rec(field):
    """Emfanizei string pou briskontai se fwliasmenes listes.

    field -- lista me fwliasmena string. Ka8e lista exei dyo stoixeia: to prwto einai
             string kai to deutero einai eite lista ths idias morfhs 'h None. 
             (Opws kai h cherry_field sto swma ths synarthshs pick_cherries_onebyone().

    Anadromiki synarthsh: den epitrepetai na xrhsimopoihsete entoles epanalhpshs
    (for, while) 'h list comprehension.

    Paradeigmata:

    >>> cherry_field = ['cherry1', ['cherry2', ['cherry3', ['cherry4', ['Yay!!!', None]]]]]
    >>> pick_cherries_rec(cherry_field)
    cherry1
    cherry2
    cherry3
    cherry4
    Yay!!!
    >>> pick_cherries_rec(['Hello', ['world', None]])
    Hello
    world
    """
    """ GRAPSTE TON KWDIKA SAS APO KATW. XRHSIMOPOIHSTE ANADROMH.
    OXI FOR, WHILE, LIST COMPREHENSIONS."""

    

        
#--------------------- Askisi 4 -----------------------------

def pick_cherries_proc(field):
    """Emfanizei string pou briskontai se fwliasmenes listes.

    field -- lista me fwliasmena string. Ka8e lista exei dyo stoixeia: to prwto einai
             string kai to deutero einai eite lista ths idias morfhs 'h None. 
             (Opws kai h cherry_field sto swma ths synarthshs pick_cherries_onebyone().

    Paradeigmata:

    >>> cherry_field = ['cherry1', ['cherry2', ['cherry3', ['cherry4', ['Yay!!!', None]]]]]
    >>> pick_cherries_proc(cherry_field)
    cherry1
    cherry2
    cherry3
    cherry4
    Yay!!!
    >>> pick_cherries_proc(['Hello', ['world', None]])
    Hello
    world
    """
    """ GRAPSTE TON KWDIKA SAS APO KATW. XRHSIMOPOIHSTE ANADROMH.
    OXI FOR, WHILE, LIST COMPREHENSIONS."""

    def flatten(ls):
        _______________________
        _______________________
        _______________________
        _______________________
        

    [print(__________) for _________ in flatten(___________)]
        


#--------------------- Askisi 5 -----------------------------

def korakize(sentence):
    """Metafrazei sta korakistika.

    sentence -- string pou 8a metafrastei
   
    Epistrefei string metafrasmeno sta korakistika.

    Paradeigmata:

    >>> korakize('Kalimera')
    'Kakalikamekaraka'
    >>> korakize('Maria')
    'Makarikaaka'
    >>> korakize('Kalimera Maria')
    'Kakalikamekaraka Makarikaaka'
    >>> korakize('Na zi kanis i na min zi')
    'Naka zika kakanikaska ika naka mikanka zika'
    """
    """GRAPSTE TON KWDIKA SAS APO KATW."""



#--------------------- Askisi 6 -----------------------------

def dekorakize(sentence):
    """Metafrazei apo korakistika.

    sentence -- string sta korakistika pou 8a metafrastei
   
    Epistrefei string. Einai h antistrofh synarthsh ths korakize.

    Paradeigmata:

    >>> dekorakize('Kakalikamekaraka')
    'Kalimera'
    >>> dekorakize('Makarikaaka')
    'Maria'
    >>> dekorakize('Kakalikamekaraka Makarikaaka')
    'Kalimera Maria'
    >>> dekorakize('Naka zika kakanikaska ika naka mikanka zika')
    'Na zi kanis i na min zi'
    """
    """GRAPSTE TON KWDIKA SAS APO KATW."""


