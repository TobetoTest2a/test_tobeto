import requests
import json

class TestAPIDeneyimlerim():
    
    def test_GET_kayitli_deneyimleri_getir():

        url="https://api.tobeto.com/api/experience/my"
        token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjkwNzcsImlhdCI6MTcxNDQ2MzQwNSwiZXhwIjoxNzE0NjM2MjA1fQ.2Dywvgm65jcJSiRPSc_EbmGKEzEaDwQsGOZjwV-Qrik"
       
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
        }

        response = requests.get(url, headers=headers)
        #print(response.text)
        
        if response.status_code == 200:
            print(" !! Basarili !! ")

        elif response.status_code == 401:
            print( "!! UnauthorizedError !!")
            print("Lütfen token güncelleyiniz!!")
        
        elif response.status_code == 404:
            print("!! NotFoundError !! ")
            print("Lütfen url kontrol ediniz!!")

        else:
            print("Lütfen girdiginiz degerleri kontrol edin!")








    def test_POST_yeni_deneyim_ekler():

        url="https://api.tobeto.com/api/experiences"
        token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjkwNzcsImlhdCI6MTcxNDQ2MzQwNSwiZXhwIjoxNzE0NjM2MjA1fQ.2Dywvgm65jcJSiRPSc_EbmGKEzEaDwQsGOZjwV-Qrik"
       
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
        }

        #test data
        payload={"id": 371111111111111,"corporationName": "ornek_api_kurum","position": "ornek_pozisyon","sector": "ornek_sektor","country": "Antalya",
                "StartDate": "2024-04-01","EndDate": "2024-04-26","createdAt": "2024-04-30T07:51:03.133Z","updatedAt": "2024-04-30T07:51:03.133Z",
                "description": "ornek is aciklamasi","sitemap_exclude": False }

        # JSON verisini stringe dönüştür
        payload_str = json.dumps(payload) # Gönderilecek JSON verisi str olmalı cunku Post metodu dtring aliyor
        
        # POST isteği yap
        response = requests.post(url, data = payload_str, headers=headers) #benim gonderdigim header json

        
        if response.status_code == 200:
            print(" !! Basarili !! ")

        elif response.status_code == 401:
            print( "!! UnauthorizedError !!")
            print("Lütfen token güncelleyiniz!!")
        
        elif response.status_code == 404:
            print("!! NotFoundError !! ")
            print("Lütfen url kontrol ediniz!!")

        else:
            print("Lütfen girdiginiz degerleri kontrol edin!")


print("****************************************")
TestAPIDeneyimlerim.test_POST_yeni_deneyim_ekler()
print("****************************************")
TestAPIDeneyimlerim.test_GET_kayitli_deneyimleri_getir()