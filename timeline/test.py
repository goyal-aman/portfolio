from django.test import TestCase 

#local imports 
from portfolio.test import BaseTestUrl 
from timeline import views as timeline_views 

class TestTimelineHomeUrl(BaseTestUrl, TestCase):
    url_name = 'timeline-home'
    url_route = 'timeline/'
    view_class = timeline_views.CardView