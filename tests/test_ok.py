from nagioscheck import NagiosCheck, Status
from tests import NagiosCheckTest

class SimpleOptimisticCheck(NagiosCheck):
    version = '1.2.3'

    msg = "SUNSHINE LOLLIPOPS"

    def __init__(self, *args, **kwargs):
        NagiosCheck.__init__(self, *args, **kwargs)

    def check(self, opts, args):
        raise Status('ok', self.msg)

class TestOk(NagiosCheckTest):
    def test_ok_does_not_open_with_status_prefix(self):
        self.check_class = SimpleOptimisticCheck
        self.run_check()

        assert not self.out.startswith("OK:")

    def test_ok_output_contains_message(self):
        self.check_class = SimpleOptimisticCheck
        self.run_check()

        assert self.out.find(SimpleOptimisticCheck.msg) != -1
