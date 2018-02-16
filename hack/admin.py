from django.contrib import admin

from .models import Team, Project, Rank

admin.site.register(Team)
admin.site.register(Project)
admin.site.register(Rank)

