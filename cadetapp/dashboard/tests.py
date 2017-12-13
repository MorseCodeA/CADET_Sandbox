from django.test import TestCase, RequestFactory
from .views import DashboardView

class DashboardViewTest(TestCase):
    """
    Testing GET requests for all views in DashboardView class
    """

    def setUp(self):
        self.factory = RequestFactory()

    def test_get_index(self):
        # Create an instance of a GET request for index
        request = self.factory.get('/dashboard/index')
        response = DashboardView.as_view()(request)
        self.assertEqual(response.status_code, 200)


    def test_get_topic_distribution(self):
        # Create an instance of a GET request for index
        request = self.factory.get('/dashboard/topic-distribution')

        response = DashboardView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_get_instructor_distribution(self):
        # Create an instance of a GET request for index
        request = self.factory.get('/dashboard/instructor-distribution')

        response = DashboardView.as_view()(request)
        self.assertEqual(response.status_code, 200)


    def test_get_stopword(self):
        # Create an instance of a GET request for index
        request = self.factory.get('/dashboard/stopword')

        response = DashboardView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_get_about(self):
        # Create an instance of a GET request for index
        request = self.factory.get('/dashboard/about')

        response = DashboardView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_get_export(self):
        # Create an instance of a GET request for index
        request = self.factory.get('/dashboard/export')

        response = DashboardView.as_view()(request)
        self.assertEqual(response.status_code, 200)


    def test_get_after_upload_options(self):
        # Create an instance of a GET request for index
        request = self.factory.get('/dashboard/options')

        response = DashboardView.as_view()(request)
        self.assertEqual(response.status_code, 200)