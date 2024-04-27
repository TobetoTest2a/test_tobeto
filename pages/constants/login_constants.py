from selenium.webdriver.common.by import By


#Giris yap sayfası locator
GIRISYAPBUTTON_LOCATOR = (By.CLASS_NAME, "btn.btn-primary.w-100.mt-6")
USERNAME_LOCATOR =  (By.NAME, "email")
PASSWORD_LOCATOR = (By.NAME, "password")
TOASTMESSAGE_LOCATOR = (By.CSS_SELECTOR, ".toast-body")
BOS_ERROR_LINE_MAIL = (By.XPATH, "//p[text()=\'Doldurulması zorunlu alan*\'][1]")
BOS_ERROR_LINE_PASSWORD = (By.XPATH, "//p[text()=\'Doldurulması zorunlu alan*\'][2]")
#Giris sayfası 
GIRISMAIL = "tobeto.0001@gmail.com"
GIRISSIFRE = "123456"
GECERSIZMAIL = "abc@gmail.com"
GECERSIZSIFRE = "123"
BASARILI_POPUP_TEXT = "• Giriş başarılı."
GECERSIZ_POPUP_TEXT = "• Geçersiz e-posta veya şifre."
BOS_ERROR_LINE_MAIL_TEXT = "Doldurulması zorunlu alan*"
BOS_ERROR_LINE_PASSWORD_TEXT = "Doldurulması zorunlu alan*"
EXCEL_FOLDER = r"testdata\giris.xlsx"


