import pytest


@pytest.fixture(scope='session')
def test_case_pattern_1():

    input_data_for_claim = {
        'name': 'ryo',
        'device': 'iPhone SE',
        'result': True
    }

    print('test_case_pattern_1')

    return input_data_for_claim
