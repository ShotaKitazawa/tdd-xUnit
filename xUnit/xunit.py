# TestCase
class TestCase:
    wasRun = None
    wasSetUp = None

    def __init__(self, name):
        self.name = name

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

    def setUp(self):
        pass


# WasRun
class WasRun(TestCase):
    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1

    def testMethod(self):
        self.wasRun = 1


# TestCaseTest
class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testRunning(self):
        # assert not test.wasRun # testSetUp のテストが通るならここのテストは要らないらしい？？納得できない
        self.test.run()
        assert self.test.wasRun

    def testSetUp(self):
        # assert not test.wasSetUp # 要るのでは？
        # assert not test.wasRun # 責務外
        self.test.run()
        assert self.test.wasSetUp
        # assert test.wasRun # 責務外


# Run Test
TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
