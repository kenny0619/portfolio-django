from django.shortcuts import render
from projects.models import Project

# Create your views here.

#An index view that shows a snippet of information about each project
def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

#A detail view that shows more information on a particular topic
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)