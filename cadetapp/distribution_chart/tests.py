from rest_framework.test import APIRequestFactory, APITestCase
from selenium.webdriver.firefox import webdriver

class DistributionChartAPITest(APITestCase):
    """
    Test suite for validating GET requests for API in distribution_chart
    views.py
    """

    def test_api_can_get_chart_topic_json(self):
        response = self.client.get('chart/topic/data/')
        self.assertEqual(response.status_code, 200)


    def test_api_can_get_chart_instructor_json(self):
        response = self.client.get('chart/instructor/data/',
                                   format='json')
        self.assertEqual(response.status_code, 200)

    def test_api_can_get_topic_word_json(self):
        response = self.client.get('chart/word/all/')
        self.assertEqual(response.status_code, 200)



