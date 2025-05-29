import requests
from django.conf import settings

class ExternalAPIClient:
    def __init__(self):
        self.base_url = 'TU_API_BASE_URL'
        self.api_key = 'TU_API_KEY'

    def get_movies(self, page=1):
        response = requests.get(
            f"{self.base_url}/movies",
            params={
                'api_key': self.api_key,
                'page': page
            }
        )
        return response.json()

    def get_series(self, page=1):
        response = requests.get(
            f"{self.base_url}/tv",
            params={
                'api_key': self.api_key,
                'page': page
            }
        )
        return response.json()