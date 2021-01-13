from typing import List
from django.shortcuts import render
from django.views.generic import ListView, View
# local imports
from timeline.models import Card

# general imports
from collections import defaultdict

# Create your views here.

class CardView(View):
    template_name = 'timeline/card_list_view.html'
    def get(self, request):
        # cards = Card.objects.all().order_by('-date').prefetch_related('link').values()
        cards = Card.objects.all().order_by('-date').values()
        
        qs = defaultdict(list)
        for query in cards:
            card_year = query['date'].year
            # link_id = query.pop('link_id', None)
            # if link_id is not None:
                # query['link'] = Link.objects.get(id=link_id).url
            qs[card_year] += [query]
        qs = dict(qs)
        return render(request, template_name=self.template_name, context={'timeline_data':qs})
