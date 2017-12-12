from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.
class DocumentationView(TemplateView):
    def home(request):
        return render(request, 'documentation/doc-home.html')
    def back_end_database(request):
        return render(request, 'documentation/back-end-database.html')
    def cadet_tutorial(request):
        return render(request, 'documentation/cadet-tutorial.html')
    def data_analysis(request):
        return render(request, 'documentation/data-analysis.html')
    def DisplayTopicCommentsFromDataLayer(request):
        return render(request,
        'documentation/DisplayTopicCommentsFromDataLayer.html')
    def enforce_code_standards(request):
        return render(request, 'documentation/enforce_code_standards.html')
    def enforce_test_before_commit(request):
        return render(request, 'documentation/enforce-test-before-commit.html')
    def file_uploader(request):
        return render(request, 'documentation/file_uploader.html')
    def instructor_topic_dashboard(request):
        return render(request, 'documentation/instructor-topic-dashboard.html')
    def metadata_retrieval(request):
        return render(request, 'documentation/metadata-retrieval.html')
    def presentation_layer_interface_for_data_results(request):
        return render(request,
        'documentation/presentation-layer-interface-for-data-results.html')
    def refactor_front_end_code(request):
        return render(request, 'documentation/refactor_front_end_code.html')
    def web_dev_docs(request):
        return render(request, 'documentation/web-dev-docs.html')
    def web_tutorial(request):
        return render(request, 'documentation/web-tutorial.html')
