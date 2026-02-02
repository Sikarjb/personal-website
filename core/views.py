from django.shortcuts import render


# Create your views here.
def home (request):
    return render(request, 'home.html')


from .models import Project

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})


from  .models import Skill

def skills(request):
    skills =Skill.objects.all()
    return render(request, 'skills.html', {'skills': skills})