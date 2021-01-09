from django.test import TestCase 

#local imports 
from portfolio.test import BaseTestUrl , BaseTestView
from timeline import views as timeline_views 

class TestTimelineHomeUrl(BaseTestUrl, TestCase):
    url_name = 'timeline-home'
    url_route = 'timeline/'
    view_class = timeline_views.CardView

class TestCardView(BaseTestView, TestCase):
    url_name = 'timeline-home'
    template_name = 'timeline/card_list_view.html'
