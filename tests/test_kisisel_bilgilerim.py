import time
import pytest
from selenium import webdriver
from pages.kisisel_bilgilerim import *
from pages.giris import *
from pages.PageBase import PageBase
import softest

@pytest.mark.usefixtures("setup")
class TestTobetoKisisel(softest.TestCase,PageBase):
    
    def test_kisisel_bilgilerim(self):
        giris_yap = Giris(self.driver)
        profil_olustur = kisisel_bilgiler(self.driver) 
        giris_yap.ana_giris()
        time.sleep(2)
        profil_olustur.sayfayi_asagi_indir()
        profil_olustur.profil_olustur_butonuna_tikla()
        profil_olustur.anasayfa_butonuna_tikla()
        profil_olustur.kullanici_adi_butonuna_tikla()
        profil_olustur.kullanici_adi_menusundeki_profil_bilgilerine_tikla()
        profil_olustur.sol_menude_goruntule()
        actual_result = self.webelement_listesinden_string_listesi_ver(SOL_MENU_LOCATED)
        self.soft_assert(self.assertEqual,profil_olustur.sol_menude_goruntule(),actual_result,"Hataaaaa") 
        self.assert_all()



        

        

        