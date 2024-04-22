import time
import pytest
from pages.egitim_hayatim import *
from pages.giris import *
from pages.PageBase import PageBase
import softest
from pages.yabanci_dillerim import Yabanci_dil_ekle

@pytest.mark.usefixtures("setup")
class TestEgitimHayatim(softest.TestCase,PageBase):

    def test_egitim_hayatim_bos_gecme(self): 
       
        giris=Giris(self.driver)  
        profile_tikla=Yabanci_dil_ekle(self.driver)
        egitimHayatim= EgitimHayatim(self.driver) 
        
        giris.ana_giris()
        profile_tikla.profilim_kismina_tikla()
        profile_tikla.profil_bilgileri_tikla()
        egitimHayatim.egitim_hayatim_butonuna_tiklar()
        egitimHayatim.kaydet_butonuna_tikla()
        egitimHayatim.doldurulmasi_zorunlu_alan_uyari_mesaji()
    
    def test_egitim_hayatim_ekle(self):

        giris=Giris(self.driver)  
        profile_tikla=Yabanci_dil_ekle(self.driver)
        egitimHayatim= EgitimHayatim(self.driver)
        egitimHayatim=Egitim_hayatim_ekle(self.driver)

        giris.ana_giris()
        profile_tikla.profilim_kismina_tikla()
        profile_tikla.profil_bilgileri_tikla()
        egitimHayatim.egitim_hayatim_butonuna_tiklar()
        egitimHayatim.egitim_durumuna_tikla()
        egitimHayatim.egitim_durumu_sec()
        egitimHayatim.universite_adi_yaz()
        egitimHayatim.bolum_adi_yaz()
        egitimHayatim.baslangic_yili_tikla()
        egitimHayatim.baslangic_yili_sec()
        egitimHayatim.mezuniyet_yili_tikla()
        egitimHayatim.mezuniyet_yili_sec()
        egitimHayatim.kaydet_butonuna_tikla()
        egitimHayatim.universite_kaydi_basarili_popup_mesaji()
    
    def test_universiteye_devam_ediyorum_butonuna_tikla(self):

        giris=Giris(self.driver)  
        profile_tikla=Yabanci_dil_ekle(self.driver)
        egitimHayatim= EgitimHayatim(self.driver)
        egitimHayatim=Egitim_hayatim_ekle(self.driver)
        egitimHayatim = Universiteye_devam_ediyor_butonu(self.driver)

        giris.ana_giris()
        profile_tikla.profilim_kismina_tikla()
        profile_tikla.profil_bilgileri_tikla()
        egitimHayatim.egitim_hayatim_butonuna_tiklar()
        egitimHayatim.egitim_durumuna_tikla()
        egitimHayatim.egitim_durumu_sec()
        egitimHayatim.universite_adi_yaz()
        egitimHayatim.bolum_adi_yaz()
        egitimHayatim.baslangic_yili_tikla()
        egitimHayatim.baslangic_yili_sec()
        egitimHayatim.universiteye_devam_ediyorum_butonuna_tikla()
        egitimHayatim.kaydet_butonuna_tikla()
        egitimHayatim.universite_kaydi_basarili_popup_mesaji()
    
    def test_kayit_edilen_universite_bilgilerini_silme(self):
        giris=Giris(self.driver)  
        profile_tikla=Yabanci_dil_ekle(self.driver)
        egitimHayatim= EgitimHayatim(self.driver)
        egitimHayatim=Egitim_hayatim_ekle(self.driver)
        egitimHayatim = Universiteye_devam_ediyor_butonu(self.driver)
        egitimHayatim = Kayit_Edilen_Universiteyi_Silme(self.driver)

        giris.ana_giris()
        profile_tikla.profilim_kismina_tikla()
        profile_tikla.profil_bilgileri_tikla()
        egitimHayatim.egitim_hayatim_butonuna_tiklar()
        egitimHayatim.sayfayi_asagi_kaydir()
        egitimHayatim.universite_kaydini_sil()
        egitimHayatim.egitimi_silmek_istediginize_eminmisiniz_popup_mesaji()
        egitimHayatim.evet_butonuna_tikla()
        egitimHayatim.kayit_silme_basarili_popup_mesaji()

