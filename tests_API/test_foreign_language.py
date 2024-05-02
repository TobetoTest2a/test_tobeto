import requests
import json
from API_constants import *
import softest

class TestForeignLanguage(softest.TestCase):
    def test_control_added_language(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token_language}'
        }

        response = requests.get(url_language, headers = headers)

        if response.status_code == 200:
            print(" !! Basarili !! ")
            response_data = response.json()


            print("Authentication API sorgusunda geçerli bilgi isteği sonucunda 200 durum kodu görüldü.", response_data)

        elif response.status_code == 401:
            print( "!! UnauthorizedError !!")
            print("Lütfen token güncelleyiniz!!", response.status_code)
        
        elif response.status_code == 404:
            print("!! NotFoundError !! ")
            print("Lütfen url kontrol ediniz!!")

        else:
            print("Lütfen girdiginiz degerleri kontrol edin!", response.status_code)

    def test_control_delete_language(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token_language}'
        }

        response = requests.delete(url_delete_language, headers = headers)

        if response.status_code == 204:  # Başarılı bir şekilde silindiğini gösteren durum kodu
            print("Body başarıyla silindi.")
        else:
            print("Body silinirken bir hata oluştu:", response.text)

# TestForeignLanguage.control_added_language()

