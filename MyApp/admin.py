from django.contrib import admin

from MyApp.classes.Team import Team
from MyApp.classes.pokemon import Pokemon
# Register your models here.

admin.site.register(Pokemon)
admin.site.register(Team)

