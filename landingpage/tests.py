from django.test import TestCase
#local imports 
from portfolio.test import BaseTestUrl, BaseTestView
from landingpage import views as landingpage_views

# Create your tests here.

class TestHomeUrl(BaseTestUrl, TestCase):
    url_name = 'home'
    url_route = ''
    view_class = landingpage_views.HomePageView

class TestHomePageView(BaseTestView, TestCase):
    url_name = 'home'
    template_name = 'landingpage/index.html'