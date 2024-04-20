import pytest
from selenium import webdriver
from pages.PageBase import PageBase
from pages.constants.kayitOlConstance import *
from pages.giris import *
from pages.kayit_ol import *
import softest


@pytest.mark.usefixtures("setup")
class TestKayitOl(softest.TestCase,PageBase):

    def test_basarili_kayit_ol(self):
        kayitOl = KayitOlFonksiyonu(self.driver)
        kayitOl.kayitOl_biliglerini_doldurur()
        kayitOl.sozlesmeler_sayfasini_doldurur()
        kayitOl.kaydetme_basarili()
        self.soft_assert(self.assertEqual, GORUNECEKTEXT , kayitOl.kaydetme_basarili(), "MESAJ GORUNTULENEMEDİ.")
        #self.assert_all()
        
    def test_bilgiler_bos_gecildiginde_uyari_meajlari_goruntulenmesi_fail(self):
        kayitOl = KayitOlFonksiyonu(self.driver)
        kayitOl.bos_kayit()  
        beklenen_zorunlu_alan_sayisi = int(5)
        self.soft_assert(self.assertEqual, beklenen_zorunlu_alan_sayisi, kayitOl.zorunlu_alan_karsilastirma(), "BEKLENILEN KADAR UYARI MESAJI ALINAMADI.")
        self.assert_all()
        #assert beklenen_zorunlu_alan_sayisi == kayitOl.zorunlu_alan_karsilastirma()
        
    def test_gecersiz_eposta_mesaji_goruntulenmesi(self):
       kayit_ol_object = KayitOlFonksiyonu(self.driver)
       kayit_ol_object.kayit_ol_biliglerini_epostasiz_doldurur()
       time.sleep(5)
       self.soft_assert(self.assertEqual, kayit_ol_object.bos_eposta_uyari_mesaji_kontrolu() , BOSEPOSTA_TEXT, "BEKLENILEN UYARI MESAJI ALINAMADI.")
       
       #assert KayitOlFonksiyonu.bos_eposta_uyari_mesaji_kontrolu() == BOSEPOSTA

    def test_sifre_eslesmedi_popup_goruntulenmesi_fail(self):  
        kayit_ol_object = KayitOlFonksiyonu(self.driver)
        kayit_ol_object.sifre_tekrari_yalnis_doldurulur()
        self.soft_assert(self.assertEqual, kayit_ol_object.sifre_eslesmedi_popup_kontrolu() , YALNIS_SIFRE_POPUP_XPATH_TEXT, "BEKLENILEN POPUP GORUNTULENMEDI.")
        #self.assert_all()
    

ttes = TestKayitOl()  
ttes.test_sifre_eslesmedi_popup_goruntulenmesi_fail() 