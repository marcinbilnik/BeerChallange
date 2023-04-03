from config import PUNK_API
import pytest

import requests

class TestName:


    def test_value_name_not_be_null(self):
        response = requests.get(f'{PUNK_API}/beers?brewed_before=12-2015')
        data = response.json()
        for beer in data:
            try:
                assert beer["name"] is not None, f"Bear {beer['name']}  have a NULL value"
            except AssertionError as e:
                pytest.fail(str(e))


    def test_check_name_if_emty_string(self):
        response = requests.get(f'{PUNK_API}/beers?brewed_before=12-2015')
        data = response.json()
        for beer in data:
            try:
                assert beer["name"] !='', f"Bear {beer['name']}  have a empty value"
            except AssertionError as e:
                pytest.fail(str(e))


                