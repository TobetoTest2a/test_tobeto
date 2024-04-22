from selenium.webdriver.common.by import By

EGITIM_HAYATIM = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[3]/span[2]")

EGITIM_DURUMU_BUTONU=(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/select")
LISANS_SEC= (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/select/option[2]")

UNIVERSITE = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input") #NAME
UNIVERSITE_ADI = "İTÜ"

BOLUM= (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input") #NAME
BOLUM_ADI= "KİMYA"
BOLUM_ADI_DEVAM ="TEST MÜHENDİSİ"

BASLAMA_YILI_BUTONU = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/div")
BASLAMA_YILI_SEC = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[7]") #XPATH

MEZUNIYET_YILI =  (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div/div/input") #XPATH
MEZUNIYET_YILI_SEC = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[8]") #XPATH

UNIVERSITEYE_DEVAM_EDIYORUM_BUTONU = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/label[2]/input")

BASARILI_POPUP_MESAJ = (By.XPATH,"//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")
BASARILI_POPUP_MESAJI_TEXT ="• Eğitim bilgisi eklendi."
                     
KAYDET_BUTONU=(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/button")

KAYDI_SIL=(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[2]/span")
KAYIT_SILMEYE_EMINMISIN_MESAJI = (By.XPATH,"//body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']/div[@class='modal-content']//p[@class='alert-message mx-3']")
KAYIT_SILMEYE_EMINMISIN_MESAJI_TEXT = "Seçilen eğitimi silmek istediğinize emin misiniz?"
EVET_BUTONU = (By.XPATH,"//body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']/div[@class='modal-content']//button[@class='btn btn-yes my-3']")
KAYIT_SILME_BASARILI = (By.XPATH,"//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")
KAYIT_SILME_BASARILI_TEXT = "• Eğitim kaldırıldı."

#UYARI MESAJI
UYARI_MESAJI= (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/span")
UYARI_MESAJI_TEXT = "Doldurulması zorunlu alan*"

PROFIL_BIGLILERI_BUTTON =(By.XPATH, "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")
KULLANICI_BUTTON = (By.XPATH, "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")
