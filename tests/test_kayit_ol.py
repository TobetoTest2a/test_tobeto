import pytest
from selenium import webdriver
from pages.PageBase import PageBase
from pages.constants.kayitOlConstance import *
from pages.giris import *
from pages.kayit_ol import *
import softest
import allure

@pytest.mark.usefixtures("setup")
class TestKayitOl(softest.TestCase,PageBase):

    def test_basarili_kayit_ol(self):
        kayit_ol_object = KayitOlFonksiyonu(self.driver)
        kayit_ol_object.kayitOl_biliglerini_doldurur()
        kayit_ol_object.sozlesmeler_sayfasini_doldurur()
        kayit_ol_object.kaydetme_basarili()
        self.soft_assert(self.assertEqual, GORUNECEKTEXT , kayit_ol_object.kaydetme_basarili(), "MESAJ GORUNTULENEMEDİ.")
        self.assert_all()
        
    def test_bilgiler_bos_gecildiginde_uyari_meajlari_goruntulenmesi_FAIL(self): # != SEKLİNDE YAZILDI
        kayit_ol_object = KayitOlFonksiyonu(self.driver)
        kayit_ol_object.bos_kayit()  
        beklenen_zorunlu_alan_sayisi = int(5)
        self.soft_assert(self.assertTrue, beklenen_zorunlu_alan_sayisi == kayit_ol_object.zorunlu_alan_karsilastirma(), "BEKLENILEN POPUP GORUNTULENMEDI.")
        self.assert_all()
        
    def test_gecersiz_eposta_mesaji_goruntulenmesi(self):
       kayit_ol_object = KayitOlFonksiyonu(self.driver)
       kayit_ol_object.kayit_ol_biliglerini_epostasiz_doldurur()
       kayit_ol_object = KayitOlFonksiyonu(self.driver)
       time.sleep(5)
       self.soft_assert(self.assertEqual, kayit_ol_object.bos_eposta_uyari_mesaji_kontrolu() , BOSEPOSTA_TEXT, "BEKLENILEN UYARI MESAJI ALINAMADI.")
       self.assert_all()

    def test_sifre_eslesmedi_popup_goruntulenmesi_FAIL(self):  
        kayit_ol_object = KayitOlFonksiyonu(self.driver)
        kayit_ol_object.sifre_tekrari_yalnis_doldurulur()
        self.soft_assert(self.assertEqual, kayit_ol_object.sifre_eslesmedi_popup_kontrolu(), YALNIS_SIFRE_POPUP_XPATH_TEXT, f"BEKLENILEN POPUP GORUNTULENMEDI. Beklenen: {YALNIS_SIFRE_POPUP_XPATH_TEXT}")
        self.assert_all()
        
    def test_mevcut_eposta_popup_goruntulenmesi_FAIL(self):
         kayit_ol_object = KayitOlFonksiyonu(self.driver)
         kayit_ol_object.mevcut_eposta_ile_kayit()
         kayit_ol_object.mevcut_eposta_popup_kontrolu()
         self.soft_assert(self.assertEqual, kayit_ol_object.mevcut_eposta_popup_kontrolu(), MEVCUTSIFRE_TEXT, f"BEKLENILEN POPUP GORUNTULENMEDI. Beklenen: {MEVCUTSIFRE_TEXT}")
         self.assert_all()
         
    def test_uzun_telefonNum_karakter_sayisi_uyarisi_kontrolu(self):
        kayit_ol_object = KayitOlFonksiyonu(self.driver)
        kayit_ol_object.kayitOl_biliglerini_doldurur()
        button_enable_mi = kayit_ol_object.is_koyitOl_button_enabled()
        #kayit ol butonunun renginin degistiginin testi
        self.soft_assert(self.assertTrue , button_enable_mi, "Button disable olmadi.")
        self.assert_all()
        kayit_ol_object.uzun_telNo_ile_sozlesmeler_sayfasini_doldurulur()
        self.soft_assert(self.assertEqual, kayit_ol_object.uzun_telNo_uyarisi_kontrolu(), UZUN_TELNO_UYARISI_TEXT, f"BEKLENILEN POPUP GORUNTULENMEDI. Beklenen: {UZUN_TELNO_UYARISI_TEXT}")
        self.assert_all()
        
    def test_az_telefonNum_karakter_sayisi_uyarisi_kontrolu(self):
        kayit_ol_object = KayitOlFonksiyonu(self.driver)
        kayit_ol_object.kayitOl_biliglerini_doldurur()
        kayit_ol_object.kisa_telNo_ile_sozlesmeler_sayfasini_doldurulur()
        self.soft_assert(self.assertEqual, kayit_ol_object.kisa_telNo_uyarisi_kontrolu(), KISA_TELNO_TEXT, f"BEKLENILEN POPUP GORUNTULENMEDI. Beklenen: {KISA_TELNO_TEXT}")
        self.assert_all()
        
    def test_kayitli_telNo_uyari_mesaji_kontrolu_FAIL(self):
        kayit_ol_object = KayitOlFonksiyonu(self.driver)
        kayit_ol_object.kayitOl_biliglerini_doldurur()
        kayit_ol_object.mevcut_telNo_ile_sozlesmeler_sayfasi_doldurulur()
        self.soft_assert(self.assertEqual, kayit_ol_object.mevcut_telNo_uyarisi_kontrolu(), MEVCUT_TELNO_UYARISI_TEXT, f"BEKLENILEN POPUP GORUNTULENMEDI. Beklenen: {MEVCUT_TELNO_UYARISI_TEXT}")
        self.assert_all()
         
        
        



