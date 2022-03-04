# main file that activates the tests
import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self): # runs at the beginning
        self.driver = webdriver.Chrome("D:\Installations\Software\chromedriver")
        self.driver.get("https://realpython.com/")

    # def test_example(self): # test methods work only if their names start with 'test'
    #     print("this test works fine") # code to be checked
    #     assert True # check if code returns True    

    # def not_a_test(self):
    #     print("this won't work")

    def test_title(self):
        mainPage = page.MainPage()
        assert mainPage.is_title_matching()
        
    def tearDown(self): # runs at the end
        self.driver.close()

if __name__ == "__main__": # if the script is not imported
    unittest.main()
