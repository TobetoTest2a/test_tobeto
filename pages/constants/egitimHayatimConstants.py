KAYDET_BUTONU = ".btn-primary" #CSS
HATA_MESAJİ_EGİTİM_DURUMU = "div:nth-of-type(1) > .text-danger" #CSS
HATA_MESAJİ_UNİVERSİTE = "div:nth-of-type(2) > .text-danger" #CSS
HATA_MESAJİ_BOLUM = "div:nth-of-type(3) > .text-danger" #CSS
HATA_MESAJİ_BASLANGİC_YİLİ =  "div:nth-of-type(4) > .text-danger" #CSS
HATA_MESAJİ_MEZUNİYET_YİLİ = "div:nth-of-type(5) > span:nth-of-type(1)" #CSS
HATA_MESAJİ_DEVAM_EDİYORUM = "div:nth-of-type(5) > span:nth-of-type(2)" #CSS
EGİTİM_DURUMU = "EducationStatus" #NAME
UNİVERSİTE = "University" #NAME
BOLUM= "Department" #NAME
BASLAMA_YİLİ = ".form-control.react-datepicker-ignore-onclickoutside.tobeto-input" #CSS
BASLAMA_YİLİ_TAKVİMİ =  ".react-datepicker-year-header.react-datepicker__header" #CSS
MEZUNİYET_YİLİ =  "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div/div/input" #XPATH
MEZUNİYET_YİLİ_TAKVİMİ = ".react-datepicker-year-header.react-datepicker__header"
EGİTİMİ_EKLEME = "my-grade" #CLASS
EGİTİMİ_SİL = ".my-grade:nth-child(1) .grade-delete" #CLASS
POPUP_UYARİ = " bg-white shadow-lg" #CLASS
EVET_BUTONU = "btn btn-yes my-3" #CLASS

from selenium.webdriver.common.by import By

# EGITIM_HAYATIM= (By.CSS_SELECTOR,".btn:nth-child(3)") #CSS SELECTOR
EGITIM_HAYATIM = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[3]/span[2]")
# KULLANICI_BUTTON = (By.CLASS_NAME,"btn p-0 fw-normal b-r-35 text-end d-flex align-items-center show") #CLASS
# PROFIL_BILGILERI=  (By.CSS_SELECTOR,"li:nth-of-type(1) > .dropdown-item.profil-dropdown") #CSS
PROFIL_BIGLILERI_BUTTON =(By.XPATH, "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")
KULLANICI_BUTTON = (By.XPATH, "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")
