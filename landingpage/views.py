from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class HomePageView(View):
    template_name = 'landingpage/index.html'

    def get(self, request):
        return render(request, self.template_name)

class ProjectView(View):
    template_name = 'landingpage/portfolio-details.html'
    def get(self, request):
        return render(request, self.template_name)