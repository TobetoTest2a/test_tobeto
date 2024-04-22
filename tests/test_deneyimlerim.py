import time
import pytest
from selenium import webdriver
from pages.deneyimlerim import Deneyimlerim
from pages.constants.deneyimlerimConstants import *
from pages.giris import *
from pages.PageBase import PageBase
import softest


@pytest.mark.usefixtures("setup")
class TestDeneyimlerim(softest.TestCase,PageBase):
   

    # Deneyimlerim sayfasine ulasir.
    def test_deneyimlerim_sayfasina_gider(self):       
        deneyimlerim= Deneyimlerim(self.driver) 
        giris=Giris(self.driver) 
        
        giris.ana_giris()
        time.sleep(8)
        deneyimlerim.kullanici_isim_butonuna_tikla()
        time.sleep(3)
        deneyimlerim.profil_bilgilerim_butonuna_tiklar()     
        time.sleep(3)
        deneyimlerim.deneyimlerim_butonuna_tiklar()
        

    # Deneyimlerim sayfasine ulastigini dogrular.
    @pytest.mark.skip
    def test_deneyimlerim_sayfasina_gittigini_dogrular(self):
        page_base=PageBase(self.driver) 
        self.test_deneyimlerim_sayfasina_gider()

        expected_title="Deneyimlerim"
        expected_url= "https://tobeto.com/profilim/profilimi-duzenle/deneyimlerim"

        self.soft_assert(self.assertEqual,expected_title,page_base.get_title(), "Title Hatali!!")
        self.soft_assert(self.assertEqual,expected_url,page_base.get_URL(),"URL Hatali!!")
        self.assert_all()
        
    # Basarili senaryo deneyim ekler.
    
    def test_basarili_deneyim_ekler(self):
        deneyimlerim= Deneyimlerim(self.driver)

        self.test_deneyimlerim_sayfasina_gider()
        time.sleep(3)
        deneyimlerim.kurum_adi_textbox_deger_girer()
        time.sleep(5)
        deneyimlerim.pozisyon_textbox_deger_girer()
        time.sleep(2)
        deneyimlerim.sektor_textbox_deger_girer()
        time.sleep(2)
        deneyimlerim.sehir_seciniz_dropdown_sehir_secimi_yapar()
        time.sleep(3)
        deneyimlerim.is_baslangic_tarihine_deger_girer()
        time.sleep(10)
        deneyimlerim.is_bitis_tarihi_deger_girer()
        time.sleep(3)
        deneyimlerim.is_aciklamasi_texbox_deger_girer()
        time.sleep(3)
        deneyimlerim.kaydet_butonuna_tiklar()
        time.sleep(3)
        expected_mesaj="• Deneyim eklendi."
        self.soft_assert(self.assertEqual,expected_mesaj,deneyimlerim.basari_mesaji(),"MESAJ Hatali!!")
        self.assert_all()
    
    # Calismaya Devam Ediyorum 
    
    def test_basarili_deneyim_ekler(self):
        deneyimlerim= Deneyimlerim(self.driver)

        self.test_deneyimlerim_sayfasina_gider()
        time.sleep(3)
        deneyimlerim.kurum_adi_textbox_deger_girer()
        time.sleep(5)
        deneyimlerim.pozisyon_textbox_deger_girer()
        time.sleep(2)
        deneyimlerim.sektor_textbox_deger_girer()
        time.sleep(2)
        deneyimlerim.sehir_seciniz_dropdown_sehir_secimi_yapar()
        time.sleep(3)
        deneyimlerim.is_baslangic_tarihine_deger_girer()
        time.sleep(10)
        deneyimlerim.calismaya_devam_ediyorum_butonuna_tiklar()
        time.sleep(3)
        deneyimlerim.is_aciklamasi_texbox_deger_girer()
        time.sleep(3)
        deneyimlerim.kaydet_butonuna_tiklar()
        time.sleep(3)

        expected_mesaj="• Deneyim eklendi."
        self.soft_assert(self.assertEqual,expected_mesaj,deneyimlerim.basari_mesaji(),"MESAJ Hatali!!")
        self.assert_all()

    def test_eklenen_deneyim_dogrulanir(self):
        deneyimlerim= Deneyimlerim(self.driver)
        time.sleep(5)
    
        self.test_deneyimlerim_sayfasina_gider() 
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,500)","")
        time.sleep(3)
        self.soft_assert(self.assertEqual,deneyimlerim.eklenen_kurum_adini_dondurur(),DATA_KURUM_ADI, "kaydedilen kurum adi hatali!!!" )
        self.soft_assert(self.assertEqual,deneyimlerim.eklenen_pozisyon_dondurur(),DATA_POZISYON,"kaydedilen pozisyon adi hatali!!")
        self.soft_assert(self.assertEqual,deneyimlerim.eklenen_sektor__dondurur(),DATA_SEKTOR, "kaydedilen sektor adi hatali!!")
        self.soft_assert(self.assertEqual,deneyimlerim.eklenen_sehir_dondurur(),DATA_SEHIR,"Kaydedilen Sehir adi hatalii!!!")
        time.sleep(3)
        self.soft_assert(self.assertEqual,deneyimlerim.is_aciklamasi_dondurur(),DATA_IS_ACIKLAMASI, "Kaydedilen is aciklamasi hatali!!")
        self.soft_assert(self.assertEqual,deneyimlerim.eklenen_tarih_asarligini_dondurur(),EXPECTED_TARIH_ARALIGI, " Kaydedilen tarihler hatali!!")

        self.assert_all()
        
    def test_deneyim_siler(self):
        deneyimlerim= Deneyimlerim(self.driver)
        time.sleep(5)
    
        self.test_deneyimlerim_sayfasina_gider() 
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,500)","")
        time.sleep(3)
        deneyimlerim.deneyim_sil_butonuna_tiklar()
        time.sleep(3)
        deneyimlerim.deneyim_sil_evet_butonuna_basar()
        time.sleep(2)
        expected_message="• Deneyim kaldırıldı."
        self.soft_assert(self.assertEqual,deneyimlerim.deneyim_silindi_mesajini_dondurur(),expected_message," deneyim kaldırılamadı!!!")
        self.assert_all()


    @pytest.mark.skip
    def test_kurum_adi_girilmediginde_hata_mesaji_alir(self):
        
        page_base=PageBase(self.driver)       
        deneyimlerim= Deneyimlerim(self.driver) 
        giris=Giris(self.driver) 
        
        giris.ana_giris()     
        time.sleep(5)
        deneyimlerim.profil_bilgilerim_butonuna_tiklar()  
        time.sleep(3)
        deneyimlerim.deneyimlerim_butonuna_tiklar()
        deneyimlerim.kurum_adi_textbox_deger_girer()

    
        
        

  
    

        