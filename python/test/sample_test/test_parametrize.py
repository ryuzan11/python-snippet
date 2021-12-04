import pytest
from ..sample_code.sample_add import add


@pytest.mark.parametrize(('x', 'y', 'expected'), [
    (0, 0, 0),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 2),
    (1, 1, 3)
])
def test_parametrize1(x, y, expected):
    res = add(x, y)
    assert res == expected


@pytest.mark.parametrize('x', [1, 2])
@pytest.mark.parametrize('y', [1, 2, 3])
def test_parametrize2(x, y):
    res = add(x, y)
    assert res == x + y
