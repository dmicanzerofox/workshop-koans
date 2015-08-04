import datetime
from django.http import HttpResponse
from django.shortcuts import render


def create_widget_view(request):
    REQUIRED_PARAMS = (
        'name',
        'size',
        'weight_lbs',
        'manufactured_date',
    )
    name = request.POST['name']
    size = request.POST['size']
    weight_lbs = request.POST['weight_lbs']
    manufactured_date = request.POST['manufactured_date']

    # YOUR CODE HERE

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
    return 'success'


def unicode_test(request):
    equation = request.POST['messed_up_equation']
    # convert the iso-8859-2 string to utf-8
    return HttpResponse(equation)
