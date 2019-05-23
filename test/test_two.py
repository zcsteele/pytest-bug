from pytest_bug import bug


@bug('skip')
def test_one():
    assert False


@bug('fail', run=True)
def test_two():
    assert False


@bug('pass', run=True)
def test_three():
    assert True
