
import requests

class TobetoAPI:
    def __init__(self, token):
        self.base_url = "https://api.tobeto.com/api"
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}"
        }

    def get_egitimler(self):
        url = f"{self.base_url}/educations"
        cevap = requests.get(url, headers=self.headers)
        return cevap.json() if cevap.status_code == 200 else None

def main():
    # API token
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjkwNzcsImlhdCI6MTcxNDQ4NjI2OCwiZXhwIjoxNzE0NjU5MDY4fQ.5dxCDDcZv5TvsQYlwGf6KUVHvItJJuyKoRdPsp05gNY"
    
    # TobetoApı yi başlatıyorum.
    api = TobetoAPI(token)
    
    # eğitim verilerini aldım.
    egitimler = api.get_egitimler()
    
   
    if egitimler:
        print("Egitim verileri:")
        print(egitimler)
    else:
        print("Eğitim verileri alınırken bir hata oluştu.")

if __name__ == "__main__":
    main()

