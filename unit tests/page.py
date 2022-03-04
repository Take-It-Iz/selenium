from xml.dom.minidom import Element


# file to store all page classes
class BasePage(object): # parent class for all page classes
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    def is_title_matching(self):
        return "Real Python Tutorials" in self.driver.title

    def click_dropdown_library(self):
        element = self.driver.find_element()
        element.click()