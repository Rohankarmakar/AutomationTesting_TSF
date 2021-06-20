import unittest
from selenium import webdriver
import sys

sys.path.append("/home/rk/PycharmProjects/Task6_AutomatedTesting")
from pageObjects.join_us import JoinUs


class TestJoinUs(unittest.TestCase):
    after_submit_url = "https://www.thesparksfoundationsingapore.org/join-us/why-join-us/#"
    page_url = "https://www.thesparksfoundationsingapore.org/join-us/why-join-us/"
    chrome = webdriver.Chrome(executable_path="/home/rk/PycharmProjects/Task6_AutomatedTesting/drivers/chromedriver")
    join = JoinUs(chrome)

    @classmethod
    def setUpClass(cls) -> None:
        cls.chrome.get(cls.page_url)
        cls.chrome.maximize_window()

    def test_submission(self):  # this will check the contact detail submission
        url = self.join.check_detail_submission()
        self.assertTrue(str(url) == self.after_submit_url)
        print("Contact information submitted perfectly.")

    def test_intern_link(self):  # will check if the internship programs link is present
        intern = self.join.check_internship_link()
        self.assertTrue(intern.is_enabled() == True)
        print("Internship programs link is present.")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.chrome.quit()
