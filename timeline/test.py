from django.test import TestCase 

#local imports 
from portfolio.test import BaseTestUrl , BaseTestView
from timeline import views as timeline_views 
from timeline.models import Card

class TestTimelineHomeUrl(BaseTestUrl, TestCase):
    url_name = 'timeline-home'
    url_route = 'timeline/'
    view_class = timeline_views.CardView

class TestCardView(BaseTestView, TestCase):
    url_name = 'timeline-home'
    template_name = 'timeline/card_list_view.html'

class TestCardModel(TestCase):
    def setUp(self) -> None:
        self.card1 = Card.objects.create(
            body = "this is body 1",
            heading = "this is heading 1"
        )
        self.card2 = Card.objects.create(
            body = "this is body 2",
            heading = "this is heading 2"
        )

    def test_card_count(self):
        self.assertTrue(Card.objects.count() == 2)
    
    def test_card_update(self):
        card1 = Card.objects.first()
        card2 = Card.objects.last()
        
        card1.heading = "new_heading1"
        card1.body = "new_body1"

        card2.heading = "new_heading2"
        card2.body = "new_body2"

        card1.save()
        card2.save()

        card1 = Card.objects.first()
        card2 = Card.objects.last() 

        self.assertTrue(card1.body=="new_body1")
        self.assertTrue(card1.heading=="new_heading1")
    
        self.assertTrue(card2.body=="new_body2")
        self.assertTrue(card2.heading=="new_heading2")