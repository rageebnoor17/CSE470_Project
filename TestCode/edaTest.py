import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
class SearchText(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://127.0.0.1:8000/")

    def test_navbar(self):
        # get the search textbox
        self.driver.find_element_by_id("AboutPage").click()
        
        
        self.driver.find_element_by_id("HomePage").click()
        
        
        self.assertTrue(True)
        
        
    def test_eda(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_id("path")
        
        filepath= "/Users/rageeb_noor/Downloads/arcive/Iris.csv"
        
        
        self.search_field.clear()
        
        self.search_field.send_keys(filepath)
        
        
        self.driver.find_element_by_id("SetPath").click()   
        
        self.driver.find_element_by_id("getColumnNames").click()
        
        
        
        Select(self.driver.find_element_by_id("varData")).select_by_visible_text('Species')

        
        self.driver.find_element_by_id("SelectButton").click()

        
        self.assertTrue(True)
        

    def tearDown(self):
        # close the browser window
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()        
