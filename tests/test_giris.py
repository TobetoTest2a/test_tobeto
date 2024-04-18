import pytest
from selenium import webdriver
from pages.giris import *
from pages.PageBase import PageBase
import softest
import unittest


@pytest.mark.usefixtures("setup")
class TestTobetoGiris(softest.TestCase, unittest.TestCase):

    
    def test_valid_login(self):
        giris_instance = Giris(self.driver) #baska sayfadan cagırılan fonksiyon
        assert giris_instance.gecerli_giris() ==  BASARILI_POPUP_TEXT

    def test_invalid_login(self):
        giris_instance = Giris(self.driver)
        assert giris_instance.gecersiz_giris() == GECERSIZ_POPUP_TEXT

    def test_empty_login(self):
        giris_instance = Giris(self.driver)
        #assert giris_instance.bos_giris() == BOS_ERROR_LINE_MAIL_TEXT, BOS_ERROR_LINE_PASSWORD_TEXT
        result = giris_instance.bos_giris() #Tuple olarak return ettiğimiz değerleri bir değişkene atadık
        expected = (BOS_ERROR_LINE_MAIL_TEXT, BOS_ERROR_LINE_PASSWORD_TEXT) #Return ettiğimiz değerler tuple olduğu için karşılaştırmak istediğimiz değerleri de tuple olarak yazıp bir değişkene atadık
        self.assertTupleEqual(result, expected) #Unittest bulunan assertTupleEqual ile tuple değerleri atadığımız değişkenleri assert ettik

    
        