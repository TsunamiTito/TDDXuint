from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):
    def setUp(self):
        self.test= WasRun("testMethod")

    def testSetUp(self):
        self.test.run()
        assert("setUp testMethod tearDown" == self.test.log)





TestCaseTest("testRunning").run()
