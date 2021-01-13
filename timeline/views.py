from typing import List
from django.shortcuts import render
from django.views.generic import ListView, View
# local imports
from timeline.models import Card, Link
from django.forms.models import model_to_dict

# general imports
from collections import defaultdict

# Create your views here.

class CardView(View):
    template_name = 'timeline/card_list_view.html'
    def get(self, request):
        cards = Card.objects.all().order_by('-date')

        qs = defaultdict(list)
        for query in cards:
            card_year = query.date.year
            query_dict = model_to_dict(query)
            query_dict['link'] = query.link.url if (query.link is not None) else None
            qs[card_year] += [query_dict]
        qs = dict(qs)
        return render(request, template_name=self.template_name, context={'timeline_data':qs})
