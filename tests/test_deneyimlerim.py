import time
import pytest
from selenium import webdriver
from pages.deneyimlerim import Deneyimlerim
from pages.giris import *
from pages.PageBase import PageBase
import softest

@pytest.mark.usefixtures("setup")
class TestDeneyimlerim(softest.TestCase,PageBase):

    def test_deneyimlerim_sayfasina_gider(self):
        page_base=PageBase(self.driver)       
        deneyimlerim= Deneyimlerim(self.driver) 
        giris=Giris(self.driver) 
        
        giris.ana_giris()     
        time.sleep(5)
        deneyimlerim.profil_bilgilerim_butonuna_tiklar()  
        time.sleep(3)
        deneyimlerim.deneyimlerim_butonuna_tiklar()

        expected_title="Deneyimlerim"
        expected_url= "https://tobeto.com/profilim/profilimi-duzenle/deneyimlerim"

        self.soft_assert(self.assertEqual,expected_title,page_base.get_title(), "Title Hatali!!")
        self.soft_assert(self.assertEqual,expected_url,page_base.get_URL(),"URL Hatali!!")
        self.assert_all()
        
       
        
        

    @pytest.mark.skip
    def test_deneme(self):
        page_base=PageBase(self.driver)       
        deneyimlerim= Deneyimlerim(self.driver) 
        giris=Giris(self.driver) 
        giris.ana_giris()

        time.sleep(5)
        kullanici_adi=self.driver.find_element(By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button/div[2]")
        kullanici_adi.click()
        PROFIL_BILGILERI_LOCATED=self.driver.find_element(By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")
        PROFIL_BILGILERI_LOCATED.click()
        time.sleep(3)
        deneyimlerim=self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[2]/span[2]")
        deneyimlerim.click()

        time.sleep(5)

    

        