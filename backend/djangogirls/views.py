#views.py
from django.shortcuts import render
from django.http import HttpResponse # HttpResponse : 페이지의 응답을 전달하는 Class
# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # print(dir(request))
    print(request.POST)
    return render(request, 'index.html')