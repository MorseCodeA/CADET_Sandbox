from django.shortcuts import render, get_object_or_404
# Create your views here.


def index(request):
    return render(request, 'dashboard/index.html')

def topic_distribution(request):
    return render(request, 'dashboard/topic_distribution.html')

def instructor_distribution(request):
    return render(request, 'dashboard/instructor_distribution.html')

