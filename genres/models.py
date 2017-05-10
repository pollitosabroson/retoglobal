from django.db import models


# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        '''
        Return value name
        '''
        return self.name
