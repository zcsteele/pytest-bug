# pytest-bug

[![Build Status](https://travis-ci.com/tolstislon/pytest-bug.svg?branch=master)](https://travis-ci.com/tolstislon/pytest-bug)
![support](https://img.shields.io/badge/python-3.6%20%7C%203.7%20-blue.svg)
![pytes_support](https://img.shields.io/badge/pytest-%3E%3D3.6.0-blue.svg)


```python
import pytest

@pytest.mark.bug('fail not calling exit code', run=True)
def test_one():
    assert False

```

or

```python
from pytest_bug import bug

@bug('fail not calling exit code', run=True)
def test_one():
    assert False
```