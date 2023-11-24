
from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.contrib.auth import get_user_model
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
import requests
from .serializers import DepositOptionsSerializer, DepositProductsSerializer,SavingProductsSerializer,SavingOptionSerializer
from .models import DepositProducts, DepositOptions,SavingOptions,SavingProducts
import random
import pprint
from django.db.models import F, ExpressionWrapper, FloatField
BASE_URL = 'http://finlife.fss.co.kr/finlifeapi/'

# Create your views here.

# @api_view(['GET'])
# def api_test(request):
#     print(111111)
#     URL = BASE_URL + 'depositProductsSearch.json'
#     params = {
#         'auth' :settings.API_KEY,
#         'topFinGrpNo' : '020000',
#         'pageNo' :  1
#     }
#     print(44444)
#     response = requests.get(URL, params).json()
#     print(2222222)

#     print(response)
#     print(3333333)
#     return JsonResponse({'response':response})


@api_view(['GET'])
def save_deposit_products(request):
    api_key = settings.API_KEY
    page = 1
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo={page}'
    response = requests.get(url).json()

    
    for li in response.get("result").get("baseList"):
        
        
        
        save_data = {
            'fin_prdt_cd' : li.get('fin_prdt_cd'),
            'kor_co_nm' : li.get('kor_co_nm'),
            'fin_prdt_nm' : li.get('fin_prdt_nm'),
            'etc_note' : li.get('etc_note'),
            'join_deny' : li.get('join_deny'),
            'join_member' : li.get('join_member'),
            'join_way' : li.get('join_way'),
            'spcl_cnd' : li.get('spcl_cnd'),
        }
        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    

    for li in response.get("result").get('optionList'):
        # print(1111111111)
        save_data = {
            'fin_prdt_cd' : li.get('fin_prdt_cd'),
            'intr_rate_type_nm' : li.get('intr_rate_type_nm'),
            'intr_rate' : li.get('intr_rate'),
            'intr_rate2' : li.get('intr_rate2'),
            'save_trm' : li.get('save_trm'),
        }
        print(222222222)
        product = DepositProducts.objects.get(fin_prdt_cd = save_data['fin_prdt_cd'])
        print(3333333)
        if not save_data['intr_rate']:
            save_data['intr_rate'] = -1

        serializer = DepositOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)
    

    return JsonResponse({'message':'okay'})
@api_view(['GET'])
def save_saving_products(request):
    api_key = settings.API_KEY
    # page = 1
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()

    
    for li in response.get("result").get("baseList"):
        
        
        
        save_data = {
            'dcls_month' : li.get('dcls_month'),
            'fin_prdt_cd' : li.get('fin_prdt_cd'),
            'kor_co_nm' : li.get('kor_co_nm'),
            'fin_prdt_nm' : li.get('fin_prdt_nm'),
            'join_way' : li.get('join_way'),
            'mtrt_int' : li.get('mtrt_int'),
            'spcl_cnd' : li.get('spcl_cnd'),
            'etc_note' : li.get('etc_note'),
            'join_deny' : li.get('join_deny'),
            'join_member' : li.get('join_member'),
            'max_limit' : li.get('max_limit'),
            'dcls_strt_day' : li.get('dcls_strt_day'),
            'fin_co_subm_day' : li.get('fin_co_subm_day'),
            
        }
        if not save_data['max_limit']:
            save_data['max_limit'] = -1
        serializer = SavingProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    # print('saved')

    for li in response.get("result").get('optionList'):
        print(1111111111)
        save_data = {
            'fin_prdt_cd' : li.get('fin_prdt_cd'),
            'intr_rate_type' : li.get('intr_rate_type'),
            'intr_rate_type_nm' : li.get('intr_rate_type_nm'),
            'rsrv_type' : li.get('rsrv_type'),
            'rsrv_type_nm' : li.get('rsrv_type_nm'),
            'save_trm' : li.get('save_trm'),
            'intr_rate' : li.get('intr_rate'),
            'intr_rate2' : li.get('intr_rate2'),
        }
        # print(save_data['fin_prdt_cd'])
        # print(2222)
        product = SavingProducts.objects.get(fin_prdt_cd = save_data['fin_prdt_cd'])
        # print(3333333)
        if not save_data['intr_rate']:
            save_data['intr_rate'] = -1

        serializer = SavingOptionSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)
    
    # print('saved2')

    return JsonResponse({'message':'okay'})
    



