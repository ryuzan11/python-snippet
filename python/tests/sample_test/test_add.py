from ..sample_code.sample_add import add


def test_add():
    res = add(1, 2)
    assert res == 3
