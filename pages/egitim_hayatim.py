import time
import pytest
from pages.PageBase import PageBase
from pages.constants.egitimHayatimConstants import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

@pytest.mark.usefixtures("setup")
class EgitimHayatim(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        time.sleep(5)

    def kullanici_butonuna_tikla(self):  
        self.wait_element_visibility(KULLANICI_BUTTON).click()
        time.sleep(5)

    def profil_bilgilerine_tikla(self):
        self.wait_element_visibility(PROFIL_BIGLILERI_BUTTON).click()
       
    def egitim_hayatim_butonuna_tiklar(self):
        self.wait_element_visibility(EGITIM_HAYATIM).click()
        time.sleep(2)
    
 