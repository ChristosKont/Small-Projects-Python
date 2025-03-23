"""Seira Askhsewn 2."""
from math import sqrt

def sum_sequence(n, term):
    """A8roisma arxikwn orwn akolou8ias

    n -- deikths teleutaiou orou (deikths prwtou = 1)
    term -- synarthsh: term(i) einai o i-ostos oros
    """
    i, sum = 1, 0
    while i <= n:
        sum += term(i)
        i += 1
    return sum


#>>>>>>>>>>>>> Askisi 1 <<<<<<<<<<<<<<<<<<<<<<<<<<

def naturals_multiples_of_7(n):
    """Epistrefei ton ari8mo twn pollaplasiwn tou 7
    mikrotera 'h isa tou ari8mou n.

    >>> naturals_multiples_of_7(10)
    1
    >>> naturals_multiples_of_7(14)
    2
    >>> naturals_multiples_of_7(40)
    5
    """
    def is_multiple_of_7(n):
        return (n % 7 == 0)

    return sum_sequence(n, is_multiple_of_7)



#>>>>>>>>>>>>> Askisi 2 <<<<<<<<<<<<<<<<<<<<<<<<<<

def count_squares(n):
    """Epistrefei ton ari8mo twn tetragwnikwn ari8mwn
    mikroterwn 'h iswn tou n. (Tetragwnikos ari8mos =
    k*k gia kapoion akeraio k.)

    >>> count_squares(10)
    3
    >>> count_squares(20)
    4
    >>> count_squares(100)
    10
    """
    is_square = lambda i: i**2 <= n
    return sum_sequence(n, is_square)



#>>>>>>>>>>>>> Askisi 3 <<<<<<<<<<<<<<<<<<<<<<<<<<

def count_primes(n):
    """Epistrefei to plh8os twn prwtwn ari8mwn
    mikroterwn 'h iswn tou n.

    >>> count_primes(1)
    1
    >>> count_primes(10)
    5
    >>> count_primes(20)
    9
    >>> count_primes(10)
    5
    >>> count_primes(100)
    26
    """
    from primes import isprime

    return sum_sequence(n, isprime)



#>>>>>>>>>>>>> Askisi 4 <<<<<<<<<<<<<<<<<<<<<<<<<<

def prime(n):
    """Epistrefei ton n-osto prwto ari8mo.
    
    >>> prime(1)
    1
    >>> prime(4)
    5
    >>> prime(9)
    19
    >>> prime(100)
    523
    """
    """GRAPSTE TON KWDIKA SAS APO KATW."""
    from primes import isprime

    if (n == 1):
        return 1
    else:
        s, x = 1, 1
        while (s != n):
            x += 1
            s += isprime(x)
        return x

    

#>>>>>>>>>>>>> Askisi 5 <<<<<<<<<<<<<<<<<<<<<<<<<<

def count_multiples_of_7(n, term):
    """Epistrefei to plh8os twn orwn ths akolou8ias
    pou einai pollaplasia tou 7.

    n -- deikths tou teleutaiou orou ths akolou8ias
         (1 einai o prwtos oros)
    term -- synarthsh: term(i) einai o i-ostos oros

    >>> count_multiples_of_7(15, lambda x: x*x)
    2
    >>> count_multiples_of_7(15, lambda x: x)
    2
    >>> count_multiples_of_7(15, lambda x: 7*x)
    15
    """
    """GRAPSTE TON KWDIKA SAS APO KATW."""
    def is_multiple_of_7(x):
        return (term(x) % 7 == 0)
    
    return sum_sequence(n, is_multiple_of_7)



#>>>>>>>>>>>>> Askisi 6 <<<<<<<<<<<<<<<<<<<<<<<<<<

def sum_primes(n):
    """Epistrefei to a8roisma twn n prwtwn ari8mwn.
    
    >>> sum_primes(1)
    1
    >>> sum_primes(4)
    11
    >>> sum_primes(5)
    18
    >>> sum_primes(100)
    23593
    """
    """GRAPSTE TON KWDIKA SAS APO KATW."""
    from primes import isprime

    if (n == 1):
        return 1
    else:
        s, x, p = 1, 1, 1
        while (p != n):
            x += 1
            if (isprime(x) == 1):
                s += x
                p += 1
        return s
        
    

