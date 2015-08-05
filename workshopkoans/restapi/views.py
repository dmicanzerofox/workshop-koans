from decimal import Decimal
import json
from django.http import HttpResponse
from django.shortcuts import render


def moneyadder(request):
    # YOUR CODE HERE

    response = {}
    return HttpResponse(
        json.dumps(response),
        content_type='application/javascript'
    )
