from django.db import models

# Create your models here.
class StudentData(models.Model):
    first_name = models.CharField(max_length=120)
    last_name  = models.CharField(max_length=120)
    number     = models.BigIntegerField()

    def __str__(self):
        return self.first_name
