import pytest
from circle_exercise import MyCircle


@pytest.fixture
def circle():
    return MyCircle(5)


def test_ceck_variables(circle):
    assert circle._radius == 5
    assert circle._diameter == 10

def test_check_area(circle):
    area = circle.calculate_area()
    assert area == circle._area
    assert area == 78.53981633974483

def test_check_eq_(circle):
    circle_two = MyCircle(5)
    assert circle == circle_two

def test_check_eq_error(circle):
    with pytest.raises(TypeError) as error:
        circle == 5
        assert error == f'Can only compare two Circles'

def test_check_gt_(circle):
    circle_two = MyCircle(2)
    assert circle > circle_two

def test_check_gt_error(circle):
    with pytest.raises(TypeError) as error:
        circle > 5
        assert error > f'Can only calculate two Circles'

def test_check_lt_(circle):
    circle_two = MyCircle(7)
    assert circle < circle_two

def test_check_lt_error(circle):
    with pytest.raises(TypeError) as error:
        circle < 5
        assert error == f'Can only calculate between two Circles'

def test_check_add_(circle):
    circle_two = MyCircle(5)
    area = circle.area + circle_two.area
    assert circle + circle_two
    assert area == 157.07963267948966

def test_check_add_error(circle):
    with pytest.raises(TypeError) as error:
        circle + 5
        assert error == f'Can only add between two Circles'

def test_properties(circle):
    assert circle._radius == 5
    assert circle._diameter == 10
    assert circle._area ==  78.53981633974483