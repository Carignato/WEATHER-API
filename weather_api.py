from utils import Config, City, CityInfo
import os
import geocoder
import requests
from typing import Dict, Any


class WeatherApi:
    def __init__(
        self,
        api_key: str,
        api_key_bing_portal: str,
        lang: str = "pt-br",
        metric: str = "metric",
    ) -> None:
        self.secrets = Config.AWS_CONFIG.get_secret_aws(os.getenv("API_SECRETS"))
        self.apy_key = api_key
        self.api_key_bing_portal = api_key_bing_portal
        self.base_url_weather = self.secrets["base_url"]
        self.lang = lang
        self.metric = metric
        city = self.get_city_from_user()
        city_info = self.__get_city_by_lat_lng(city)
        self.__weather_api_request_post(city_info)

    def get_city_from_user(city) -> None:

        city = input("Digite o nome de uma cidade: ")

        return city

    def __get_city_by_lat_lng(self, city: City) -> Dict:

        try:
            response = geocoder.bing(f"{city}", key=f"{self.api_key_bing_portal}")

        except Exception as error:
            raise error

        city_info: CityInfo = CityInfo(
            lat=response.json["lat"], lng=response.json["lng"]
        )

        return city_info

    def __weather_api_request_post(self, city_info: CityInfo) -> Dict[str, Any]:

        path_params = {
            "lat": city_info.lat,
            "lng": city_info.lng,
            "appid": self.apy_key,
            "units": self.metric,
        }

        try:

            request = requests.get(url=self.base_url_weather, params=path_params)

        except requests.RequestException as error:
            raise error

        return request.json()
