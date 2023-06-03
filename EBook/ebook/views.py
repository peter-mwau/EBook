from django.shortcuts import render
import requests


def home(request):
    return render(request, 'home2.html')

