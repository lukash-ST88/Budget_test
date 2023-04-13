import pytest


# # function  Run once per test
# # class	    Run once per class of tests
# # module	  Run once per module
# # session	  Run once per session

@pytest.fixture(scope='session')
def fixture_1():
    print('run-fixutre1')
    return 1


def test_ex2(fixture_1):
    print('run-ex2')
    num = fixture_1
    assert num == 1


@pytest.fixture
def yield_fixture():
    print('Start Test Phase')
    yield 6
    print('End Test Phase')


def test_example(yield_fixture):
    print('run-example-1')
    assert yield_fixture == 6
