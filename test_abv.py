from config import PUNK_API
import pytest

import requests

class TestAbv:

    def test_check_double_value(self):
        response = requests.get(f'{PUNK_API}/beers?brewed_before=12-2015')
        data = response.json()
        for beer in data:
            try:
                #print(beer["abv"])
                assert isinstance(beer["abv"],
                                  float), f"Bear {beer['name']} doesn't have a double value"
            except AssertionError as e:
                pytest.fail(str(e))
                #print(f"Asertion error: {e}")

    def test_value_not_be_null(self):
        response = requests.get(f'{PUNK_API}/beers?brewed_before=12-2015')
        data = response.json()
        for beer in data:
            try:
                assert beer["abv"] is not None, f"Bear {beer['name']}  have a NULL value"
            except AssertionError as e:
                pytest.fail(str(e))


    def test_check_emty_string(self):
        response = requests.get(f'{PUNK_API}/beers?brewed_before=12-2015')
        data = response.json()
        for beer in data:
            try:
                assert beer["abv"] !='', f"Bear {beer['name']}  have a empty value"
            except AssertionError as e:
                pytest.fail(str(e))

    def test_check_if_over_4_0(self):
        response = requests.get(f'{PUNK_API}/beers?brewed_before=12-2015')
        data = response.json()
        for beer in data:
            try:
                assert beer["abv"] >=4.0, f"Bear {beer['name']}  have lower value than 4.0"
            except AssertionError as e:
                pytest.fail(str(e))

