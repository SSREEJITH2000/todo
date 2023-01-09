from django.db import models

# Create your models here.
class tasks (models.Model):
    names=models.CharField(max_length=250)
    priorities=models.IntegerField()
    dates=models.DateField()

    def __str__(self):
        return self.names
