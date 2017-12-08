from django.shortcuts import render
from django.http import HttpResponse
import polling, requests

def index(request):
    return HttpResponse("Hello, world. You're at the results index.")

def retrieve(request,result_id):
    from django.conf import settings
    
    url = settings.GLOBAL_SETTINGS['BACKEND_URL']+'users/%s/' % result_id
    response = 'URL: ' +url+' | Resp OK = '
    
    try:
        polling.poll(lambda: requests.get(url).status_code == 200,
                     step=1,
                     max_tries=5)
        resp = requests.get(url)
        response = response + 'OK'
    except polling.MaxCallException:
        response = response + 'FAIL'
        
    return HttpResponse(response)
