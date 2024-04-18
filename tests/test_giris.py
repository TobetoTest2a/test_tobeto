import pytest
from selenium import webdriver
from pages.giris import *
import softest

@pytest.mark.usefixtures("setup")
class TestTobetoGiris(softest.TestCase):
    
    def test_validUserName_validPassword_girisYap(self):
        giris_instance = Giris(self.driver) #baska sayfadan cagırılan fonksiyon
        self.soft_assert(self.assertEqual, BASARILI_POPUP_TEXT, giris_instance.gecerli_giris, "Hatali basarili mesaji.")
        #assert giris_instance.gecerli_giris() ==  BASARILI_POPUP_TEXT
        #self.assert_all()