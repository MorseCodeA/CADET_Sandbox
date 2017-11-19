from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.
class DocumentationView(TemplateView):
    def home(request):
        return render(request, 'documentation/doc-home.html')