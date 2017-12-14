from django.test import TestCase, RequestFactory
from fileupload.models import Document
from django.conf import settings
from fileupload.DataConversion import CSVfiletoJSONobj


class CSVfiletoJSONobjTest(TestCase):

    def setUp(self):
        self.newFile = CSVfiletoJSONobj.objects.all()

    def test_obj_has_inputpath(self):
        # Every test needs access to the request factory.
        self.assertEqual(type(newFile.inputpath), type("string"))

    def test_obj_has_outputpath(self):
        self.assertEqual(type(newFile.outputpath), type("string"))