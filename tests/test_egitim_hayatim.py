import time
import pytest
from pages.egitim_hayatim import *
from pages.giris import *
from pages.PageBase import PageBase
import softest

from pages.yabanci_dillerim import Yabanci_dil_ekle

@pytest.mark.usefixtures("setup")
class TestEgitimHayatim(softest.TestCase,PageBase):

    def test_egitim_hayatim(self): 
       

        giris=Giris(self.driver)  
        profile_tikla=Yabanci_dil_ekle(self.driver)
        egitimHayatim= EgitimHayatim(self.driver) 
        giris.ana_giris()
        profile_tikla.profilim_kismina_tikla()
        profile_tikla.profil_bilgileri_tikla()
        egitimHayatim.egitim_hayatim_butonuna_tiklar()
       
        
    



    

        