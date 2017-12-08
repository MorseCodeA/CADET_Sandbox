from django.shortcuts import render
from django.http import HttpResponse

import requests

def index(request):
    return HttpResponse("Hello, world. You're at the results index.")

def retrieve(request,result_id):
    from django.conf import settings
    
    url = settings.GLOBAL_SETTINGS['BACKEND_URL']+'comments/%s/' % result_id
    
    resp = requests.get(url)
    response = 'URL: ' +url+' |  Request OK = ' + str(resp.ok)
    return HttpResponse(response)
