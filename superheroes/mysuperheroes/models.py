from django.db import models


# Create your models here.


class SuperHero(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    primary_ability = models.CharField(max_length=50)
    secondary_ability = models.CharField(max_length=50)
    catch_phrase = models.CharField(max_length=100)


def myfunc():
    print()


