from config import PUNK_API
import pytest

import requests

class TestUnit:


    def test_value_unit_have_litres(self):
        response = requests.get(f'{PUNK_API}/beers?brewed_before=12-2015')
        data = response.json()
        for beer in data:
            try:
                assert beer["volume"]["unit"] =="litres", f"Bear {beer['name']}  have wronk unit"
            except AssertionError as e:
                pytest.fail(str(e))




                