# TestCase
class TestCase:
    log = ""

    def __init__(self, name):
        self.name = name

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()

    def setUp(self):
        pass

    def tearDown(self):
        pass


# WasRun
class WasRun(TestCase):
    def setUp(self):
        self.log += "setUp "

    def tearDown(self):
        self.log += "tearDown "

    def testMethod(self):
        self.log += "testMethod "


# TestCaseTest
class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert test.log == "setUp testMethod tearDown "


# Run Test
TestCaseTest("testTemplateMethod").run()
