from StringIO import StringIO

class WouldHaveExitNonZero(Exception):
    def __init__(self, code):
        self.code = code

    def __repr__(self):
        return "%s(%d)" % (self.__class__.__name__, self.code)

class NagiosCheckTest(object):
    def setUp(self):
        self.outio = StringIO()
        self.errio = StringIO()

    def tearDown(self):
        self.errio.close()
        self.outio.close()

    def run_check(self, argv=None):
        try:
            self.check_class(self.outio, self.errio,
                             raise_exception_on_exit).run(argv)
        finally:
            self.out = self.outio.getvalue()
            self.out_lines = self.out.split("\n")

def raise_exception_on_exit(code):
    """Raise an exception instead of exiting fo' real."""
    if code == 0:
        pass
    else:
        raise WouldHaveExitNonZero(code)
