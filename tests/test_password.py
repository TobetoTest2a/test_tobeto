import pytest
from selenium import webdriver
from pages.password import *
import softest


@pytest.mark.usefixtures("setup")
class TestTobetoPassword(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.password_sayfasi = Password(self.driver)

    def test_sifre_sifirlama_basarili(self):
        self.password_sayfasi.sifremi_unuttum_butonuna_tikla()
        self.password_sayfasi.mail_input_gönder(GIRISMAIL)
        self.password_sayfasi.gönder_butonuna_tikla()
        actual_value = self.password_sayfasi.toast_mesaji_bul_ve_içeriği_text_getir()
        self.soft_assert(self.assertEqual,  SIFRE_POPUP_TEXT , actual_value , "HATA!!!")
        self.assert_all

    def test_sifre_sifirlama_gecersiz_mail(self):
        self.password_sayfasi.sifremi_unuttum_butonuna_tikla()
        self.password_sayfasi.mail_input_gönder("email")
        self.password_sayfasi.gönder_butonuna_tikla()
        actual_value = self.password_sayfasi.toast_mesaji_bul_ve_içeriği_text_getir()
        self.soft_assert(self.assertEqual, SIFRE_GECERSIZ_MAIL_POPUP_TEXT , actual_value , "HATA!!!")
        self.assert_all

    def test_sifre_sifirlama_gecersiz_kullanici(self):
        self.password_sayfasi.sifremi_unuttum_butonuna_tikla()
        self.password_sayfasi.mail_input_gönder("tobeto1@gmail.com")
        self.password_sayfasi.gönder_butonuna_tikla()
        actual_value = self.password_sayfasi.toast_mesaji_bul_ve_içeriği_text_getir()
        self.password_sayfasi.if_assert_fail_screenshot(actual_value, SIFRE_GECERSIZ_KULLANICI_POPUP_TEXT, SCREENSHOT_FOLDER)

    # def test_sifre_sifirlama_basarili(self):
    #  
    #     #assert self.password_sayfasi.sifre_sifirlama() == SIFRE_POPUP_TEXT
    #     self.soft_assert(self.assertEqual,  SIFRE_POPUP_TEXT , self.password_sayfasi.sifre_sifirlama(), "HATA!!!")
    #     self.assert_all

    
    # def test_sifre_sifirlama_gecersiz_mail(self):
    #  
    #     #assert self.password_sayfasi.sifre_sifirlama_gecersiz_mail() == SIFRE_GECERSIZ_MAIL_POPUP_TEXT
    #     self.soft_assert(self.assertEqual,  SIFRE_GECERSIZ_MAIL_POPUP_TEXT , self.password_sayfasi.sifre_sifirlama_gecersiz_mail(), "HATA!!!")
    #     self.assert_all

    # #@pytest.mark.xfail
    # def test_sifre_sifirlama_gecersiz_kullanici(self):
    #  
    #     actual_value = self.password_sayfasi.sifre_sifirlama_gecersiz_kullanici() 
    #     # try:
    #     #     # self.soft_assert(self.assertEqual,  SIFRE_GECERSIZ_KULLANICI_POPUP_TEXT , actual_value, "HATA!!!")
    #     #     # self.assert_all
    #     #     assert actual_value == SIFRE_GECERSIZ_KULLANICI_POPUP_TEXT
    #     # except AssertionError:
    #     # # Take a screenshot when the assertion fails
    #     #     screenshot_path = SCREENSHOT_FOLDER
    #     #     self.driver.save_screenshot(screenshot_path)
    #     #     #pytest.fail("Assertion failed: {} != {}".format( actual_value  , SIFRE_GECERSIZ_KULLANICI_POPUP_TEXT))
    #     self.password_sayfasi.if_fail_screenshot(actual_value, SIFRE_GECERSIZ_KULLANICI_POPUP_TEXT, SCREENSHOT_FOLDER)