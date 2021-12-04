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


@pytest.fixture
def test_case_2():
    input_data_for_menu = {
        'flag': 3,
        'pattern': 4,
        'result': True
    }
    return input_data_for_menu


def test_fixture_1(test_case_1):
    print('1')
    flag1 = test_case_1.get('flag')
    pattern1 = test_case_1.get('pattern')
    result1 = test_case_1.get('result')

    response = fixture(flag1, pattern1)

    assert response == result1


def test_fixture_2(test_case_2):
    print('2')
    flag2 = test_case_2.get('flag')
    pattern2 = test_case_2.get('pattern')
    result2 = test_case_2.get('result')

    response = fixture(flag2, pattern2)

    assert response == result2


def test_fixture_3(test_case_1, test_case_2):
    print('3')
    flag1 = test_case_1.get('flag')
    pattern1 = test_case_1.get('pattern')
    result1 = test_case_1.get('result')

    response1 = fixture(flag1, pattern1)

    flag2 = test_case_2.get('flag')
    pattern2 = test_case_2.get('pattern')
    result2 = test_case_2.get('result')

    response2 = fixture(flag2, pattern2)

    assert response1 == result1 & response2 == result2
