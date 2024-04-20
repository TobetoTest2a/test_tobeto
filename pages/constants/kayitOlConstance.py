from selenium.webdriver.common.by import By
import random

KAYITOLBUTTON = (By.CLASS_NAME, "text-decoration-none text-muted fw-bold")

GIRIS_URL = "https://tobeto.com/giris"
KAYITOL_URL = "https://tobeto.com/kayit-ol"

#kayit ol sayfasi
AD = (By.NAME, "firstName")
SOYAD = (By.NAME,"lastName")
EPOSTA = (By.NAME, "email")
SIFRE = (By.NAME,"password")
SIFRETEKRAR = (By.NAME, "passwordAgain") 
KAYITOL = (By.CLASS_NAME, "btn.btn-primary.w-100.mt-6")

ILKKAYITOL = (By.CLASS_NAME, "text-decoration-none.text-muted.fw-bold") 

#sozlesmeler sayfasi
ACIKRIZAMETNİ = (By.NAME,"contact")
UYELİKSOZLESMESİ = (By.NAME,"membershipContrat")
EPOSTAIZNI = (By.NAME,"emailConfirmation")
ARAMAIZNI = (By.NAME,"phoneConfirmation")
TELNO = (By.ID, "phoneNumber")
telno = random.randint(1000000000, 9999999999)
ROBOTDEGILIM = (By.ID, "recaptcha-anchor") 
DEVAMETBUTTON = (By.CLASS_NAME ,"btn.btn-yes.my-3")

#valid giris
kullanici_ad = "Tobeto"
kullanici_soyad = "Kodluyor"
randonint = str(random.randint(1000, 9999))
kullanici_eposta= ("tobeto"+ randonint +"@gmail.com")   #SUNUMDA ANLATILACAK
valid_password = "123456"
BASARILIGIRIS_URL = "https://tobeto.com/e-posta-dogrulama?registerType=registerForm"
TIKISARET = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/div/svg/path[1]")
KAYITTEXTI = (By.CLASS_NAME, "success-payment-text")
GORULECEKTEXT_LOCATE = (By.CLASS_NAME, "success-payment-text")
GORUNECEKTEXT = "Tobeto Platform'a kaydınız başarıyla gerçekleşti."

#uyarı metni: doldurulması zorunlu alan
ZORUNLU1 = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/div/form/p[1]")
ZORUNLU2 = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/div/form/p[2]")

#bos eposta uyarısı
EPOSTABOS_UYARIMESAJI = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/div/form/p")
BOSEPOSTA_TEXT = "Geçersiz e-posta adresi*"
#yalnis sifre tekrari
YALNIS_SIFRE_POPUP_XPATH = (By.XPATH, "//body/div[@role='dialog']")
YALNIS_SIFRE_POPUP_XPATH_TEXT = "• Şifreler Eşleşmedi"


