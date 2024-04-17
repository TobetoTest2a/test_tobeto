import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.PageBase import PageBase
from pages.constants.kisisel_bilgilerim_constants import *
from pages.giris import Giris
from time import sleep

@pytest.mark.usefixtures("setup")
class kisisel_bilgiler(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def profil_olustur_butonuna_tikla(self):
        sleep(1)
        profil_olustur_butonu = self.wait_element_visibility(PROFILI_OLUSTUR_BUTTON_LOCATED)
        profil_olustur_butonu.click()
        sleep(4)

    def sayfayi_asagi_indir(self):
        self.driver.execute_script("scrollBy(0,1000)")

    def get_title(self):
        return self.driver.title
    
    def anasayfa_butonuna_tikla(self):
        anasayfa_butonu = self.wait_element_visibility(ANASAYFA_BUTONU_LOCATED)
        anasayfa_butonu.click()

    def kullanici_adi_butonuna_tikla(self):
        kullanici_adi_butonu = self.wait_element_visibility(KULLANICI_ADI_BUTONU_LOCATED)
        kullanici_adi_butonu.click()
        sleep(2)

    def kullanici_adi_menusundeki_profil_bilgilerine_tikla(self):
        profil_bilgileri_butonu = self.wait_element_visibility(PROFIL_BILGILERI_LOCATED)
        profil_bilgileri_butonu.click()
        sleep(2)
    
    def sol_menude_goruntule(self):
        expected_sol_menu = ["Kişisel Bilgilerim", "Deneyimlerim", "Eğitim Hayatım", "Yetkinliklerim", "Sertifikalarım", "Medya Hesaplarım", "Yabancı Dillerim", "Ayarlar"]
        return expected_sol_menu 
        