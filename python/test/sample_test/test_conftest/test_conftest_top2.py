from ...sample_code.sample_fixture import fixture


def test_conftest_2(test_case_pattern_top_1):
    name = test_case_pattern_top_1.get('name')
    device = test_case_pattern_top_1.get('device')
    result = test_case_pattern_top_1.get('result')

    response = fixture(name, device)

    assert response == result
