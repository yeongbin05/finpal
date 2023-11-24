from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from .serializers import RatesSerializer
from .models import Rates
from datetime import date


@api_view(['GET'])
def get_rates(request):
    api_key = settings.RATE_API_KEY
    today = date.today()
    print(today)
    # print(type(today))
    formatted_today = str(today).replace('-', '')
    # print(formatted_today)
    # url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&searchdate={formatted_today}&data=AP01'
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&searchdate=20231117&data=AP01'

    print(url)
    response = requests.get(url).json()
    for li in response : 
        save_data = {
            'RESULT' : li.get('result'),
            'CUR_UNIT' : li.get('cur_unit'),
            'TTB' : li.get('ttb'),
            'TTS' : li.get('tts'),
            'DEAL_BAS_R' : li.get('deal_bas_r'),
            'BKPR' : li.get('bkpr'),
            'CUR_NM' : li.get('cur_nm'),
            'YY_EFEE_R' : li.get('yy_efee_r'),
            'TEN_DD_EFEE_R' : li.get('ten_dd_efee_r'),
            'KFTC_DEAL_BAS_R' : li.get('kftc_deal_bas_r'),
            'KFTC_BKPR' : li.get('kftc_bkpr'),
        }
        serializer = RatesSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    # print(save_data)
    return JsonResponse({'message':'ok'})


# def calculate_rates(request):
#     rate = list(Rates.objects.values())
    # print(111)
    # rates = RatesSerializer(rate)
    # print(222)

    # return JsonResponse(rate, safe=False)
@api_view(['GET','POST'])
def calculate_rates(request):
    rates = Rates.objects.values()
    serializers = RatesSerializer(rates,many=True)
    return Response(serializers.data)

