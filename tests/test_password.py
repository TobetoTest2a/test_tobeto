import pytest
from selenium import webdriver
from pages.password import *
import softest


@pytest.mark.usefixtures("setup")
class TestTobetoPassword(softest.TestCase):

    def test_sifre_sifirlama_basarili(self):
        password_instance = Password(self.driver)
        password_instance.sifremi_unuttum_butonuna_tikla()
        password_instance.mail_input_gönder(GIRISMAIL)
        password_instance.gönder_butonuna_tikla()
        actual_value = password_instance.toast_mesaji_bul_ve_içeriği_text_getir()
        self.soft_assert(self.assertEqual,  SIFRE_POPUP_TEXT , actual_value , "HATA!!!")
        self.assert_all

    def test_sifre_sifirlama_gecersiz_mail(self):
        password_instance = Password(self.driver)
        password_instance.sifremi_unuttum_butonuna_tikla()
        password_instance.mail_input_gönder("email")
        password_instance.gönder_butonuna_tikla()
        actual_value = password_instance.toast_mesaji_bul_ve_içeriği_text_getir()
        self.soft_assert(self.assertEqual, SIFRE_GECERSIZ_MAIL_POPUP_TEXT , actual_value , "HATA!!!")
        self.assert_all

    def test_sifre_sifirlama_gecersiz_kullanici(self):
        password_instance = Password(self.driver)
        password_instance.sifremi_unuttum_butonuna_tikla()
        password_instance.mail_input_gönder("tobeto1@gmail.com")
        password_instance.gönder_butonuna_tikla()
        actual_value = password_instance.toast_mesaji_bul_ve_içeriği_text_getir()
        try:
            assert actual_value == SIFRE_GECERSIZ_KULLANICI_POPUP_TEXT
        except AssertionError:
            password_instance.if_fail_screenshot(actual_value, SIFRE_GECERSIZ_KULLANICI_POPUP_TEXT, SCREENSHOT_FOLDER)

    # def test_sifre_sifirlama_basarili(self):
    #     password_instance = Password(self.driver)
    #     #assert password_instance.sifre_sifirlama() == SIFRE_POPUP_TEXT
    #     self.soft_assert(self.assertEqual,  SIFRE_POPUP_TEXT , password_instance.sifre_sifirlama(), "HATA!!!")
    #     self.assert_all

    
    # def test_sifre_sifirlama_gecersiz_mail(self):
    #     password_instance = Password(self.driver)
    #     #assert password_instance.sifre_sifirlama_gecersiz_mail() == SIFRE_GECERSIZ_MAIL_POPUP_TEXT
    #     self.soft_assert(self.assertEqual,  SIFRE_GECERSIZ_MAIL_POPUP_TEXT , password_instance.sifre_sifirlama_gecersiz_mail(), "HATA!!!")
    #     self.assert_all

    # #@pytest.mark.xfail
    # def test_sifre_sifirlama_gecersiz_kullanici(self):
    #     password_instance = Password(self.driver)
    #     actual_value = password_instance.sifre_sifirlama_gecersiz_kullanici() 
    #     # try:
    #     #     # self.soft_assert(self.assertEqual,  SIFRE_GECERSIZ_KULLANICI_POPUP_TEXT , actual_value, "HATA!!!")
    #     #     # self.assert_all
    #     #     assert actual_value == SIFRE_GECERSIZ_KULLANICI_POPUP_TEXT
    #     # except AssertionError:
    #     # # Take a screenshot when the assertion fails
    #     #     screenshot_path = SCREENSHOT_FOLDER
    #     #     self.driver.save_screenshot(screenshot_path)
    #     #     #pytest.fail("Assertion failed: {} != {}".format( actual_value  , SIFRE_GECERSIZ_KULLANICI_POPUP_TEXT))
    #     password_instance.if_fail_screenshot(actual_value, SIFRE_GECERSIZ_KULLANICI_POPUP_TEXT, SCREENSHOT_FOLDER)