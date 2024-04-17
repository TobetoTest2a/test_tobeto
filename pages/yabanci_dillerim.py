import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.PageBase import PageBase
from pages.constants.yabanciDillerimConstants import *
from pages.giris import Giris


@pytest.mark.usefixtures("setup")
class Yabanci_dil_ekle(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    def profilim_kismina_tikla(self):
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, PROFILIMBUTTON))).click()
    
    def profil_bilgileri_tikla(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, PROFILBILGILERIMBUTTON))).click()
        time.sleep(7)
    
    def yabanci_dillerim_tikla(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, YABANCIDILLERIM_BUTTON))).click()
        time.sleep(7)

    def dil_acilirmenu_tikla(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, YABANCIDIL_ACILIRMENU))).click()
        time.sleep(5)

    def yabancidil_sec(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ALMANCASEC))).click()
        time.sleep(5)
    
    def seviye_acilirmenu_tikla(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, SEVIYESEC_ACILIRMENU))).click()
        time.sleep(5)
    
    def seviye_sec(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, SEVIYESEC))).click()
        time.sleep(5)

    def kaydet(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, KAYDET_BUTTON))).click()
        time.sleep(5)

    def kaydetme_basarili(self):
        actual_result_message = WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, SAVE_POPUP_MESSAGE)))
        assert actual_result_message.text


class Yabanci_dil_bos_gecme(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    
    def profilim_kismina_tikla(self):
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, PROFILIMBUTTON))).click()
    
    def profil_bilgileri_tikla(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, PROFILBILGILERIMBUTTON))).click()
        time.sleep(5)
    
    def yabanci_dillerim_tikla(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, YABANCIDILLERIM_BUTTON))).click()
        time.sleep(5)

    def dil_acilirmenu_tikla(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, YABANCIDIL_ACILIRMENU))).click()
        time.sleep(5)

    def yabancidil_sec(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ALMANCASEC))).click()
        time.sleep(5)
    
    def seviye_acilirmenu_tikla(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, SEVIYESEC_ACILIRMENU))).click()
        time.sleep(5)

    def kaydet(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, KAYDET_BUTTON))).click()
        time.sleep(5)

    def doldurulmasi_zorunlu_alan_mesaji(self):
        actual_result_message = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(BLANK_MESSAGE))
        assert actual_result_message.text == BLANK_MESSAGE_TEXT

    
        

 
        