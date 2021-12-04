import pytest
from ..sample_code.sample_fixture import fixture


@pytest.fixture
def after_print():

    input_data_for_menu = {
        'flag': 1,
        'pattern': 8,
        'result': True
    }

    yield input_data_for_menu

    print('最後に出力される')


def test_after_fixture(after_print):
    flag = after_print.get('flag')
    pattern = after_print.get('pattern')
    result = after_print.get('result')

    response = fixture(flag, pattern)

    assert response == result
