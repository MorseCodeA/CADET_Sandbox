from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Results_Set
from dashboard.views import DashboardView
import json, polling, random as rng, requests

""" results.view documentation
Purpose: Create views fuction to retrieve results from data layer and store it
    using Results_Set model from /models.py

Functions:   
    retrieve(request,result_id): gather results pertaining to resutls_id from
        backend database
"""

def retrieve(request,result_id):
    """
    Purpose: Retrieve data from either the database created by back end or 
    alternativly, if that is unavailable, through a URL that contains a 
    randomly generated JSON in a specific template

    Return: HTTP response

    How: Use polling to ping the website and store the json in the 
    Results_Set model from .models.py.
    
    Template expected can be found in Results-example.json
    """
    USE_ALTERNATIVE_URL=False    # Takes precident
    USE_PLACEHOLDER_URL=False
    if (USE_ALTERNATIVE_URL):
        url = settings.GLOBAL_SETTINGS['ALTERNATIVE_URL']
    elif (USE_PLACEHOLDER_URL):
        url = settings.GLOBAL_SETTINGS['PLACEHOLDER_URL'] + '%s/' % result_id
    else:
        url = settings.GLOBAL_SETTINGS['BACKEND_URL'] + '%s/' % result_id    

    response = 'URL: ' +url+' | Resp = '
    
    try:
        # poll the results table and get the JSON object when complete
        polling.poll(lambda: requests.get(url).status_code == 200,
                     step=settings.POLLING_SETTINGS['TIMEOUT'],
                     max_tries=settings.POLLING_SETTINGS['RETRIES'])
        jsonObj = requests.get(url).json()

        # create a new result set to store the data
        resultset = Results_Set()

        # if useing the alternative url, save it up
        if (USE_ALTERNATIVE_URL):
            resultset.id = 1
            resultset.jsonObj = jsonObj[0]

        # if using the placeholder url, shove in the data
        elif USE_PLACEHOLDER_URL:
            resultset.id = jsonObj['id'];
            fakedResult={'result_id':jsonObj['id'],
                         'meta_file_info':{},
                         'results':{'topics_stats':[],'instructor_stats':[]}
            }
            # Fake Metadata
            fakedMeta={'document_id_number':rng.randint(1,1000),
                       'user_selected_number_topics':rng.randint(1,5),
                       'user_selected_number_interations':rng.randint(1,30),
                       'user_selected_number_words_per_topic':rng.randint(1,5)}
            fakedResult['meta_file_info']=fakedMeta
            
            #Fake Topic Results
            fakedTopic_comments={
                'positive':jsonObj['company']['name'].split(),
                'neutral':jsonObj['company']['catchPhrase'].split(),
                'negative':jsonObj['company']['bs'].split()}                
            fakedTopic_stats={'words':jsonObj['website'].split(),
                              'comments':fakedTopic_comments}
            fakedTopicStatsList=[fakedTopic_stats,fakedTopic_stats]
            fakedResult['results']['topics_stats']=fakedTopicStatsList
            
            #Fake Instructor Results
            fakedInstr_comments={
                'positive':jsonObj['address']['street'].split(),
                'neutral':jsonObj['address']['suite'].split(),
                'negative':jsonObj['address']['city'].split()}
            fakedInstr_stats={
                'instructor_first_name':jsonObj['name'].split()[0],
                'instructor_first_name':jsonObj['name'].split()[0],
                'course_num_sect_id':jsonObj['address']['geo']['lat'],
                'comments':fakedInstr_comments}
            fakedInstrList=[fakedInstr_stats,fakedInstr_stats]
            fakedResult['results']['instructor_stats']=fakedInstrList
            resultset.jsonObj = fakedResult
        #END elif (USE_PLACEHOLDER_URL)
        
        else:
            resultset.id = result_id
            resultset.jsonObj = jsonObj
        
        resultset.save()
        response = response + 'OK'
    except polling.MaxCallException:
        response = response + 'FAIL'      
    #return HttpResponse(response)
    return redirect('/dashboard/topic-distribution')

def index(request):
    return HttpResponse("Hello, world. You're at the results index.")


