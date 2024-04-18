import pytest
from selenium import webdriver
from pages.password import *
import softest


@pytest.mark.usefixtures("setup")
class TestTobetoPassword(softest.TestCase):

    def test_sifre_sifirlama_basarili(self):
        password_instance = Password(self.driver)
        assert password_instance.sifre_sifirlama() == SIFRE_POPUP_TEXT


    def test_sifre_sifirlama_gecersız_mail(self):
        password_instance = Password(self.driver)
        assert password_instance.sifre_sifirlama_gecersiz_mail() == SIFRE_GECERSIZ_MAIL_POPUP_TEXT

    #@pytest.mark.xfail
    def test_sifre_sifirlama_gecersiz_kullanici(self):
        password_instance = Password(self.driver)
        try:
            assert password_instance.sifre_sifirlama_gecersiz_kullanici() == SIFRE_GECERSIZ_KULLANICI_POPUP_TEXT
        except AssertionError:
        # Take a screenshot when the assertion fails
            screenshot_path = SCREENSHOT_FOLDER
            self.driver.save_screenshot(screenshot_path)


