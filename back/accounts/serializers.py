from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.core.validators import RegexValidator

class CustomRegisterSerializer(RegisterSerializer):
    # 기본 설정 필드: username, password1, password2, email
    # 추가 설정 필드: iD, age, telphone
    # iD = serializers.
    telphoneRegex = RegexValidator(regex=r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    telphone = serializers.CharField(validators=[telphoneRegex],help_text="휴대폰 번호는 다음과 같은 형식을 따라야 합니다: 010-1234-5678")
    realname = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255
    )
    age = serializers.IntegerField(required=False)
    money = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    financial_products = serializers.ListField(child=serializers.IntegerField(), required=False)
    
    def get_cleaned_data(self):
        return {
        'username': self.validated_data.get('username', ''),
        'password1': self.validated_data.get('password1', ''),
        'realname': self.validated_data.get('realname', ''),
        'age': self.validated_data.get('age', ''),
        'money': self.validated_data.get('money', ''),
        'salary': self.validated_data.get('salary', ''),
        'financial_products': self.validated_data.get('financial_products', ''),
        'telphone': self.validated_data.get('telphone', ''),
        'email': self.validated_data.get('email', ''),
        }
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user
