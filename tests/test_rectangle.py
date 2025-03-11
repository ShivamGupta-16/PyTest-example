import math
import pytest
import source.shapes as shapes



def test_area(my_rectangle):
    assert my_rectangle.area() == 10*20

def test_parameter(my_rectangle):
    assert my_rectangle.parameter() == 2 * (10+20)


def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle
