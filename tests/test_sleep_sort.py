import pytest
import src.sleep_sort as sleep_sort

def test_is_sorted_simple():
    assert sleep_sort.sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]
    

def test_pre_sorted():
    assert sleep_sort.sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    

def test_neg_pre_sort():
    assert sleep_sort.sort([-5,-4,-3,-2,-1]) == (-5,-4,-3,-2,-1)
    
    
def test_neg_sort_simple():
    assert sleep_sort.sort([-4,-1,-3,-5,-2]) == (-5,-4,-3,-2,-1)