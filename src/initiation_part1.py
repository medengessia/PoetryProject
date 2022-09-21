# Answer 1

def mult_two(a: int, b: int) -> int:
    return a*b


print("Example")
print(mult_two(1, 2))

assert mult_two(3, 2) == 6
assert mult_two(0, 1) == 0

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

print('Example:')
print(checkio([1, 2, 3, 1, 3]))

assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
assert checkio([1, 2, 3, 4, 5]) == []
assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
assert checkio([2, 2, 3, 2, 2]) == [2, 2, 2, 2]
assert checkio([10, 20, 30, 10]) == [10, 10]
assert checkio([7]) == []
assert checkio([0, 1, 2, 3, 4, 0, 1, 2, 4]) == [0, 1, 2, 4, 0, 1, 2, 4]
assert checkio([99, 98, 99]) == [99, 99]
assert checkio([0, 0, 0, 1, 1, 100]) == [0, 0, 0, 1, 1]
assert checkio([0, 0, 0, -1, -1, 100]) == [0, 0, 0, -1, -1]

# Answer 3

def flat_list(array):
    new = []
    for l in array:
        if type(l) == int:
            new.append(l)
        else:
            new += flat_list(l)
    return new

if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"

# Answer 4

def goes_after(word: str, first: str, second: str) -> bool:
    res = False
    if first in word and second in word:
        res = word.index(second) - word.index(first) == 1
    return res


print("Example:")
print(goes_after("world", "w", "o"))

assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False

# Answer 5

from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    split = [text[i]+text[i+1] for i in range(0,len(text)-1,2)]
    if len(text)%2 == 1:
        split.append(text[-1] + "_")
        return split
    return split


print("Example:")
print(list(split_pairs("abcd")))

assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]
assert list(split_pairs("")) == []

# Answer 6

def is_all_upper(text: str) -> bool:
    return not True in [ord(text[i]) >= 97 and ord(text[i]) <= 122 for i in range(len(text))]


print("Example:")
print(is_all_upper("ALL UPPER"))

assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == True
assert is_all_upper("444") == True
assert is_all_upper("55 55 5 ") == True