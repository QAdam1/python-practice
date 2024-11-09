class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def quit(self):
        self.driver.quit()

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    def go_to(self, url):
        self.driver.get(url)