import pytest


def bug(*args, run=False):
    """
    Mark test as a bug
    :param run: bool
    :return: MarkGenerator
    """
    return pytest.mark.bug(*args, run=run)


__all__ = ["bug"]
