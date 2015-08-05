# coding=utf-8
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
        self.assertEqual(response.content, 'success')

    def test_validation_of_missing_params(self):
        """
        Modify the view to handle detecting when parameters are absent
        When a parameter is absent an HttpResponse should be returned
        of form EXPECTED_ERROR_MESSAGE_TEMPLATE.

        All fields should be ordered alpha, make requests with each field
        missing and assert that the correct error response is returned.

        Make sure to make requests with multiple fields missing!!

        :return:
        """
        EXPECTED_ERROR_MESSAGE_TEMPLATE = 'Error: Missing Fields {}'

        # example first test
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

    def test_validation_of_optional_params(self):
        """
        Add support to create_widget_view for a new parameter 'color'.
        Add two segments to this test:
        one that POSTs it to create_widget_view and asserts that a
        `success` function is returned and another that doesn't
        submit it and that asserts `success` is returned.

        :return:
        """
        self.fail()

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
        import ipdb; ipdb.set_trace();
        response = self.client.post(reverse('validation:unicode_test'), data)
        self.assertEqual(correct_equation, response.content)

    def test_utc_conversion(self):
        self.fail()
