from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

import requests

from rest_framework.decorators import api_view, permission_classes

# Create your views here.

def get_remote_data(tracking_number=''):
    if tracking_number:
        headers={'Authorization': 'JsonWebToken {}'.format(settings.TOKEN)}
        r = requests.get('https://bps.bringer.dev/public/api/v2/get/parcel/tracking.json?tracking_number={}'.format(tracking_number), headers=headers)
        return r.json()
    return None


@api_view(['GET', 'POST'])
def get_parcel_tracking(request):
    tracking_number = request.GET.get('tracking_number', '')
    data = get_remote_data(tracking_number)
    if data:
        return JsonResponse(data, safe=False)
    return JsonResponse({'ERROR': 'tracking_number is required'})
