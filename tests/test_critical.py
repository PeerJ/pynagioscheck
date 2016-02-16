from nagioscheck import NagiosCheck, Status
from nose.tools import raises
from tests import NagiosCheckTest, WouldHaveExitNonZero

class SimplePessimisticCheck(NagiosCheck):
    version = '1.2.3'

    msg = "YOU DUN MADE ME MAD"

    def __init__(self, *args, **kwargs):
        NagiosCheck.__init__(self, *args, **kwargs)

    def check(self, opts, args):
        raise Status('critical', self.msg)

class TestCritical(NagiosCheckTest):
    @raises(WouldHaveExitNonZero)
    def test_critical_returns_nonzero(self):
        self.check_class = SimplePessimisticCheck

        try:
            self.run_check()
        except WouldHaveExitNonZero, e:
            assert e.code == Status.EXIT_CRITICAL
            raise

    def test_critical_does_not_open_with_status_prefix(self):
        self.check_class = SimplePessimisticCheck
        try:
            self.run_check()
        except WouldHaveExitNonZero:
            pass

        assert not self.out.startswith("CRITICAL:")

    def test_critical_output_contains_message(self):
        self.check_class = SimplePessimisticCheck
        try:
            self.run_check()
        except WouldHaveExitNonZero:
            pass

        assert self.out.find(SimplePessimisticCheck.msg) != -1
