import datetime
from django.http import HttpResponse
from django.shortcuts import render
import pytz


EXPECTED_ERROR_MESSAGE_TEMPLATE = 'Error: Missing Fields: {}'

def create_widget_view(request):
    REQUIRED_PARAMS = (
        'name',
        'size',
        'weight_lbs',
        'manufactured_date',
    )

    # MODIFY BLOCK

    name = request.POST['name']
    size = request.POST['size']
    weight_lbs = request.POST['weight_lbs']
    manufactured_date = request.POST['manufactured_date']

    # MODIFY BLOCK END


    return HttpResponse(
        _create_widget(name, size, weight_lbs, manufactured_date)
    )


def _create_widget(name, size, weight_lbs, manufactured_date, color=None):
    """
    Saves a widget to the db.

    :param name:
    :param size:
    :param weight_lbs:
    :param manufactured_date:
    :return:
    """
    assert name == 'widget'
    assert size == 'large'
    shipping_box_weight = 10
    total_shipping_weight = weight_lbs + shipping_box_weight
    assert total_shipping_weight == 210
    today = datetime.date.today()
    days_old = (manufactured_date - today).days
    if color:
        assert color == 'blue'
    return 'success'


def unicode_test(request):
    """
    messed_up_equation should always be unicode when we access it
    here.  It will be encoding using iso-8859-2 character set which is
    incorrect,

    HINT:
    `encode` to a bytestring using the known encoding
    `decode` to utf-8 :)
    """
    equation = request.POST['messed_up_equation']
    # convert the iso-8859-2 string to utf-8
    return HttpResponse(equation)


def utc_conversion_test(request):
    manufactured = request.POST['manufactured_datetime']
    #  YOUR CONVERSION CODE HERE
    # http://pytz.sourceforge.net/
    utc_manufactured = ''
    return HttpResponse(utc_manufactured)
