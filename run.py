import pytest
from test_abv import TestAbv
from test_name import TestName
from test_unit import TestUnit
from test_image_url import TestUrl


if __name__ == '__main__':
    results = pytest.main(['-v'])
    exit(results)
