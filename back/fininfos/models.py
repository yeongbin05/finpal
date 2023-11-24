from django.db import models
from django.conf import settings

# Create your models here.
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True) # 금융 상품 코드
    kor_co_nm = models.TextField() # 금융회사명
    fin_prdt_nm = models.TextField() # 금융상품명
    etc_note = models.TextField() # 금융 상품 설명
    join_deny = models.IntegerField() # 가입제한(1:제한없음, 2:서민전용, 3:일부제한)
    join_member = models.TextField() # 가입대상
    join_way = models.TextField() # 가입 방법
    spcl_cnd = models.TextField() # 우대조건
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_depositpds')


class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE) # 외래키
    fin_prdt_cd = models.TextField() # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100) # 저축금리 유형명
    intr_rate = models.FloatField() # 저축금리
    intr_rate2 = models.FloatField() # 최고우대금리
    save_trm = models.IntegerField() # 저축기간(단위:개월)

class SavingProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True) # 금융상품코드
    kor_co_nm = models.TextField() # 금융회사 명
    fin_prdt_nm = models.TextField() # 금융 상품명
    join_way = models.TextField() # 가입 방법
    mtrt_int = models.TextField() # 만기 후 이자율
    spcl_cnd = models.TextField() # 우대조건
    etc_note = models.TextField() # 기타 유의사항
    join_deny = models.TextField() # 가입제한
    join_member = models.TextField() # 가입대상
    max_limit = models.TextField() # 최고한도
    dcls_strt_day = models.TextField() # 공시 시작일
    fin_co_subm_day = models.TextField() #금융회사 제출일
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_savingpds')

class SavingOptions(models.Model):
    product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type = models.CharField(max_length=20) # 저축 금리 유형
    intr_rate_type_nm = models.TextField() # 저축 금리 유형명
    rsrv_type = models.TextField() # 적립 유형
    rsrv_type_nm = models.TextField() #
    save_trm = models.TextField() # 저축 기간
    intr_rate = models.TextField() # 저축 금리
    intr_rate2 = models.TextField() # 최고 우대 금리
