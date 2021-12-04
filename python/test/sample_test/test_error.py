import pytest
from ..sample_code.sample_error import exception_error


def test_error1():
    # eはExceptionInfoクラス
    # https://docs.pytest.org/en/6.2.x/reference.html#id67
    with pytest.raises(Exception):
        exception_error()


# Fail判定
def test_error2():
    # eはExceptionInfoクラス
    # https://docs.pytest.org/en/6.2.x/reference.html#id67
    with pytest.raises(ZeroDivisionError):
        exception_error()


def test_error3():
    # eはExceptionInfoクラス
    # https://docs.pytest.org/en/6.2.x/reference.html#id67
    with pytest.raises(Exception) as e:
        exception_error()

    assert str(e.value) == 'test'
