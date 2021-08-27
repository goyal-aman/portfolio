from django.shortcuts import render
from django.views.generic import View

# models
from landingpage.models import Project

# Create your views here.

class HomePageView(View):
    template_name = 'landingpage/index.html'

    def get(self, request):
        qs = {'project_data':Project.objects.all()}
        return render(request, self.template_name, context=qs)

class ProjectView(View):
    template_name = 'landingpage/portfolio-details.html'
    def get(self, request):
        return render(request, self.template_name)