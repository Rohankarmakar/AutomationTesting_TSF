from selenium.webdriver.support.ui import Select


class JoinUs:
    class_drp = "form-control"
    submit_xpath = "/html/body/div[2]/div/div[2]/div[2]/div/form/input[3]"
    internship = "/html/body/div[2]/div/div[2]/div[1]/ul/li[5]/a"

    def __init__(self, driver):
        self.driver = driver

    def check_detail_submission(self):
        self.driver.find_element_by_name("Name").send_keys("Rohan Tester")
        self.driver.find_element_by_name("Email").send_keys("xyz@gmail.com")
        elem = self.driver.find_element_by_class_name(self.class_drp)
        drp = Select(elem)
        drp.select_by_index(1)
        self.driver.find_element_by_xpath(self.submit_xpath).click()
        return self.driver.current_url

    def check_internship_link(self):
        link = self.driver.find_element_by_xpath(self.internship)
        return link
