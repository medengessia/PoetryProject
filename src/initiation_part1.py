# Answer 1

def mult_two(a: int, b: int) -> int:
    return a*b

# Answer 2

def checkio(data: list) -> list:
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
    new = []
    for l in array:
        if type(l) == int:
            new.append(l)
        else:
            new += flat_list(l)
    return new    

# Answer 4

def goes_after(word: str, first: str, second: str) -> bool:
    res = False
    if first in word and second in word:
        res = word.index(second) - word.index(first) == 1
    return res

# Answer 5

from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    split = [text[i]+text[i+1] for i in range(0,len(text)-1,2)]
    if len(text)%2 == 1:
        split.append(text[-1] + "_")
        return split
    return split

# Answer 6

def is_all_upper(text: str) -> bool:
    return not True in [ord(text[i]) >= 97 and ord(text[i]) <= 122 for i in range(len(text))]
