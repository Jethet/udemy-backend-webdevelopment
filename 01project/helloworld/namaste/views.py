from django.shortcuts import render
from django.http import HttpResponse

def namaste(request):
    return HttpResponse('Namaste means Hello in India, just like Namaskar.')
