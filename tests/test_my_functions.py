import pytest
import time
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(1,2)
    assert result ==3

def test_divide():
    result = my_functions.divide(10,2)
    assert result ==5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(5,0)

def test_add_strings():
    result = my_functions.add("I like ","Dosa")
    assert result == "I like Dosa"


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(10,5)
    assert result == 2

@pytest.mark.skip(reason = "This feature is currently broken")
def test_add():
    result = my_functions.add(1,2)
    assert result ==3

@pytest.mark.xfail(reason = "We know we cannot divide by zero")
def test_divide_zero_broken():
    my_functions.divide(4,0)