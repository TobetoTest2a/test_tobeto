from selenium.webdriver.common.by import By
#Yabancı Dillerim
PROFILIMBUTTON = "btn.p-0.fw-normal.b-r-35.text-end.d-flex.align-items-center"
PROFILBILGILERIMBUTTON = "#__next > div > nav > div.container-fluid > div > div > div.btn-group.header-avatar > ul > li:nth-child(1) > a"
YABANCIDILLERIM_BUTTON = "languages2"
YABANCIDIL_ACILIRMENU = "languageName"
ALMANCASEC = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/select/option[2]"
SEVIYESEC_ACILIRMENU = "proficiency"
SEVIYESEC = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/select/option[2]"
KAYDET_BUTTON = "btn.btn-primary.py-2.mb-3.d-inline-block.mobil-btn"

SAVE_POPUP_MESSAGE = "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']"

#olumlu mesaj
POPUP_MESSAGE_TEXT = "• Yabancı dil bilgisi eklendi."

#doldurulması zorunlu alan uyarı mesajı
BLANK_MESSAGE = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/p")
BLANK_MESSAGE_TEXT = "Doldurulması zorunlu alan*"
