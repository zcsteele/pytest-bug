import pytest


def bug(*args, run=False):
    """Mark test as a bug"""
    return pytest.mark.bug(*args, run=run)


__all__ = ["bug"]
