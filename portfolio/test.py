from django.test import Client 
from django.urls import resolve, reverse
from django.views.generic import View

# Create your tests here.

class BaseTest:
    """ Base Test Class """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = Client()
        self.response, self.resolver = \
            self.get_response_and_resolver(self.client)

    def get_response_and_resolver(self, client):
        """ method to get `response` and `resovler object` of curr `url_name` """
        path = reverse(self.url_name)
        response = self.client.get(path)
        resolver = resolve(path)
        return response, resolver
        

class BaseTestUrl(BaseTest):

    url_name : str
    view_class : View
    url_route  : str
    
    def test_url_response(self):
        self.assertTrue(self.response.status_code==200)
    
    def test_url_view_used(self):
        self.assertTrue(self.resolver.func.view_class==self.view_class)
    
    def test_url_name(self):
        self.assertTrue(self.resolver.url_name==self.url_name)
    
    def test_url_route(self):
        self.assertTrue(self.resolver.route==self.url_route)
    
class BaseTestView(BaseTest):
    url_name : str 
    template_name  : str

    # TODO: add test to check context data returned by view | maybe this is custom to each view?

    def test_view_url_name(self):
        """ test urlpattern used by views (name parameter of url_pattern) """
        self.assertTrue(self.resolver.url_name==self.url_name)
        assert True

    def test_view_template_name(self):
        """ test template used by view  """
        self.assertTemplateUsed(self.response, self.template_name)
    
    def test_view_response(self):
        self.assertTrue(self.response.status_code==200)
