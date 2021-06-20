from django.http.response import HttpResponse
from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponse

class ViewTestCase(TestCase):
    def test_login_link(self):
        '''
        login view retuns an HttpResponse
        '''
        response = self.client.get(reverse('userreviews:login'))
        self.assertIsInstance(response, HttpResponse)
        