@api_view(['GET','POST'])
def deposit_products(request,page_pk):
    if request.method=='GET':
        # depositProducts = DepositProducts.objects.all()
        items_per_page = 10
        
        # 시작 인덱스 계산
        start_index = (page_pk - 1) * items_per_page

        # 종료 인덱스 계산
        end_index = start_index + items_per_page

        # depositProducts 가져오기
        depositProducts = DepositProducts.objects.order_by('id')[start_index:end_index]        
        serializer = DepositProductsSerializer(depositProducts, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        temp_data = {
            'fin_prdt_cd' : 'TEST001',
            'kor_co_nm' : 'SSAFY은행',
            'fin_prdt_nm' : '텐션업10기예금',
            'etc_note' : '자유',
            'join_deny' : 1,
            'join_member' : '실명의 개인',
            'join_way' : '스마트폰',
            'spcl_cnd' : '해당사항 없음',
        }
        serializer = DepositProductsSerializer(data=temp_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return JsonResponse({ 'message': 'okay' })
@api_view(['GET','POST'])
def saving_products(request,page_pk):
    if request.method=='GET':
        items_per_page = 10
        
        # 시작 인덱스 계산
        start_index = (page_pk - 1) * items_per_page

        # 종료 인덱스 계산
        end_index = start_index + items_per_page

        # depositProducts 가져오기
        savingProducts = SavingProducts.objects.order_by('id')[start_index:end_index]
        
        serializer = SavingProductsSerializer(savingProducts, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        temp_data = {
            'fin_prdt_cd' : 'TEST001',
            'kor_co_nm' : 'SSAFY은행',
            'fin_prdt_nm' : '텐션업10기예금',
            'join_way' : '스마트폰',
            'mtrt_int' : '만기 후 1개월 미만',
            'spcl_cnd' : '해당사항 없음',
            'etc_note' : '자유',
            'join_deny' : 1,
            'join_member' : '실명의 개인',
            'max_limit' : '50000',
            'dcls_strt_day' : '20231117',
            'fin_co_subm_day' : '202311171017',

        }
        serializer = SavingProductsSerializer(data=temp_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return JsonResponse({ 'message': 'okay' })


@api_view(['GET'])
def deposit_products_options(request,fin_prdt_cd):
    print(111111)
    product = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    # print(product[0])
    serializer = DepositOptionsSerializer(product[0])
    return Response(serializer.data)


@api_view(['GET'])
def top_rate(request):
    
    product = DepositOptions.objects.all().order_by('-intr_rate2')
    serializer = DepositOptionsSerializer(product[0])
    fin_prdt_cd = serializer.data.get('fin_prdt_cd')
    product2 = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    serializer2 = DepositProductsSerializer(product2)
    response_data = {
        'deposit_products': serializer2.data,
        'options': serializer.data,
        
    }
    
    return Response(response_data)

@api_view(['GET'])
def deposit_products_detail(request,product_pk):
    product = get_object_or_404(DepositProducts,pk=product_pk)
    if request.method == 'GET':
        serializer = DepositProductsSerializer(product)
        print(serializer.data)
        return Response(serializer.data)
    

@api_view(['GET'])
def saving_products_detail(request,saving_pk):
    saving = get_object_or_404(SavingProducts,pk=saving_pk)
    if request.method == 'GET':
        serializer = SavingProductsSerializer(saving)
        print(serializer.data)
        return Response(serializer.data)
    

@api_view(['GET'])
def saving_products_options(request,fin_prdt_cd):
    saving = SavingOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = SavingOptionSerializer(saving[0])
    return Response(serializer.data)



@api_view(['GET'])
def recommend(request):
    deposit = DepositProducts.objects.all()
    saving = SavingProducts.objects.all()

    deposit_serializer = DepositProductsSerializer(deposit, many=True)
    saving_serializer = SavingProductsSerializer(saving, many=True)

    # 직렬화된 데이터 얻기
    serialized_deposit = deposit_serializer.data
    serialized_saving = saving_serializer.data
    combined_data = {'deposit_products': serialized_deposit, 'saving_products': serialized_saving}
    random.shuffle(combined_data['deposit_products'])
    random.shuffle(combined_data['saving_products'])

    # 랜덤으로 두 개의 응답을 선택
    response_data = {
        'response_1': random.choice(combined_data['deposit_products'] + combined_data['saving_products']),
        'response_2': random.choice(combined_data['deposit_products'] + combined_data['saving_products']),
        'response_3': random.choice(combined_data['deposit_products'] + combined_data['saving_products']),
        'response_4': random.choice(combined_data['deposit_products'] + combined_data['saving_products']),
        'response_5': random.choice(combined_data['deposit_products'] + combined_data['saving_products']),
    }
    return Response ( response_data)
# int_rate+int_rate2+save_trm이 큰 순대로 정렬하고 복리인 것과 아닌 것 나눠서 복리 상위 5개 아닌거 5개 출력하고 다시 그중에 상위 5개
@api_view(['GET'])
def recommend2(request):
    options_with_weighted_value = DepositOptions.objects.annotate(
        weighted_value=ExpressionWrapper(
            F('intr_rate') + F('intr_rate2') + F('save_trm'),
            output_field=FloatField()
        )
    )

    # 값이 큰 순서대로 정렬
    sorted_options = options_with_weighted_value.order_by('-weighted_value')

    # 'intr_rate_type_nm'이 '복리'인 데이터 필터링
    filtered_options = sorted_options.filter(intr_rate_type_nm='복리')

    # 'intr_rate_type_nm'이 '복리'인 데이터를 제외한 데이터 필터링
    other_options = sorted_options.exclude(intr_rate_type_nm='복리')

    # 'intr_rate_type_nm'이 '복리'인 데이터를 상위 5개로 제한
    top_5_filtered_options = filtered_options[:5]

    # 'intr_rate_type_nm'이 '복리'인 데이터를 제외한 데이터를 상위 5개로 제한
    top_5_other_options = other_options[:5]

    # 상위 5개의 데이터를 합쳐서 최종 결과 생성
    result = list(top_5_filtered_options.values(
        'product__fin_prdt_cd',
        'product__kor_co_nm',
        'product__fin_prdt_nm',
        'intr_rate_type_nm',
        'intr_rate',
        'intr_rate2',
        'weighted_value'
    )) + list(top_5_other_options.values(
        'product__fin_prdt_cd',
        'product__kor_co_nm',
        'product__fin_prdt_nm',
        'intr_rate_type_nm',
        'intr_rate',
        'intr_rate2',
        'weighted_value'
    ))

    # result를 json 형식으로 구성하여 반환
    response_data = {
        'top_5_sorted_and_filtered_deposit_options': result[:5]
    }

    return Response(response_data)


@api_view(['GET'])
def deposit_likes(request, username, depositproducts_pk):

    depositpd = get_object_or_404(DepositProducts, pk=depositproducts_pk)
    user = get_user_model().objects.get(username=username)
    my_depositpds = user.depositproducts_set.all()
    serializer = DepositProductsSerializer(my_depositpds, many=True)

    if user.id in depositpd.like_users.all():
        depositpd.like_users.remove(user)
    else:
        depositpd.like_users.add(user)
    return Response(serializer.data)


@api_view(['GET'])
def saving_likes(request, username, savingproducts_pk):

    

    savingpd = get_object_or_404(SavingProducts, pk=savingproducts_pk)
    user = get_user_model().objects.get(username=username)
    my_savingpds = user.savingproducts_set.all()
    serializer = DepositProductsSerializer(my_savingpds, many=True)

    if user in savingpd.like_users.all():
        savingpd.like_users.remove(user)
    else:
        savingpd.like_users.add(user)
    return Response(serializer.data)