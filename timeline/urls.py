from django.urls import path

#local imports
from timeline import views as timeline_views

urlpatterns = [
    path('', timeline_views.CardView.as_view(), name='timeline-home'),
]