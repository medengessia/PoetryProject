from typing import Iterable

# Answer 1

def mult_two(n_a: int, n_b: int) -> int:
    """
    Computes the product of two numbers.

    Parameters
    ----------
    n_a : int
        the first number.
    n_b : int
        the second one.

    Returns
    -------
    int
        The product of both numbers.

    """
    return n_a*n_b

# Answer 2

def checkio(data: list) -> list:
    """
    Returns the list of non unique elements.

    Parameters
    ----------
    data : list
        The list to work onto.

    Returns
    -------
    elt
        The list of non unique elements.

    """
    elt = []
    for i in range(len(data)):
        if data[i] in elt:
            elt.append(data[i])
        for j in range(i+1, len(data)):
            if not data[i] in elt:
                if data[i] == data[j]:
                    elt.append(data[i])                
    return elt

# Answer 3

def flat_list(array):
    """
    Returns the one-dimensional list associated to the array

    Parameters
    ----------
    array : list
        The list to work onto.

    Returns
    -------
    new : list
        The one-dimensional list associated to the array.

    """
    new = []
    for lst in array:
        if isinstance(lst, int):
            new.append(lst)
        else:
            new += flat_list(lst)
    return new    

# Answer 4

def goes_after(word: str, first: str, second: str) -> bool:
    """
    Tells if a specific letter in a word comes after another.

    Parameters
    ----------
    word : str
        The word to study.
    first : str
        The letter whose position is to be evaluated with respect to the second.
    second : str
        The letter we want to know whether or not it is right after the first.

    Returns
    -------
    bool
        True if first comes after second, False otherwise.

    """
    res = False
    if first in word and second in word:
        res = word.index(second) - word.index(first) == 1
    return res

# Answer 5

def split_pairs(text: str) -> Iterable[str]:
    """
    Splits a string into a list of pairs of two characters.

    Parameters
    ----------
    text : str
        The string to work onto.

    Returns
    -------
    Iterable[str]
        The list with the pairs of characters.

    """
    split = [text[i]+text[i+1] for i in range(0,len(text)-1,2)]
    if len(text)%2 == 1:
        split.append(text[-1] + "_")
        return split
    return split

# Answer 6

def is_all_upper(text: str) -> bool:
    """
    Tells if all letters are upper cased.

    Parameters
    ----------
    text : str
        The text to study.

    Returns
    -------
    bool
        True if all letters are upper cased, False otherwise.

    """
    return not True in [ord(text[i]) >= 97 and ord(text[i]) <= 122 for i in range(len(text))]
