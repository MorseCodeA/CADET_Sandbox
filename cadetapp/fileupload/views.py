from django.conf import settings
from django.contrib import messages
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .DataConversion import CSVfiletoJSONobj
from .forms import DocumentForm, JsonForm
from .models import Document
from .PushJSON import DataPush
from results.views import retrieve
import os,json

def option_view(request):
    """
    Purpose: This function is the main view for the upload options
    page. The page objects are generated with the JsonForm. The
    form inputs are pulled in from the Django models and used to
    create the JSON transport file
    """
    if request.method == 'POST':
        form = JsonForm(request.POST)
        #On POST pull CSV to “Download” folder and call Data Conversion method
        if form.is_valid():
            media_path = settings.MEDIA_ROOT + '/downloads/'
            comments = form.cleaned_data['comments']
            topics = form.cleaned_data['topics']
            iterations = form.cleaned_data['iterations']
            JSONinput = CSVfiletoJSONobj()
            JSONinput._init_()
            JSONinput.set_input_path(form.cleaned_data['files'])
            JSONinput.set_output_path(media_path
                                      + str('cadet-file-to-json.json'))
            JSONinput.CSVtoJSON_Obj()
            messages.info(request,
                          'The JSON file has been successfully created!')

            PushDataToDataTeam = DataPush()
            PushDataToDataTeam._init_()

            resultset_id = PushDataToDataTeam.PushJSONObject(
                comments,
                topics,
                iterations,
                media_path + str('cadet-file-to-json.json'))

            messages.info(request,
                          'The JSON file has been successfully created!')
            return redirect(retrieve,result_id=resultset_id)
    else:
        form = JsonForm()
    return render(request, 'options.html', {'form': form})
# END option_view(request)

def upload_view(request):
    """
    Purpose: This function is the main view for the file upload
    page. Uses the the default Django file upload documentation
    with a model and form
    """
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            for a_file in files:
                Document(file=a_file).save()
            return redirect('options.html')
    else:
        form = DocumentForm()
    return render(request, 'file_upload.html', {'form': form})
# END def upload_view

def upload_progress(request):
    """
    Purpose: This function uses Ajax calls to return the upload progress
    and total length values for the progress bar
    Works in conjunction with upload_progress$ url.
    """
    if 'X-Progress-ID' in request.GET:
        progress_id = request.GET['X-Progress-ID']
    elif 'X-Progress-ID' in request.META:
        progress_id = request.META['X-Progress-ID']
    else:
        progress_id = None

    if progress_id:
        cache_key = "%s_%s" % (request.META['REMOTE_ADDR'], progress_id)
        data = cache.get(cache_key)
        return HttpResponse(json.dumps(data))
# END def upload_progress
