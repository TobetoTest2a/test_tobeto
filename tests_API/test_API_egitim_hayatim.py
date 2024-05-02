
import requests
import pytest

class TestTobetoAPI():
    def __init__(self, token):
        self.base_url = "https://api.tobeto.com/api"
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}"
        }

    def test_get_egitimler(self):
        url = f"{self.base_url}/educations"
        cevap = requests.get(url, headers=self.headers)
        return cevap.json() if cevap.status_code == 200 else None

    def test_main():
    # API token
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjkwNzcsImlhdCI6MTcxNDUwNzU3NiwiZXhwIjoxNzE0NjgwMzc2fQ.YD88QvjT7Gai-OoqwV4Nqc0vLWd4kfHOg3jsyVEB_9w"
     
    # TobetoApı yi başlatıyorum.
        api = TestTobetoAPI(token)
    
    # eğitim verilerini aldım.
        egitimler = api.test_get_egitimler()
    
   
        if egitimler:
            print("Egitim verileri:")
            print(egitimler)
        else:
            print("Eğitim verileri alınırken bir hata oluştu.")

        # if __name__ == "__main__":
        
TestTobetoAPI.test_main()

