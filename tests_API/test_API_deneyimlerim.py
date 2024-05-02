import pytest
import requests
import json
import softest
from tests_API.API_constants import *


class TestAPIDeneyimlerim(softest.TestCase): 
        
    
    def test_GET_kayitli_deneyimleri_getir(self):
        
        end_point= base_url+ "/experience/my"

        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
        }

        response = requests.get(end_point, headers=headers)
        
        response_data = response.json() # JSON yanıtını işle
       
        # İlk öğeyi seç
        user_data = response_data[0] 
        
        
        if response.status_code == 200:
            print(" !! Basarili !! ")
            #self.soft_assert(self.assertEqual,expected_corporationName,user_data['corporationName'],"corporationName hatali!!")
            
            assert (expected_corporationName == user_data['corporationName'] and expected_position== user_data['position'] and
                   expected_country == user_data['country'] and expected_sector == user_data['sector'] and 
                   expected_EndDate == user_data['EndDate'] and expected_StartDate == user_data['StartDate'])    
        else:
            print("Lütfen girdiginiz degerleri kontrol edin!")


    def test_POST_yeni_deneyim_ekler(self):

        end_point=base_url+"/experiences"
        token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjkwNzcsImlhdCI6MTcxNDQ2MzQwNSwiZXhwIjoxNzE0NjM2MjA1fQ.2Dywvgm65jcJSiRPSc_EbmGKEzEaDwQsGOZjwV-Qrik"
       
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
        }

        #test data
        payload={"data":{"corporationName":"otomasyondanGelen","position":"selenium","sector":"bilgi teknolojileri",
                  "country":"Balıkesir","StartDate":"2024-04-01T00:00:00+03:00",
                  "EndDate":"2024-04-06T00:00:00+03:00","description":"otomasyon yap"}}

        # JSON verisini stringe dönüştür
        payload_str = json.dumps(payload) # Gönderilecek JSON verisi str olmalı cunku Post metodu dtring aliyor
        
        # POST isteği yap
        response = requests.post(end_point, data = payload_str, headers=headers) #benim gonderdigim header json
        print(response.text)
        
        if response.status_code == 200:
            print(" !! Basarili !! ")

        else:
            print("Lütfen girdiginiz degerleri kontrol edin!")


