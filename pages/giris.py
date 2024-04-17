import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.PageBase import PageBase
from pages.constants.globalConstants import *


@pytest.mark.usefixtures("setup")
class Giris(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def ana_giris(self):
        user_name= self.wait_element_visibility(USERNAME_LOCATED)
        user_name.send_keys("tobeto.0001@gmail.com")
        password = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(PASSWORD_LOCATED))
        password.send_keys("123456")
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, GIRISYAPBUTTON))).click()
        
    
    def gecerli_giris(self):
        self.ana_giris()
        actual_basarili_popup = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(BASARILIPOPUP))
        #assert actual_basarili_popup.text ==  BASARILI_POPUP_TEXT
        return actual_basarili_popup.text
        #self.soft_assert(self.assertEqual, actual_basarili_popup.text, BASARILI_POPUP_TEXT, "Basarili pop up goruntulenemedi.")
        
       
        