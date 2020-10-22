from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def reverse(request):
    return render(request, 'reverse.html')
