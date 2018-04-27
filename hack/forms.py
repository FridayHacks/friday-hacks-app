from django.contrib.auth.models import User
from django import forms

from .models import Team, Project, Rank

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ['team']

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['project_title','project_description','votes','proposed_by']
