from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Team, Project, Rank
from .forms import UserForm
from .models import Project
from .serializers import ProjectSerializer
from datetime import datetime

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'hack/login.html')
    else:
        projects = Project.objects.all()
        return render(request, 'hack/index.html', {
                'projects': projects
        })


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'hack/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                projects = Project.objects.filter()
                return render(request, 'hack/index.html', {'projects': projects})
            else:
                return render(request, 'hack/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'hack/login.html', {'error_message': 'Invalid login'})
    return render(request, 'hack/login.html')


def signup(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #projects = Project.objects.filter(user=request.user)
                return render(request, 'hack/index.html')#, {'projects': projects})
    context = {
        "form": form,
    }
    return render(request, 'hack/signup.html', context)


def propose(request):

    if not request.user.is_authenticated():
        return render(request, 'hack/login.html')
    else:
        return render(request, 'hack/propose.html')


def propose_project(request):

    if request.method == 'POST':
        project_title = request.POST['title']
        project_description = request.POST['description']
        proposed_by = request.user
        date = datetime.now()
        status = "Proposed"
        votes = 0

        project = Project(project_title=project_title,
                        project_description=project_description,
                        proposed_by=proposed_by,
                        status=status,
                        date=date,
                        votes=votes)
        project.save()
        projects = Project.objects.all()
        context = {
            'message': 'Success. Project Proposed!',
            'color': 'green',
            'projects' : projects
        }
        return render(request, 'hack/index.html', context)
    context = {
            'message': 'Error. Try again.',
            'color': 'red',
        }
    return render(request, 'hack/index.html', context)



def teams(request):

    if not request.user.is_authenticated():
        return render(request, 'hack/login.html')
    else:
        return render(request, 'hack/teams.html')


class ProjectList(APIView):

    def get(self,request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects,many=True)
        return Response(serializer.data)

    def post(self):
        pass
