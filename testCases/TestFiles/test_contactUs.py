import unittest
from selenium import webdriver
import sys

sys.path.append("/home/rk/PycharmProjects/Task6_AutomatedTesting")
from pageObjects.contact_us import ContactUs


class TestContactUs(unittest.TestCase):
    correct_link = "https://www.linkedin.com/groups/10379184/"
    page_url = "https://www.thesparksfoundationsingapore.org/contact-us/"
    num = "+65-8402-8590"
    mail = "info@thesparksfoundation.sg"
    chrome = webdriver.Chrome(executable_path="/home/rk/PycharmProjects/Task6_AutomatedTesting/drivers/chromedriver")
    contact = ContactUs(chrome)

    @classmethod
    def setUpClass(cls) -> None:
        cls.chrome.get(cls.page_url)
        cls.chrome.maximize_window()

    def test_linkedin_link(self):  # will test the linked in link
        link = self.contact.check_linkedin_link()
        self.assertTrue(link == self.correct_link)
        print("Linked In link is correct.")

    def test_contact(self):  # will test the contact details
        number, con_mail = self.contact.check_contact_details()
        self.assertTrue(number == self.num)
        self.assertTrue(con_mail == self.mail)
        print("Provided Contact details are correct.")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.chrome.quit()
