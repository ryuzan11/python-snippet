import pytest


#  pytest -s --days=1 --capture=no
# TODO 名前別ではだめ？
# TODO 下層のconftest.pyで定義した場合はどうなる？
def pytest_addoption(parser):
    parser.addoption('--days', action='store', default='all')


# トップレベルのconftestにscope='session'を設定すると、テストが実行される前に1度呼び出され、それをテストコード全体で使いまわせる
@pytest.fixture(scope='session')
def test_case_pattern_top_1(request):
    print('days', request.config.getoption('--days'))

    input_data_for_claim = {
        'name': 'ryo',
        'device': 'iPhone SE',
        'result': True
    }

    print('test_case_pattern_top_1')

    return input_data_for_claim
