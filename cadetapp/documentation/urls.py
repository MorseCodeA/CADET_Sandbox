from django.conf.urls import url
from .views import DocumentationView

urlpatterns = [
    url('doc-home', DocumentationView.home, name="doc-home.html"),

    # go here http://localhost:8000/dashboard/documentation/back-end-database
    # and it will work, but with no styling from your html
    url('back-end-database', DocumentationView.back_end_database,
        name="back-end-database.html"),

    # go here http://localhost:8000/dashboard/documentation/cadet-tutorial
    # and it will also work, but with the dashboard styling and wrapper
    url('cadet-tutorial', DocumentationView.cadet_tutorial,
        name="cadet-tutorial.html"),

    url('data-analysis', DocumentationView.data_analysis,
        name="data-analysis.html"),
    url('display-topic-comments',
        DocumentationView.DisplayTopicCommentsFromDataLayer,
        name="DisplayTopicCommentsFromDataLayer.html"),
    url('enforce-code-standards', DocumentationView.enforce_code_standards,
        name="enforce-code-standards.html"),
    url('enforce-test-before-commit',
        DocumentationView.enforce_test_before_commit,
        name="enforce-test-before-commit.html"),
    url('file-uploader-doc', DocumentationView.file_uploader,
        name="file_uploader.html"),
    url('instructor-topic-dashboard',
        DocumentationView.instructor_topic_dashboard,
        name="instructor-topic-dashboard.html"),
    url('metadata-retrieval', DocumentationView.metadata_retrieval,
        name="metadata-retrieval.html"),
    url('presentation-layer-interface-for-data-results',
        DocumentationView.presentation_layer_interface_data_results,
        name="presentation-layer-interface-for-data-results.html"),
    url('refactor-front-end-code', DocumentationView.refactor_front_end_code,
        name="refactor_front_end_code.html"),
    url('web-dev-docs', DocumentationView.web_dev_docs,
        name="web-dev-docs.html"),
    url('web-tutorial', DocumentationView.web_tutorial,
        name="web-tutorial.html"),
]
