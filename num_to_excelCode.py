#python 3.7 (f-strings're using)
# This code online-demo: https://repl.it/repls/QuarrelsomeStaidGlobalarrays

import doctest

_test = True
_demo = True

N_LETTERS = 26


def num_to_excel_сode(number):
    """Getting Excel-style code from number
    :param number: number for coding
    :return: srting with Excel-style code

    >>> num_to_excel_сode(2)
    'B'

    >>> num_to_excel_сode(28)
    'AB'

    """

    def get_letter_by_code(n):
        """Getting letter by number code
        :param n: number code
        :return: str (1 symbol)

        >>> get_letter_by_code(1)
        'A'

        >>> get_letter_by_code(26)
        'Z'

        """
        if n >= -2:
            return chr(ord('A') + n)
        else:
            raise ValueError(f"Bad value for n = {n}")

    number -= 1  # for starting with "1" (num_to_excel_сode(1)= "A")
    letter1_code = number // N_LETTERS - 1
    if letter1_code > N_LETTERS:
        letter1 = num_to_excel_сode(letter1_code)
    elif letter1_code == 1:
        # remove extra symbol "@" for first 26 decodings (the only way I found for the moment))
        letter1 = ''
    else:
        letter1 = get_letter_by_code(letter1_code)
    letter2_code = number % N_LETTERS
    letter2 = get_letter_by_code(letter2_code)
    return letter1 + letter2 \
        if letter1 != '@' \
        else letter2  # the only way i've found to fight with extra "@" for 1st 26 letters :-)


def demo_case(from_nr, to_nr):
    """Demo of num_to_excel_сode(n) function for one case for range of numbers
    :param from_nr: start of range
    :param to_nr: end of range
    """
    to_nr = from_nr + to_nr
    for i in range(from_nr, to_nr):
        print(str(f'num_to_excel_сode({i})= {num_to_excel_сode(i)}'))


def power(a, b):
    """Getting a power b"""
    if b == 0: return 1
    for i in range(b - 1):
        a *= a
    return a


def demo():
    """Demo for several cases  at the junctions of threshold values"""
    nr = 4
    demo_case(1, nr)
    for i in range(1, 5):
        demo_case(-1 + power(N_LETTERS, i), nr)

if _test:
    doctest.testmod()

if _demo:
    demo()
