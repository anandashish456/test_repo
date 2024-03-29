from unittest import TestCase
from unittest.mock import patch
import simple_get.app


class TestTheGet(TestCase):
    def test_url(self):
        with patch('simple_get.app.requests.get') as mocked_call:
            simple_get.app.call_func()
            mocked_call.assert_called_with("https://www.google.com")

    def test_check_print(self):
        with patch('builtins.print') as mocked_print:
            simple_get.app.call_func()
            mocked_print.assert_called_with(200)

