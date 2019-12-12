from django.db import models

from MyApp.classes.pokemon import Pokemon


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    pokemons = models.ManyToManyField(Pokemon, null=True)


    def __str__(self):
        return self.name