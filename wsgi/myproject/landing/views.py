from django.shortcuts import render
from django.http import HttpResponse

from landing.models import Email 

# Create your views here.

def email(request):
    print request.POST
    email = request.POST.get('email')
    ip = request.META['REMOTE_ADDR']
    browser = request.META['HTTP_USER_AGENT']
    Email.objects.create(email = email, ip = ip, browser = browser)
    return HttpResponse('')
    
    