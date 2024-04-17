import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.PageBase import PageBase
from pages.constants.deneyimlerimConstants import *
from pages.giris import Giris


@pytest.mark.usefixtures("setup")

class Deneyimlerim(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def kullanici_isim_butonuna_tikla(self):       
        kullanici_isim_butonu= self.driver.find_element(By.XPATH,KULLANICI_ISIM_BUTONU)
        kullanici_isim_butonu.click()

    def profil_bilgilerim_butonuna_tiklar(self):
        self.kullanici_isim_butonuna_tikla()
        profil_bilgilerim=self.driver.find_element(By.XPATH,PROFIL_BILGILERI)
        profil_bilgilerim.click()

    def deneyimlerim_butonuna_tiklar(self):
        self.profil_bilgilerim_butonuna_tiklar()
        deneyimlerim=self.driver.find_element(By.XPATH, DENEYIMLERIM)
        deneyimlerim.click()
        


