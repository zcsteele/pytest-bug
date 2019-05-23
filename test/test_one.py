import pytest


@pytest.mark.bug('skip')
def test_one():
    assert False


@pytest.mark.bug('run fail', run=True)
def test_two():
    assert False


@pytest.mark.bug('run pass', run=True)
def test_three():
    assert True
