from selenium.webdriver.common.by import By

#Password Locators
SIFREMI_UNUTTUM_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".d-block")
MAIL_INPUT_LOCATOR = (By.CLASS_NAME, "form-control.mt-6")
GONDER_BUTTON_LOCATOR = (By.CLASS_NAME, "btn.btn-primary.w-100.mt-6")
TOAST_MESSAGE_LOCATOR = (By.CLASS_NAME, "toast-body")

GIRISMAIL = "tobeto.0001@gmail.com"
SIFRE_POPUP_TEXT = "• Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin."
SIFRE_GECERSIZ_MAIL_POPUP_TEXT = "• Girdiğiniz e-posta geçersizdir."
SIFRE_GECERSIZ_KULLANICI_POPUP_TEXT = "• Kullanıcı bulunamadı."
SCREENSHOT_FOLDER = r'C:\Users\oguzh\OneDrive\Masaüstü\test_tobeto\tests\test_sifre_sifirlama_gecersiz_kullanici_failure.png'


