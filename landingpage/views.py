from django.shortcuts import render
from django.views.generic import View

# models
from landingpage.models import Project
from download_resume_pdf.models import ResumeLink

# Create your views here.

class HomePageView(View):
    template_name = 'landingpage/index.html'

    def get(self, request):
        activeResumes = ResumeLink.objects.filter(is_active=True)
        qs = {
            'project_data':Project.objects.all(),
            'resume_url': (activeResumes[0] if len(activeResumes) else [])
        }
        return render(request, self.template_name, context=qs)

class ProjectView(View):
    template_name = 'landingpage/portfolio-details.html'
    def get(self, request):
        return render(request, self.template_name)