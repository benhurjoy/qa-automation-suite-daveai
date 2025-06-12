from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
class UnitTesting(unittest.TestCase):
    def setUp(self):  #setup function
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.iamdave.ai/")
        self.driver.maximize_window()
    def test_title(self): # testing title
        self.assertIn("DaveAI", self.driver.title)
    def test_book_demo_button_presence(self):# testing buttonpresence
           button=self.driver.find_element(By.CLASS_NAME,"vamtam-btn-text" ) #filtering by classname
           self.assertTrue(button.is_displayed(),"book a demo button is not visible") 
    def test_navigation_button(self):#testing naviagtion flow
        old_url=self.driver.current_url
        book_demo=self.driver.find_element(By.CLASS_NAME,"vamtam-btn-text" )#filtering by classname
        book_demo.click()
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url != old_url)# to wait until form fields are present
        new_url=self.driver.current_url
        self.assertNotEqual(old_url, new_url, "Page did not navigate")
    def test_input_fields_exist(self):#testing input field exists
        driver = self.driver

        # TO Click the 'Book Demo' button
        book_demo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "vamtam-btn-text"))
        )
        book_demo.click()

        # To Wait until form fields are present
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "form-field-name_free_audit"))
        )
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "form-field-email"))
        )

        # Assert fields are visible
        self.assertTrue(username_field.is_displayed())
        self.assertTrue(email_field.is_displayed())
    def tearDown(self):#closing the webdriver
         self.driver.quit()
if __name__ == "__main__":
    unittest.main()
 
        



