import pytest
from ..sample_code.sample_fixture import fixture


# @pytest.fixture(autouse=True)で、テストメソッド実行前に常に実行されるフィクスチャになる
@pytest.fixture
def test_case_1():
    input_data_for_menu = {
        'flag': 1,
        'pattern': 8,
        'result': True
    }
    return input_data_for_menu


def test_before_and_after1(test_case_1):
    print('1')
    flag1 = test_case_1.get('flag')
    pattern1 = test_case_1.get('pattern')
    result1 = test_case_1.get('result')

    response = fixture(flag1, pattern1)

    assert response == result1

    return response


def test_before_and_after2():
    print(test_before_and_after1)

    assert test_before_and_after1 is True
