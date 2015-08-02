from django.test import TestCase


class APIMoneyadderTestCase(TestCase):
    """
    Create an API endpoint that can add an arbitrary number of
    decimals and return their sum.

    Data will be encoding as JSON and posted to the endpoint.

    All responses should be returned as JSON.

    Request JSON will be an array of decimal strings.

    Response JSON should be in form:
    {
        'sum': decimal string,
        'error': mixed - string/null - string of error that occurred or
        null if request was OK
    }

    The Endpoint should be able to handle and return a couple of error
    strings
    - request JSON is malformed
    - no numbers present
    - invalid number types
    """
    def test_moneyadder_no_numbers_returns_error(self):
        self.fail()

    def test_moneyadder_single_number_returns_itself(self):
        self.fail()

    def test_moneyadder_multiple_numbers(self):
        self.fail()

    def test_moneyadder_malformed_json(self):
        self.fail()

    def test_moneyadder_invalid_number_types(self):
        self.fail()

