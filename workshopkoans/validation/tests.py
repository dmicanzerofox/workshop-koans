from django.core.urlresolvers import reverse
from django.test import TestCase


class ValidationKoansTestCase(TestCase):

    def test_validation_on_correct_types(self):
        """
        Modify the `create_widget_view` so that the request.POST
        parameters are converted to the correct types.

        :return:
        """
        params = {
            'manufactured_date': '2015-08-02',
            'size': 'large',
            'weight_lbs': '200',
            'name': 'widget'
        }
        response = self.client.post(
            reverse('validation:create_widget'), params)
        self.assertEqual(response.status_code, 200)

    def test_validation_of_missing_params(self):
        self.fail()

    def test_validation_of_optional_params(self):
        self.fail()

    def test_unicode_conversion(self):
        self.fail()

    def test_utc_conversion(self):
        self.fail()
