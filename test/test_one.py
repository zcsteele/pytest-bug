import pytest


@pytest.mark.bug('skip')
def test_one():
    assert False


@pytest.mark.bug('fail', run=True)
def test_two():
    assert False


@pytest.mark.bug('pass', run=True)
def test_three():
    assert True
