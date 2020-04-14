# TestCase
class TestCase:
    log = ""

    def __init__(self, name):
        self.name = name

    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        # 以下だと意図しない例外を握りつぶしてしまうためNG
        # try:
        #    method()
        # except Exception:
        #    result.testFailed()
        self.tearDown()
        return result

    def setUp(self):
        pass

    def tearDown(self):
        pass


class TestResult:
    def __init__(self):
        self.runCount = 0
        self.failedCount = 0

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.failedCount += 1

    def summary(self):
        return "{runCount} run, {failedCount} failed".format(
            runCount=self.runCount, failedCount=self.failedCount
        )


# WasRun
class WasRun(TestCase):
    def setUp(self):
        self.log += "setUp "

    def tearDown(self):
        self.log += "tearDown "

    def testMethod(self):
        self.log += "testMethod "

    def testBrokenMethod(self):
        raise Exception


# TestCaseTest
class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert test.log == "setUp testMethod tearDown "

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert "1 run, 0 failed" == result.summary()

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert "1 run, 1 failed" == result.summary()


# Run Test
TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
# raise より例外が発生するためpending
# TestCaseTest("testFailedResult").run()
