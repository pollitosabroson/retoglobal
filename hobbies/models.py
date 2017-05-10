from django.db import models

# Create your models here.


class Hobbie(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Hobbie"
        verbose_name_plural = "Hobbies"

    def __str__(self):
        '''
        Return value name
        '''
        return self.name
