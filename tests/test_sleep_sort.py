import pytest
import src.sleep_sort as sleep_sort

def test_is_sorted_simple():
    sleep_sort.sort([5, 3, 1, 4, 2])
    assert sleep_sort.sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]
    

def test_pre_sorted():
    sleep_sort.sort([5, 3, 1, 4, 2])
    assert sleep_sort.sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    