from selenium.webdriver.firefox import webdriver
from selenium.webdriver.common.keys import Keys
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils import formats


# using selenium for functional test cases
class FunctionalCadetTest(StaticLiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.WebDriver()
        self.selenium.implicitly_wait(3)

    def tearDown(self):
        self.selenium.quit()

    # helper function to add view subdir to URL
    def _get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_home_title(self):
        """
        Tests that Dashboard title is loading properly
        """
        self.selenium.get(self._get_full_url("home"))
        self.assertIn(u'Dashboard Home', self.selenium.title)

