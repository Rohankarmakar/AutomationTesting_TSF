import unittest
from selenium import webdriver
import sys

sys.path.append("/home/rk/PycharmProjects/Task6_AutomatedTesting")
from pageObjects.links_ai_in_edu import LinksAiPage


class LinksTest(unittest.TestCase):
    expect_heading = "AI In Education"
    links_url = "https://www.thesparksfoundationsingapore.org/links/ai-in-education/"
    chrome = webdriver.Chrome(executable_path="/home/rk/PycharmProjects/Task6_AutomatedTesting/drivers/chromedriver")
    lp = LinksAiPage(chrome)

    @classmethod
    def setUpClass(cls) -> None:
        cls.chrome.get(cls.links_url)
        cls.chrome.maximize_window()

    def test_heading(self):  # will test if the heading is correct
        heading = self.lp.check_heading()
        self.assertTrue(heading.text == self.expect_heading)
        print("The heading is correct.")

    def test_blogLink(self):  # will check the blog link
        lnk = self.lp.check_blog_link()
        self.assertTrue(lnk.is_displayed() == True)
        print("The blog link is available.")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.chrome.quit()
