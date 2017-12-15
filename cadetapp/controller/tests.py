from django.test import TestCase
from controller.views import computeTopicResults, computeInstructorResults

class computeTopicResultsTest(TestCase):

    def setUp(self):
        self.data = {
            "topic": [
                {
                    "topic_id": "1",
                    "sentiment_count": [
                        {
                            "pos": "15",
                            "neu": "5",
                            "neg": "14"
                        }
                    ]
                },
                {
                    "topic_id": "2",
                    "sentiment_count": [
                        {
                            "pos": "11",
                            "neu": "19",
                            "neg": "3"
                        }
                    ]
                },
            ]
        }

    def check_result_json(self):
        validJson = computeTopicResults(self.data).is_json
        self.assertEqual(validJson, True)

