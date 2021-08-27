from django.urls import path

#local imports
from landingpage import views as landingpage_views

urlpatterns = [
    # path('', landingpage_views.ProjectView.as_view(), name='project'),
    path('', landingpage_views.HomePageView.as_view(), name='home'),
]