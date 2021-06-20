class LinksAiPage:
    ai_link = "/html/body/div[2]/div/div[1]/div/div[1]/div/div/div[1]/div/a"

    heading_xpath = '//*[@id="home"]/div/div[2]/h2'

    def __init__(self, driver):
        self.driver = driver

    def check_blog_link(self):
        link = self.driver.find_element_by_xpath(self.ai_link)
        return link

    def check_heading(self):
        heading = self.driver.find_element_by_xpath(self.heading_xpath)
        return heading
