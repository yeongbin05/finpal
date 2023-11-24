import random
import requests

first_name_samples = "김이박최정강조윤장임"
middle_name_samples = "민서예지도하주윤채현지"
last_name_samples = "준윤우원호후서연아은진"


en_first_name = ['James ','Robert ','Mary ','Patricia ','John ','Jennifer ','Michael ','Linda ','David ','Elizabeth ']
en_last_name = ['William','Barbara','Richard','Susan','Joseph','Jessica','Thomas','Sarah','Christopher','Karen']

jp_last_name = ['佐藤 ','鈴木 ','高橋 ','田中 ','伊藤 ','渡辺 ','山本 ','中村 ','山田 ','斎藤 ']
jp_first_name = ['陽葵','凛','詩','陽菜','結菜','杏','澪','結愛','芽依','莉子']

ch_last_name = ['王','李','张','刘','陈','杨','黄','赵','吴','周']
ch_first_name = ['沐宸','若汐','浩宇','一诺','沐辰','艺涵','茗泽','依诺','奕辰','梓涵']
def random_name():
    result = ""
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result + str(random.randint(1, 100))

def en_random_name():
    result = ""
    result += random.choice(en_first_name)
    result += random.choice(en_last_name)
    return result + str(random.randint(1, 100))

def jp_random_name():
    result = ""
    result += random.choice(jp_last_name)
    result += random.choice(jp_first_name)
    return result + str(random.randint(1, 100))

def ch_random_name():
    result = ""
    result += random.choice(ch_last_name)
    result += random.choice(ch_first_name)
    return result + str(random.randint(1, 100))
DP_URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
SP_URL = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'

API_KEY = '42c6bf74f01388098e16a1d1d9ae51da'

financial_products = []

params = {
  'auth': API_KEY,
  # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
  'topFinGrpNo': '020000',
  'pageNo': 1
}

# 정기예금 목록 저장
response = requests.get(DP_URL, params=params).json()
baseList = response.get('result').get('baseList')   # 상품 목록

for product in baseList:
    financial_products.append(product['fin_prdt_cd'])

# 적금 목록 저장
response = requests.get(SP_URL, params=params).json()
baseList = response.get('result').get('baseList')   # 상품 목록

for product in baseList:
    financial_products.append(product['fin_prdt_cd'])
# print(financial_products)
dict_keys = ['username', 'gender', 'financial_products', 'age', 'money', 'salary']

# json 파일 만들기
import json
from collections import OrderedDict

file = OrderedDict()

username_list = []
N = 10000
i = 0

while i < N:
    rn = random.choice([random_name(),en_random_name(),jp_random_name(),ch_random_name()])
    if rn in username_list:
        continue
    
    username_list.append(rn)
    i += 1
print(username_list)

save_dir = 'back/accounts/fixtures/accounts/data.json'

# save_dir = 'data.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')
    
    for i in range(N):
        # 랜덤한 데이터를 삽입
        file["model"] = "accounts.User"
        file["pk"] = i+1
        file["fields"] = {
            'username': username_list[i],  # 유저 이름 랜덤 생성
            # 랜덤한 0~5개의 상품을 가입하도록 삽입됨
            'financial_products': ','.join([random.choice(financial_products) for _ in range(random.randint(0, 5))]), # 금융 상품 리스트
            'age': random.randint(1, 100),  # 나이
            'money': random.randrange(0, 100000000, 100000),    # 현재 가진 금액
            'salary': random.randrange(0, 1500000000, 1000000), # 연봉
            'password': "1234",
            'nickname': None,
            'is_active': True,
            'is_staff': False,
            'is_superuser': False
        }

        json.dump(file, f, ensure_ascii=False, indent="\t")
        if i != N-1:
            f.write(',')
    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')
