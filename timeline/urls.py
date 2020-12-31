from django.urls import path

#local imports
from timeline import views as timeline_views

urlpatterns = [
    path('', timeline_views.CardListView.as_view(), name='timeline-home'),
]