class ContactUs:
    linked_in_xpath = "/html/body/div[2]/div/div/div[1]/div[1]/p/span/a"
    contact_xpath = "/html/body/div[2]/div/div/div[3]/div[2]/p[2]"

    def __init__(self, driver):
        self.driver = driver

    def check_linkedin_link(self):
        link = self.driver.find_element_by_xpath(self.linked_in_xpath).get_attribute('href')
        return str(link)

    def check_contact_details(self):
        elem = self.driver.find_element_by_xpath(self.contact_xpath)
        details = str(elem.text)
        num, mail = details.split(',')
        return num, mail.lstrip()
