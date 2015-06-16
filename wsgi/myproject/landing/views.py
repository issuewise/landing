from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from landing.models import Email 

# Create your views here.

def email(request):
    email = request.POST.get('email')
    try:
        Email.objects.get(email=email)
    except MultipleObjectsReturned:
        pass
    except ObjectDoesNotExist:
        ip = request.META['REMOTE_ADDR']
        browser = request.META['HTTP_USER_AGENT']
        Email.objects.create(email = email, ip = ip, browser = browser)
    return HttpResponse('')
    
    