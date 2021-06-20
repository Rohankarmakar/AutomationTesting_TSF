import unittest
from selenium import webdriver
import sys
sys.path.append("/home/rk/PycharmProjects/Task6_AutomatedTesting")
from pageObjects.home_page import HomePage


class HomeTest(unittest.TestCase):
    home_page_url = "https://www.thesparksfoundationsingapore.org/"
    chrome = webdriver.Chrome(executable_path="/home/rk/PycharmProjects/Task6_AutomatedTesting/drivers/chromedriver")
    hp = HomePage(chrome)

    @classmethod
    def setUpClass(cls) -> None:
        cls.chrome.get(cls.home_page_url)
        cls.chrome.maximize_window()

    def test_logo(self):  # This will test if the logo is visible
        logo = self.hp.check_logo()
        self.assertTrue(logo.is_displayed() == True)
        print('The Logo is Displayed.')

    def test_link(self):  # This will check if the link is working
        ln = self.hp.check_link()
        self.assertTrue(ln.is_enabled() == True)
        print("The link is enabled.")

    def test_nav_bar(self):  # Will check the navbar
        nav = self.hp.check_navbar()
        self.assertTrue(nav.is_displayed() == True)
        print("The navbar is available.")

    def test_top_hover(self):  # will test the link to top of the page
        top = self.hp.check_top_hover()
        self.assertTrue(top.is_enabled() == True)
        print("The element to get back to top is available.")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.chrome.close()
