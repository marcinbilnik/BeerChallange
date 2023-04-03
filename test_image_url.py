from config import PUNK_API
import pytest

import requests

class TestUrl:


    def test_image_url(self):
        response = requests.get(f'{PUNK_API}/beers?brewed_before=12-2015')
        data = response.json()
        for beer in data:
            try:
                assert beer["image_url"].startswith("https://") or beer["image_url"].startswith("http://"), f"Bear {beer['name']}  have a wronk image link"
            except AssertionError as e:
                pytest.fail(str(e))




                