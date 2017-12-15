from django.db import models
from django.test import TestCase
from .models import Results_Set

class Results_SetTest(TestCase):
    def test_model_results_set(self):
        result_test = Results_Set.objects.create(1, True)
        self.assertTrue(result_test(instance))



