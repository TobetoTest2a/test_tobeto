import pytest
from selenium import webdriver
from pages.giris import *
from pages.PageBase import PageBase
import softest

@pytest.mark.usefixtures("setup")
class TestTobetoGiris(softest.TestCase,PageBase):
    
    
    def test_validUserName_validPassword_girisYap(self):
        giris_instance = Giris(self.driver) #baska sayfadan cagırılan fonksiyon
        assert giris_instance.gecerli_giris() ==  BASARILI_POPUP_TEXT
        