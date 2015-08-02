from django.core.urlresolvers import reverse
from django.test import TestCase


class ValidationKoansTestCase(TestCase):

    def test_validation_on_correct_types(self):
        params = {

        }
        response = self.client.post(
            reverse('validation:correct_types'), params)
        self.assertEqual(response.status_code, 200)
        self.fail()

    def test_validation_of_missing_params(self):
        self.fail()

    def test_validation_of_optional_params(self):
        self.fail()

    def test_unicode_conversion(self):
        self.fail()

    def test_utc_conversion(self):
        self.fail()
