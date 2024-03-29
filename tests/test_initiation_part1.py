from src.initiation_part1 import mult_two
from src.initiation_part1 import checkio
from src.initiation_part1 import flat_list
from src.initiation_part1 import goes_after
from src.initiation_part1 import split_pairs
from src.initiation_part1 import is_all_upper

def test_mult_two():
    assert mult_two(3, 2) == 6
    assert mult_two(0, 1) == 0
    
def test_checkio():
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
    
def test_flat_list():
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"

def test_goes_after():
    assert goes_after("world", "w", "o") == True
    assert goes_after("world", "w", "r") == False
    assert goes_after("world", "l", "o") == False
    assert goes_after("panorama", "a", "n") == True
    assert goes_after("list", "l", "o") == False
    assert goes_after("", "l", "o") == False
    assert goes_after("list", "l", "l") == False
    assert goes_after("world", "d", "w") == False
    
def test_split_pairs():
    assert list(split_pairs("abcd")) == ["ab", "cd"]
    assert list(split_pairs("abc")) == ["ab", "c_"]
    assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
    assert list(split_pairs("a")) == ["a_"]
    assert list(split_pairs("")) == []
    
def test_is_all_upper():
    assert is_all_upper("ALL UPPER") == True
    assert is_all_upper("all lower") == False
    assert is_all_upper("mixed UPPER and lower") == False
    assert is_all_upper("") == True
    assert is_all_upper("444") == True
    assert is_all_upper("55 55 5 ") == True
    
