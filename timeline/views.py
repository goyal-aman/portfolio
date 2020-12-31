from typing import List
from django.shortcuts import render
from django.views.generic import ListView
# local imports
from timeline.models import Card

# Create your views here.

class CardListView(ListView):
    model = Card
    template_name = 'timeline/card_list_view.html'
    ordering = '-date'
