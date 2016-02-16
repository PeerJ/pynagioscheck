from nagioscheck import NagiosCheck, PerformanceMetric, Status
from tests import NagiosCheckTest, WouldHaveExitNonZero

class SimpleOptimisticCheck(NagiosCheck):
    version = '1.2.3'

    msg = "SUNSHINE LOLLIPOPS"

    def __init__(self, *args, **kwargs):
        NagiosCheck.__init__(self, *args, **kwargs)

    def check(self, opts, args):
        raise Status('ok', self.msg)

class SimplePerfdataCheck(NagiosCheck):
    version = '1.2.3'

    msg = "Sumfin dun broke"

    def __init__(self, *args, **kwargs):
        NagiosCheck.__init__(self, *args, **kwargs)

    def check(self, opts, args):
        raise Status('critical',
                     (self.msg,
                      None,
                      self.msg + "\n" + self.lines()),
                      PerformanceMetric('flibs', 10))

    def lines(self):
        """Return a multi-line string to simulate multi-line plugin 
        output."""
        # 0
        # 1
        # [...]
        # 4
        return "\n".join(map(lambda i: str(i), range(5)))

class TestPerfdata(NagiosCheckTest):
    def test_no_perfdata_by_default(self):
        self.check_class = SimpleOptimisticCheck
        self.run_check()

        assert self.out_lines[0].find("|") == -1

    def test_perfdata_on_first_line(self):
        self.check_class = SimplePerfdataCheck
        try:
            self.run_check(argv=["check_perfdata", "-vv"])
        except WouldHaveExitNonZero:
            pass

        # Test that perfdata appears where it is supposed to appear...
        assert self.out_lines[0].find("|") != -1
        assert self.out_lines[0].find("flibs=10;;;;;") != -1

        # ...and not where it is not supposed to appear.
        for line in self.out_lines[1:]:
            assert line.find("|") == -1
