class HomePage:
    logo_xpath = "//*[@id='home']/div/div[1]/h1/a/img"
    nav_xpath = '//*[@id="link-effect-3"]/ul'
    link_text = "KNOW MORE"
    top_hover_id = "toTopHover"

    def __init__(self, driver):
        self.driver = driver

    def check_logo(self):
        logo = self.driver.find_element_by_xpath(self.logo_xpath)
        return logo

    def check_navbar(self):
        nav = self.driver.find_element_by_xpath(self.nav_xpath)
        return nav

    def check_link(self):
        lnk = self.driver.find_element_by_link_text(self.link_text)
        return lnk

    def check_top_hover(self):
        ele = self.driver.find_element_by_id(self.top_hover_id)
        return ele
