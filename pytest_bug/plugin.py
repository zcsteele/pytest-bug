import enum

import pytest

__version__ = '0.1.1'

BUG = '_mark_bug'


class MARKS(enum.Enum):
    SKIP = 'b'
    FAIL = 'f'
    PASS = 'p'
    UNKNOWN = 'u'


def bug_mark(*args, run=False, **kwargs):
    com = [str(i) for i in args]
    com.extend(str(i) for i in kwargs.values())
    return ', '.join(com), run


class PyTestBug:

    def __init__(self, config):
        self.config = config
        self._skipped = 0
        self._failed = 0
        self._passed = 0

    def counter(self, mark):
        if mark is MARKS.SKIP:
            self._skipped += 1
        elif mark is MARKS.FAIL:
            self._failed += 1
        elif mark is MARKS.PASS:
            self._passed += 1

    @staticmethod
    def set_mark(obj, mark=MARKS.UNKNOWN):
        setattr(obj, BUG, mark)

    def pytest_runtest_setup(self, item):
        for i in item.iter_markers(name='bug'):
            comment, run = bug_mark(*i.args, **i.kwargs)
            if not run:
                self.set_mark(item, MARKS.SKIP)
                pytest.skip(comment)
            else:
                self.set_mark(item)

    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(self, item):
        outcome = yield
        rep = outcome.get_result()
        mark = getattr(item, BUG, None)
        if mark:
            if rep.skipped:
                self.set_mark(rep, MARKS.SKIP)
            if rep.when == 'call':
                if rep.passed:
                    self.set_mark(rep, MARKS.PASS)
                elif rep.failed:
                    rep.outcome = "skipped"
                    eval_fail = getattr(item, "_evalxfail", None)
                    if eval_fail is not None:
                        rep.wasxfail = eval_fail.getexplanation()
                        self.set_mark(rep, MARKS.FAIL)

    def pytest_report_teststatus(self, report):
        mark = getattr(report, BUG, None)
        if mark:
            self.counter(mark)
            return report.outcome, mark.value, report.outcome.upper()

    def pytest_terminal_summary(self, terminalreporter):
        terminalreporter.write_sep(
            '-',
            'Bugs skipped: {0}, Bugs passed: {1}, Bugs failed: {2}'.format(self._skipped, self._passed, self._failed)
        )
