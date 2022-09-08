from django.urls import path
from . import views # 현재 디렉토리에서 views.py 가져오기
urlpatterns = [
    #/myuser/register/로 요청이 들어오면, views.py에 register 함수 실행
    path('register/',views.register),
]
