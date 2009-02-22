"""
test_models.py

Created by Dmitry Shevchenko on 2009-02-22.
"""

import unittest
from django.test.client import Client
from django.test import TestCase

from tinyurl.models import TinyURL
from hashlib import md5

class TestTinyURL(TestCase):
    def setUp(self):
        self.url = 'http://www.google.com'
        self.tinyurl = TinyURL.objects.create(url = self.url)
        self.tinyurl.save()
    
    def test_create(self):
        assert self.tinyurl
        assert self.tinyurl.url == self.url
        assert self.tinyurl.hash == md5(self.url).hexdigest()
        assert self.tinyurl.get_absolute_url() == '/tinyurl/%s/' % self.tinyurl.hash 
        
    def tearDown(self):
        self.tinyurl.delete() 
        

class TestViews(TestCase):
    def setUp(self):
        self.url = 'http://www.google.com/'
        self.tinyurl = TinyURL.objects.create(url = self.url)
        self.tinyurl.save()
    
    def tearDown(self):
        self.tinyurl.delete()
   
    def test_redirect(self):
        c = Client()
        response = c.get(self.tinyurl.get_absolute_url())
        assert response.status_code == 302