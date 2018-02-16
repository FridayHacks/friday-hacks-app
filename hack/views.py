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
from .serializers import ProjectSerializer

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'hack/login.html')
    else:
        projects = Project.objects.all()
        teams = Team.objects.all()
        ranks = Rank.objects.all()
        return render(request, 'hack/index.html', {
                'projects': projects,
                'teams': teams,
                'ranks': ranks
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



def projects(request):

    if not request.user.is_authenticated():
        return render(request, 'hack/login.html')
    else:
        return render(request, 'hack/projects.html')

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