#>>>>>>>>>>>>> Askisi 7 <<<<<<<<<<<<<<<<<<<<<<<<<<

def roundize(func):
    """Epistrefei th "stroggyleumenh" parallagh ths
    synarthshs sto orisma.

    func -- synarthsh pou stroggyleuetai

    Epistrefei synarthsh 

    >>> from math import sqrt, sin
    >>> round_sqrt = roundize(sqrt)
    >>> round_sqrt(5)
    2
    >>> roundize(sqrt)(8.5)
    3
    >>> roundize(abs)(3.2)
    3
    >>> roundize(sin)(3)
    0
    >>> roundize(sin)(1.5)
    1
    """
    """GRAPSTE TON KWDIKA SAS APO KATW."""
    def h(x):
        return round(func(x))

    return h



#>>>>>>>>>>>>> Askisi 8 <<<<<<<<<<<<<<<<<<<<<<<<<<

def make_quadratic(a, b, c):
    """Epistrefei thn tetragwnikh synarthsh 
    f(x) = a*x*x+b*x+c.

    >>> f = make_quadratic(1, 2, 1)
    >>> f(0)
    1
    >>> f(-1)
    0
    >>> f(1)
    4
    """
    return lambda x: a*x*x+b*x+c



#>>>>>>>>>>>>> Askisi 9 <<<<<<<<<<<<<<<<<<<<<<<<<<

def derivative(func):
    """Epistrefei thn paragwgo synarthsh.

    func -- Tetragwnikh synarthsh ths morfhs
            a*x*x + b*x + c
    Epistrefei th synarthsh 2*a*x + b

    >>> df = derivative(make_quadratic(1, 2, 1))
    >>> df(1)
    4
    >>> df(0)
    2
    """
    """GRAPSTE TON KWDIKA SAS APO KATW."""

    b = (func(1)-func(-1))/2
    a = func(1)-b-func(0)

    return lambda x: 2*a*x + b



#>>>>>>>>>>>>> Askisi 10 <<<<<<<<<<<<<<<<<<<<<<<<<<

def sum_sequence_rec(n, term):
    """Opws h sum_sequence, omws leitourgei anadromika
    xwris entoles epanalhpshs (while, for).

    >>> sum_sequence_rec(10, lambda x: x*x)
    385
    >>> sum_sequence_rec(10, lambda x: x)
    55
    >>> sum_sequence_rec(10, lambda x: x**3)
    3025
    """
    """GRAPSTE TON KWDIKA SAS APO KATW."""

    if (n == 0):
        return term(0)
    
    return term(n) + sum_sequence_rec(n-1, term)
    


#>>>>>>>>>>>>> Askisi 11 <<<<<<<<<<<<<<<<<<<<<<<<<<

def print_sequence(n, term, reverse=False):
    """Emfanizei tous arxikous orous akolou8ias.

    n -- deikths teleutaiou orou.
    term -- synarthsh: term(i) einai o i-ostos oros
    reverse=False -- logikh timh

    Emfanizei tous orous me deikth 1 ews n ean h
    reverse einai False. Ean einai True, emfanizontai
    me antistrofh seira: apo ton n-osto ews ton 1o.


    >>> print_sequence(5, lambda x:x)
    1
    2
    3
    4
    5
    >>> print_sequence(8, lambda x:x, True)
    8
    7
    6
    5
    4
    3
    2
    1
    >>> print_sequence(8, lambda x:x*x, True)
    64
    49
    36
    25
    16
    9
    4
    1
    """
    """GRAPSTE TON KWDIKA SAS APO KATW."""
    """PREPEI NA LEITOYRGEI ANADROMIKA, XWRIS ENTOLES
    EPANALHPSHS OPWS while, for.
    """

    if (reverse==True and n>0):
        print(term(n))
        print_sequence(n-1, term, reverse)

    if (reverse==False and n>0):
        print_sequence(n-1, term, reverse)
        print(term(n))

        
