import pytest


@pytest.fixture()
def start_test():
    print('Run')
    yield
    print('End Run')


@pytest.fixture(scope='session')
def hello():
    print('START')
    yield
    print('END')