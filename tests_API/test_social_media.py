import requests
import json
from API_constants import *
import softest

class TestSocialMedia(softest.TestCase):
    def test_control_added_media(self):

        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token_socialMedia}'
        }

        response = requests.get(url_socialMedia, headers = headers)

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
    
    def test_add_media(self):
      headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token_socialMedia}'
        }  
      
      new_media_data = {"data": {"SocialMediaName": "Github", "SocialMediaUrl": "https://www.github.com/"}}
         
      data_str = json.dumps(new_media_data)

      response = requests.post(url_socialMedia, data = data_str,  headers = headers)

      if response.status_code == 200:
        print("Authentication API sorgusunda geçerli bilgi isteği sonucunda 200 durum kodu görüldü.")
    
      else:
        print("Yeni veri oluşturulurken bir hata oluştu:", response.text)

    
    def test_existing_media(self):
       headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token_socialMedia}'
        }  
      
       new_media_data = {"data": {"SocialMediaName": "Linkedin", "SocialMediaUrl": "https://www.linkedin.com/"}}
         
       data_str = json.dumps(new_media_data)

       response = requests.post(url_socialMedia, data = data_str,  headers = headers)

       if response.status_code == 200:
        print("Var olan bir veri eklemeye çalışma sonucunda 200 durum kodu görüldü.", response.text)
    
       else:
        print("Beklenmeyen bir hata oluştu:", response.text)
       
        


# TestSocialMedia.control_added_media()
# print("----------------------------------")
# TestSocialMedia.add_media()
# print("----------------------------------")
# TestSocialMedia.existing_media()
# print("----------------------------------")

