import unittest
import sys
import HtmlTestRunner

sys.path.append("/home/rk/PycharmProjects/Task6_AutomatedTesting")
from testCases.TestFiles.test_homepage import HomeTest
from testCases.TestFiles.test_links_ainedu import LinksTest
from testCases.TestFiles.test_contactUs import TestContactUs
from testCases.TestFiles.test_joinUs import TestJoinUs
from testCases.TestFiles.test_aboutUs import TestAboutUs

tc1 = unittest.TestLoader().loadTestsFromTestCase(HomeTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(LinksTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(TestContactUs)
tc4 = unittest.TestLoader().loadTestsFromTestCase(TestJoinUs)
tc5 = unittest.TestLoader().loadTestsFromTestCase(TestAboutUs)

finalTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5])
report = "/home/rk/PycharmProjects/Task6_AutomatedTesting/reports"

runner = HtmlTestRunner.HTMLTestRunner(output=report, report_title="TSF Test Report")
runner.run(finalTestSuite)  # This will run all the test files
