from django.db import models

from genres.models import Genre
from hobbies.models import Hobbie


# Create your models here.


class User(models.Model):
    age = models.CharField(max_length=255)
    genre = models.ForeignKey(
        Genre
    )
    hobbies = models.ManyToManyField(
        Hobbie
    )
    last_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Userss"

    def __str__(self):
        '''
        Return value full name
        '''
        return '{} {}'.format(self.name, self.last_name)
