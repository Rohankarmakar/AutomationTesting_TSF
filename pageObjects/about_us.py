class AboutUs:
    texts_class = "media"

    def __init__(self, driver):
        self.driver = driver

    def check_texts(self):
        elements = self.driver.find_elements_by_class_name(self.texts_class)
        return len(elements)

    def check_page_title(self):
        title = self.driver.title
        return title
