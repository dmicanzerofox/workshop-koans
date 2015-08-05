import json
from django.core.urlresolvers import reverse
from django.test import TestCase


class APIMoneyadderTestCase(TestCase):
    """
    Create an API endpoint that can add an arbitrary number of
    decimals and return their sum.

    Data will be encoding as JSON and posted to the endpoint.

    All responses should be returned as JSON.

    Request will be of form {numbers: []} of decimal strings.

    Response JSON should be in form:
    {
        'sum': float,
        'error': mixed - string/null - string of error that occurred or
        null if request was OK
    }

    The Endpoint should be able to handle and return a couple of error
    strings
    - request is malformed
    - no numbers present
    - invalid number types

    Try to write tests first, first test should be completely filled
    out.
    """
    def test_moneyadder_multiple_numbers(self):
        numbers = [2.50, 1.75]
        request = reverse('api:moneyadder')
        response = self.client.post(
            request,
            {'numbers': numbers}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get('Content-type'), 'application/javascript')
        expected = {
            'sum': 4.25,
            'error': None
        }
        self.assertJSONEqual(response.content, expected)

    def test_moneyadder_no_numbers_returns_error(self):
        self.fail()

    def test_moneyadder_single_number_returns_itself(self):
        self.fail()

    def test_moneyadder_malformed_json(self):
        self.fail()

    def test_moneyadder_invalid_number_types(self):
        self.fail()

