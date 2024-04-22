from selenium.webdriver.common.by import By

PROFILI_OLUSTUR_BUTTON_LOCATED = (By.CLASS_NAME, "btn.btn-primary.w-100")
ANASAYFA_BUTONU_LOCATED = (By.CLASS_NAME, "nav-link.c-gray-3")
KULLANICI_ADI_BUTONU_LOCATED = (By.XPATH, "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")
PROFIL_BILGILERI_LOCATED = (By.XPATH, "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")
SOL_MENU_LOCATED = (By.CLASS_NAME, "sidebar-text")
ULKE_TEXT_LOCATED = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[8]/label")
SCREENSHOT_FOLDER = r'C:\Users\mehme\Desktop\test_tobeto\screenshots\kisisel_bilgilerim\ulke_bayragi_degisimi.png'
BAYRAK_BUTON_LOCATED = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/div/div")
BAYRAK_SEC_LOCATED = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/div/div/select/option[216]")
TELEFON_NO_LOCATED = (By.XPATH, "//*[@id='phoneNumber']")
TELEFON_NO_DATA = "+90"
TURKIYE_BAYRAGI_LOCATED = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/div/div/select/option[225]")
EXPECTED_TITLE = "Kişisel Bilgilerim"
TC_KIMLIK_LOCATED = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/input")
GECERSIZ_TC_KIMLIK_DATA = "+"


KSB_AD_LOCATE = (By.NAME, "name")
KSB_SOYAD_LOCATE = (By.NAME, "surname")
KSB_MAIL_LOCATE = (By.NAME, "email")
KSB_TEL_NO_LOCATE = (By.ID, "phoneNumber")

KAYITLI_AD = "Tobeto"
KAYITLI_SOYAD = "Tobeto"
KAYITLI_MAIL = "tobeto.0001@gmail.com"
KAYITLI_TEL_NO = "+90 505 000 00 00"

IL_MENU_LOCATE = (By.NAME, "city")
ILCE_MENU_LOCATE = (By.NAME, "district")
IL_ISTANBUL_PATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[9]/select/option[41]")
ILCE_BEYLIKDUZU_PATH = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[10]/select/option[13]")

PP_DUZENLEME_BUTON_LOCATE = (By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/div[1]/div[1]")
DOSYA_YUKLEME_ILK_LOCATE = (By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[1]")
DOSYA_YUKLEME_ILK_TEXT = ("Sürükleyip bırak, yapıştır veya\ngözat")
GOZAT_LOCATE = (By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[1]/button")
GOZAT_TEXT = ("gözat")
GOZAT_BUTON_LOCATE = (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[1]/button")
DOSYA1_PATH = r'C:\Users\mehme\Desktop\test_tobeto\uploads\resim1.png'
DOSYA_SUBMIT_LOCATE = (By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[4]/div[1]/div[2]/button")