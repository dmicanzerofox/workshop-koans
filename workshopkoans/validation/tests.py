# coding=utf-8
from django.core.urlresolvers import reverse
from django.test import TestCase
from validation.views import EXPECTED_ERROR_MESSAGE_TEMPLATE


class ValidationTypesTestCase(TestCase):

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
        self.assertEqual(response.content, 'success')

class ValidationMissingParamsTestCase(TestCase):
    """
    Modify the view to handle detecting when parameters are absent
    When a parameter is absent an HttpResponse should be returned
    of form EXPECTED_ERROR_MESSAGE_TEMPLATE.

    All fields should be sorted alphabetically in error message

    :return:
    """

    def test_validation_of_missing_single_param(self):
        params = {
            'manufactured_date': '2015-08-02',
            'size': 'large',
            'weight_lbs': '200',
        }
        response = self.client.post(
            reverse('validation:create_widget'), params)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.content, EXPECTED_ERROR_MESSAGE_TEMPLATE.format('name'))

    def test_validation_of_multiple_missing_params(self):
        params = {
            'manufactured_date': '2015-08-02',
            'size': 'large',
            }
        response = self.client.post(
            reverse('validation:create_widget'), params)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.content,
            EXPECTED_ERROR_MESSAGE_TEMPLATE.format(
                ','.join(['name', 'weight_lbs'])
            )
        )

class ValidationOptionalParamsTestCase(TestCase):
    """
    Add support to create_widget_view for a new parameter 'color'.

    :return:
    """
    def test_validation_optional_param_in_request(self):
        params = {
            'manufactured_date': '2015-08-02',
            'size': 'large',
            'weight_lbs': '200',
            'name': 'widget',
            'color': 'blue'
        }
        response = self.client.post(
            reverse('validation:create_widget'), params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'success')

    def test_validation_optional_param_missing(self):
        params = {
            'manufactured_date': '2015-08-02',
            'size': 'large',
            'weight_lbs': '200',
            'name': 'widget',
        }
        response = self.client.post(
            reverse('validation:create_widget'), params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'success')

class ValidationUnicodeTestCase(TestCase):
    def test_unicode_conversion(self):
        """
        A client is sending iso-8859-2 strings but our application
        expects utf-8.  Since the client has specified an encoding of
        iso-8859-2 we can safely convert it to utf-8 so
        our system can handle it.  Convert the string in `unicode_test`
        so that the view responds with utf8 bytestring.

        :return:
        """
        correct_equation = u'\u2203y \u2200x \xac(x \u227a y)'.encode('utf-8')
        # mis-encoded to 'iso-8859-2'
        messed_up = u'\xe2\x88\x83y \xe2\x88\x80x \xc2\u0179(x \xe2\x89\u015f y)'
        data = {
            'messed_up_equation': messed_up
        }
        response = self.client.post(reverse('validation:unicode_test'), data)
        self.assertEqual(correct_equation, response.content)

class ValdationUTCConversionTestCase(TestCase):
    def test_utc_conversion(self):
        """
        Clients input their dates in 'US/Eastern' timezone.

        Convert the user submitted time to UTC

        :return:
        """
        post_data = {
            'manufactured_datetime': '2014-02-01 00:11:01'
        }
        request = self.client.post(
            reverse('validation:utc_conversion_test'), post_data)
        self.assertEqual(request.content, '2014-02-01 05:11:01')
