import unittest
from selenium import webdriver
import sys

sys.path.append("/home/rk/PycharmProjects/Task6_AutomatedTesting")
from pageObjects.about_us import AboutUs


class TestAboutUs(unittest.TestCase):
    all_texts = 5
    page_title = "The Sparks Foundation | Home"
    page_url = "https://www.thesparksfoundationsingapore.org/about/guiding-principles/"
    chrome = webdriver.Chrome(executable_path="/home/rk/PycharmProjects/Task6_AutomatedTesting/drivers/chromedriver")
    about = AboutUs(chrome)

    @classmethod
    def setUpClass(cls) -> None:
        cls.chrome.get(cls.page_url)
        cls.chrome.maximize_window()

    def test_texts(self):  # will check all the paras under guiding principle are present or not
        num = self.about.check_texts()
        self.assertTrue(num == self.all_texts)
        print("All Paragraphs are present.")

    def test_title(self):  # will check the title of the page
        title = self.about.check_page_title()
        self.assertTrue(title == self.page_title)
        print("The page title is Correct")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.chrome.quit()
