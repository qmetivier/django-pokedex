from django.db import models


class Pokemon(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    types = models.CharField(max_length=30)
    link_img = models.CharField(max_length=100, null=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    link_detail = models.CharField(max_length=100)

    def __str__(self):
        return self.name