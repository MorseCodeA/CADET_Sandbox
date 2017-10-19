from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic


def index(request):

    # later will call dashboard or chart instance from Ashley's models,
    # which contains comments and topics

    # main dashboard located at http://example/dashboard
    return render(request, 'dashboard/index.html')

def topic_distribution(request):

    # http://example/dashboard/topic-distribution
    return render(request, 'dashboard/topic-distribution.html')

def instructor_distribution(request):

    # http://example/dashboard/instructor-distribution
    return render(request, 'dashboard/instructor-distribution.html')



# for refactoring later, when models can be instantiated for query_set

# class DashboardView(generic.ListView):
#     context_object_name = 'dashboard'
#     template_name = 'dashboard/index.html'
#
#
# class TopicDistributionView(generic.DetailView):
#     template_name = 'dashboard/topic-distribution.html'
#
#
# class InstructorDistributionView(generic.DetailView):
#     template_name = 'dashboard/instructor-distribution.html'