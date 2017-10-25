import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.core.cache import cache
from django.shortcuts import render, redirect
from fileupload.forms import DocumentForm
from fileupload.models import Document

def index(request):

    # later will call instances from Ashley's models,
    # which contains comments and topics
    # main dashboard located at http://example/dashboard
    return render(request, 'dashboard/index.html')

def topic_distribution(request):

    # http://example/dashboard/topic-distribution
    return render(request, 'dashboard/topic-distribution.html')

def instructor_distribution(request):
    # http://example/dashboard/instructor-distribution
    return render(request, 'dashboard/instructor-distribution.html')

def upload_view(request):
    documents = Document.objects.all()
    return render(request, 'dashboard/file_upload.html', {'documents':
                                                          documents})
def file_upload(request):
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            for a_file in files:
                Document(file=a_file).save()
            return redirect('dashboard/file_upload.html')
    else:
        form = DocumentForm()
    return render(request, 'dashboard/file_upload.html', {'form': form})

def upload_progress(request):
    # Uses Ajax calls to return the upload progress and total length values
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

def stopword_view(request):
    return render(request, 'dashboard/stopword.html')

def about_view(request):
    return render(request, 'dashboard/about.html')

def export_view(request):
    return render(request, 'dashboard/export.html')



# for refactoring later, when models can be instantiated for query_set

# class DashboardView(generic.ListView):
#     context_object_name = 'dashboard'
#     template_name = 'dashboard/index.html'
#

# class TopicDistributionView(generic.DetailView):
#     template_name = 'dashboard/topic-distribution.html'
#
#
# class InstructorDistributionView(generic.DetailView):
#     template_name = 'dashboard/instructor-distribution.html'