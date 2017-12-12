from django.conf.urls import url
from .views import DocumentationView

urlpatterns = [
    url('/', DocumentationView.home, name="doc-home.html"),
    url('/', DocumentationView.back_end_database, name="back-end-database.html"),
    url('/', DocumentationView.cadet_tutorial, name="cadet-tutorial.html"),
    url('/', DocumentationView.data_analysis, name="data-analysis.html"),
    url('/', DocumentationView.DisplayTopicCommentsFromDataLayer, name="DisplayTopicCommentsFromDataLayer.html"),
    url('/', DocumentationView.enforce_code_standards, name="enforce-code-standards.html"),
    url('/', DocumentationView.enforce_test_before_commit, name="enforce-test-before-commit.html"),
    url('/', DocumentationView.file_uploader, name="file_uploader.html"),
    url('/', DocumentationView.instructor_topic_dashboard, name="instructor-topic-dashboard.html"),
    url('/', DocumentationView.metadata_retrieval, name="metadata-retrieval.html"),
    url('/', DocumentationView.presentation_layer_interface_for_data_results, name="presentation-layer-interface-for-data-results.html"),
    url('/', DocumentationView.refactor_front_end_code, name="refactor_front_end_code.html"),
    url('/', DocumentationView.web_dev_docs, name="web-dev-docs.html"),
    url('/', DocumentationView.web_tutorial, name="web-tutorial.html"),
]
