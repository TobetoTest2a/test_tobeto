from time import sleep
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.PageBase import PageBase
from pages.constants.password_constans import *


@pytest.mark.usefixtures("setup")
class Password(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def sifremi_unuttum_butonuna_tikla(self):
        sifre_unuttum_button = self.wait_element_visibility(SIFREMI_UNUTTUM_BUTTON_LOCATOR)
        sifre_unuttum_button.click()

    def mail_input_gönder(self, data):
        mail_input_area = self.wait_element_visibility(MAIL_INPUT_LOCATOR)
        self.wait_element_visibility(MAIL_INPUT_LOCATOR).send_keys(data)
        #mail_input_area.send_keys(data)

    def gönder_butonuna_tikla(self):
        gonder_button = self.wait_element_clickable(GONDER_BUTTON_LOCATOR)
        gonder_button.click()

    def toast_mesaji_bul_ve_içeriği_text_getir(self):
        toast_message_sifre_sifirlama = self.wait_element_presence(TOAST_MESSAGE_LOCATOR)
        return toast_message_sifre_sifirlama.text

    # def sifre_sifirlama(self):
    #     sifre_unuttum_button = self.wait_element_visibility(SIFREMI_UNUTTUM_BUTTON_LOCATOR)
    #     sifre_unuttum_button.click()
    #     mail_input_area = self.wait_element_visibility(MAIL_INPUT_LOCATOR)
    #     self.wait_element_visibility(MAIL_INPUT_LOCATOR).send_keys(GIRISMAIL)
    #     #mail_input_area.send_keys(GIRISMAIL)
    #     gonder_button = self.wait_element_visibility(GONDER_BUTTON_LOCATOR)
    #     gonder_button.click()
    #     toast_message_sifre_sifirlama = self.wait_element_presence(TOAST_MESSAGE_LOCATOR)
    #     return toast_message_sifre_sifirlama.text

    # def sifre_sifirlama_gecersiz_mail(self):
    #     sifre_unuttum_button = self.wait_element_visibility(SIFREMI_UNUTTUM_BUTTON_LOCATOR)
    #     sifre_unuttum_button.click()
    #     mail_input_area = self.wait_element_visibility(MAIL_INPUT_LOCATOR)
    #     self.wait_element_visibility(MAIL_INPUT_LOCATOR).send_keys("email")
    #     #mail_input_area.send_keys("email")
    #     gonder_button = self.wait_element_visibility(GONDER_BUTTON_LOCATOR)
    #     gonder_button.click()
    #     toast_message_sifre_sifirlama_gecersiz_mail = self.wait_element_presence(TOAST_MESSAGE_LOCATOR)
    #     return toast_message_sifre_sifirlama_gecersiz_mail.text
    
    # def sifre_sifirlama_gecersiz_kullanici(self):
    #     sifre_unuttum_button = self.wait_element_visibility(SIFREMI_UNUTTUM_BUTTON_LOCATOR)
    #     sifre_unuttum_button.click()
    #     mail_input_area = self.wait_element_visibility(MAIL_INPUT_LOCATOR)
    #     self.wait_element_visibility(MAIL_INPUT_LOCATOR).send_keys("tobeto1@gmail.com")
    #     #mail_input_area.send_keys("tobeto1@gmail.com")
    #     gonder_button = self.wait_element_clickable(GONDER_BUTTON_LOCATOR)
    #     gonder_button.click()
    #     toast_message_sifre_sifirlama_gecersiz_kullanici = self.wait_element_presence(TOAST_MESSAGE_LOCATOR)
    #     return toast_message_sifre_sifirlama_gecersiz_kullanici.text 
    

    