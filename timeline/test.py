from django.test import TestCase 

#local imports 
from portfolio.test import BaseTestUrl , BaseTestView
from timeline import views as timeline_views 
from timeline.models import Card, Link

class TestTimelineHomeUrl(BaseTestUrl, TestCase):
    url_name = 'timeline-home'
    url_route = 'timeline/'
    view_class = timeline_views.CardView

class TestCardView(BaseTestView, TestCase):
    url_name = 'timeline-home'
    template_name = 'timeline/card_list_view.html'

class TestCardModel(TestCase):
    def setUp(self) -> None:
        link = Link.objects.create(url='www.example.com')
        self.card1 = Card.objects.create(
            body = "this is body 1",
            heading = "this is heading 1"
        )
        self.card2 = Card.objects.create(
            body = "this is body 2",
            heading = "this is heading 2"
        )

        self.card3 = Card.objects.create(
            body = "body3",
            heading = "heading3",
            link = link
        )

    def test_card_count(self):
        self.assertTrue(Card.objects.count() == 3)
    
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
    
    def test_card_with_link(self):
        card = Card.objects.get(id=3)
        self.assertTrue(card.link.url == "www.example.com")
    
    def test_card_with_link_url_update(self):
        """ testing that changing url of card link workd """
        card = Card.objects.get(id=3)
        old_link = card.link
        new_link = "www.update.com"
        card.link.url = new_link
        card.save()

        self.assertFalse(card.link.url==old_link)
        self.assertTrue(card.link.url==new_link)

    def test_card_with_link_delete(self):
        """ testing when link is deleted, its value is set to null in `link` field in card """
        
        # confirming card has link before testing
        card = Card.objects.get(id=3)
        self.assertTrue(card.link!=None)
        
        # actual test
        link = Link.objects.first()
        link.delete()
        card = Card.objects.get(id=3)
        self.assertTrue(card.link == None)