from selenium import webdriver
import pytest
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.service import Service as ChromeService
from pages.constants.globalConstants import *


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()
    
 #service=ChromeService(ChromeDriverManager().install())   
    
