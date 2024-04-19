import pytest
from selenium import webdriver
from pages.giris import *
from pages.PageBase import PageBase
import softest
import unittest


@pytest.mark.usefixtures("setup")
class TestTobetoGiris(softest.TestCase, unittest.TestCase):

    def test_valid_login(self):
        giris_instance = Giris(self.driver)
        giris_instance.username_bul_ve_gönder(GIRISMAIL)
        giris_instance.password_bul_ve_gönder(GIRISSIFRE)
        giris_instance.giris_yap_butonuna_tikla()
        actual_value = giris_instance.toast_mesaji_bul_text_döndür()
        self.soft_assert(self.assertEqual, BASARILI_POPUP_TEXT , actual_value, "HATA!!!")
        self.assert_all

    def test_invalid_login(self):
        giris_instance = Giris(self.driver)
        giris_instance.username_bul_ve_gönder(GECERSIZMAIL)
        giris_instance.password_bul_ve_gönder(GECERSIZSIFRE)
        giris_instance.giris_yap_butonuna_tikla()
        actual_value = giris_instance.toast_mesaji_bul_text_döndür()
        self.soft_assert(self.assertEqual, GECERSIZ_POPUP_TEXT , actual_value, "HATA!!!")
        self.assert_all

    def test_empty_login(self):
        giris_instance = Giris(self.driver)
        giris_instance.username_bul_ve_gönder("")
        giris_instance.password_bul_ve_gönder("")
        giris_instance.giris_yap_butonuna_tikla()
        result = giris_instance.hata_satirlarini_bul_ve_döndür() #Tuple olarak return ettiğimiz değerleri bir değişkene atadık
        expected = (BOS_ERROR_LINE_MAIL_TEXT, BOS_ERROR_LINE_PASSWORD_TEXT) #Return ettiğimiz değerler tuple olduğu için karşılaştırmak istediğimiz değerleri de tuple olarak yazıp bir değişkene atadık
        self.assertTupleEqual(result, expected) #Unittest bulunan assertTupleEqual ile tuple değerleri atadığımız değişkenleri assert ettik
        

    # def test_valid_login(self):
    #     giris_instance = Giris(self.driver) 
    #     #assert giris_instance.gecerli_giris() ==  BASARILI_POPUP_TEXT
    #     self.soft_assert(self.assertEqual, BASARILI_POPUP_TEXT , giris_instance.gecerli_giris(), "HATA!!!")
    #     self.assert_all

    # def test_invalid_login(self):
    #     giris_instance = Giris(self.driver)
    #     #assert giris_instance.gecersiz_giris() == GECERSIZ_POPUP_TEXT
    #     self.soft_assert(self.assertEqual,  GECERSIZ_POPUP_TEXT , giris_instance.gecersiz_giris(), "HATA!!!")
    #     self.assert_all

    # def test_empty_login(self):
    #     giris_instance = Giris(self.driver)
    #     #assert giris_instance.bos_giris() == BOS_ERROR_LINE_MAIL_TEXT, BOS_ERROR_LINE_PASSWORD_TEXT
    #     result = giris_instance.bos_giris() #Tuple olarak return ettiğimiz değerleri bir değişkene atadık
    #     expected = (BOS_ERROR_LINE_MAIL_TEXT, BOS_ERROR_LINE_PASSWORD_TEXT) #Return ettiğimiz değerler tuple olduğu için karşılaştırmak istediğimiz değerleri de tuple olarak yazıp bir değişkene atadık
    #     self.assertTupleEqual(result, expected) #Unittest bulunan assertTupleEqual ile tuple değerleri atadığımız değişkenleri assert ettik

    
        