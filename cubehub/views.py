from django.http import HttpRequest
from django.shortcuts import render

def home(request:HttpRequest):
    return render(request, 'home.html')

def custom_404(request: HttpRequest, exception):

    return render(
        request,
        '404.html',
        status=404
    )