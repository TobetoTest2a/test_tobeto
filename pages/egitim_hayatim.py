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
        
    def kaydet_butonuna_tikla(self):
        self.wait_element_visibility(KAYDET_BUTONU).click()
        time.sleep(2)

    def doldurulmasi_zorunlu_alan_uyari_mesaji(self):
        beklenen_mesaj =self.wait_element_presence(UYARI_MESAJI)
        assert beklenen_mesaj.text == UYARI_MESAJI_TEXT
        time.sleep(2)
    
class Egitim_hayatim_ekle(PageBase):
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def kullanici_butonuna_tikla(self):  
        self.wait_element_visibility(KULLANICI_BUTTON).click()
        time.sleep(5)

    def profil_bilgilerine_tikla(self):
        self.wait_element_visibility(PROFIL_BIGLILERI_BUTTON).click()
       
    def egitim_hayatim_butonuna_tiklar(self):
        self.wait_element_visibility(EGITIM_HAYATIM).click()
        time.sleep(2)
    
    def egitim_durumuna_tikla(self):
        self.wait_element_visibility(EGITIM_DURUMU_BUTONU).click()
        time.sleep(2)

    def egitim_durumu_sec(self):
        self.wait_element_visibility(LISANS_SEC).click()
        time.sleep(2)
    
    def universite_adi_yaz(self):
        universite_adi_yaz = self.wait_element_visibility(UNIVERSITE)
        universite_adi_yaz.send_keys(UNIVERSITE_ADI)
        time.sleep(2)

    def bolum_adi_yaz(self):
        bolum_adi_yaz = self.wait_element_visibility(BOLUM)
        bolum_adi_yaz.send_keys(BOLUM_ADI)
        time.sleep(2)

    def baslangic_yili_tikla(self):
        self.wait_element_visibility(BASLAMA_YILI_BUTONU).click()
        time.sleep(2)

    def baslangic_yili_sec(self):
        self.wait_element_visibility(BASLAMA_YILI_SEC).click()
        time.sleep(2)

    def mezuniyet_yili_tikla(self):
        self.wait_element_visibility(MEZUNIYET_YILI).click()
        time.sleep(2)

    def mezuniyet_yili_sec(self):
        self.wait_element_visibility(MEZUNIYET_YILI_SEC).click()
        time.sleep(2)

    def kaydet_butonuna_tikla(self):
        self.wait_element_visibility(KAYDET_BUTONU).click()
        time.sleep(2)
    
    def universite_kaydi_basarili_popup_mesaji(self):
        beklenen_mesaj =self.wait_element_presence(BASARILI_POPUP_MESAJ)
        assert beklenen_mesaj.text == BASARILI_POPUP_MESAJI_TEXT
        time.sleep(2)
    
class Universiteye_devam_ediyor_butonu(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
       

    def kullanici_butonuna_tikla(self):  
        self.wait_element_visibility(KULLANICI_BUTTON).click()
        time.sleep(5)

    def profil_bilgilerine_tikla(self):
        self.wait_element_visibility(PROFIL_BIGLILERI_BUTTON).click()
       
    def egitim_hayatim_butonuna_tiklar(self):
        self.wait_element_visibility(EGITIM_HAYATIM).click()
        time.sleep(2)
    
    def egitim_durumuna_tikla(self):
        self.wait_element_visibility(EGITIM_DURUMU_BUTONU).click()
        time.sleep(2)

    def egitim_durumu_sec(self):
        self.wait_element_visibility(LISANS_SEC).click()
        time.sleep(2)
    
    def universite_adi_yaz(self):
        universite_adi_yaz = self.wait_element_visibility(UNIVERSITE)
        universite_adi_yaz.send_keys(UNIVERSITE_ADI)
        time.sleep(2)

    def bolum_adi_yaz(self):
        bolum_adi_yaz = self.wait_element_visibility(BOLUM)
        bolum_adi_yaz.send_keys(BOLUM_ADI_DEVAM)
        time.sleep(2)

    def baslangic_yili_tikla(self):
        self.wait_element_visibility(BASLAMA_YILI_BUTONU).click()
        time.sleep(2)

    def baslangic_yili_sec(self):
        self.wait_element_visibility(BASLAMA_YILI_SEC).click()
        time.sleep(2)

    def universiteye_devam_ediyorum_butonuna_tikla(self):
        self.wait_element_visibility(UNIVERSITEYE_DEVAM_EDIYORUM_BUTONU).click()
        time.sleep(2)

    def kaydet_butonuna_tikla(self):
        self.wait_element_visibility(KAYDET_BUTONU).click()
        time.sleep(2)
    
    def universite_kaydi_basarili_popup_mesaji(self):
        beklenen_mesaj =self.wait_element_presence(BASARILI_POPUP_MESAJ)
        assert beklenen_mesaj.text == BASARILI_POPUP_MESAJI_TEXT
        time.sleep(2)
    
class Kayit_Edilen_Universiteyi_Silme(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
       

    def kullanici_butonuna_tikla(self):  
        self.wait_element_visibility(KULLANICI_BUTTON).click()
        time.sleep(5)

    def profil_bilgilerine_tikla(self):
        self.wait_element_visibility(PROFIL_BIGLILERI_BUTTON).click()
       
    def egitim_hayatim_butonuna_tiklar(self):
        self.wait_element_visibility(EGITIM_HAYATIM).click()
        time.sleep(2)
    
    def sayfayi_asagi_kaydir (self):
        self.driver.execute_script("scrollBy(0,2000)")
        time.sleep(5)
   
    def universite_kaydini_sil(self):
        self.wait_element_visibility(KAYDI_SIL).click()
        time.sleep(2)

    
    def egitimi_silmek_istediginize_eminmisiniz_popup_mesaji(self):
        beklenen_mesaj =self.wait_element_visibility(KAYIT_SILMEYE_EMINMISIN_MESAJI)
        assert beklenen_mesaj.text == KAYIT_SILMEYE_EMINMISIN_MESAJI_TEXT
        time.sleep(2)

    def evet_butonuna_tikla(self):
        self.wait_element_visibility(EVET_BUTONU).click()

    def kayit_silme_basarili_popup_mesaji(self):
        beklenen_mesaj=self.wait_element_visibility(KAYIT_SILME_BASARILI)
        assert beklenen_mesaj.text == KAYIT_SILME_BASARILI_TEXT