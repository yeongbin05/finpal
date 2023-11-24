import json 
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomRegisterSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import base64
import matplotlib.pyplot as plt
from io import BytesIO


# Create your views here.
def profile(request, username):
    # User의 Detail 페이지
    # User를 조회
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def profile_list(request, username):
    if request.method == 'GET':
        user = get_object_or_404(User, username=username)
        serializer = CustomRegisterSerializer(user)
        # print(serializer.data)
        return Response(serializer.data)
    
@api_view(['GET'])
def recommend(request):
    # print(1111111111111111111111)
    file_path = 'accounts/fixtures/accounts/data.json'
    # print(22222222222222)
    with open(file_path,'r',encoding='utf-8') as json_file:
        # print(333333333333333333)

        data = json.load(json_file)
        # print(4444444444444444444)

        # print(data)
    # print(5555555555555555)
    # print(data)
    # ratio = [34, 32, 16, 18]
    # labels = ['Apple', 'Banana', 'Melon', 'Grapes']

    # plt.pie(ratio, labels=labels, autopct='%.1f%%')
    # plt.show()

    # buffer = BytesIO()
    # plt.savefig(buffer,format='png')
    # image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    # buffer.close()
    return Response(data)