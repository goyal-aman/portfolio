from django.shortcuts import render
from django.views.generic import View

# models
from landingpage.models import Project
from resume_pdf_section.models import ResumePdfLink

# Create your views here.

class HomePageView(View):
    template_name = 'landingpage/index.html'

    def get(self, request):
        qs = {
            "project_data": Project.objects.all(),
            "data": {"link": self.get_resume_url(request)},
        }
        return render(request, self.template_name, context=qs)

    def get_resume_url(self, request):
        try:
            resumeObject:ResumePdfLink = ResumePdfLink.objects.first() 
        except Exception as e:
            # TODO : add feature to notify if resume is not fetched.
            return None

        if resumeObject:
            return resumeObject.link
        return None 
        
class ProjectView(View):
    template_name = 'landingpage/portfolio-details.html'
    def get(self, request):
        return render(request, self.template_name)