from django.db import models

# Create your models here.


class ToDo(models.Model):
    Title= models.CharField(max_length=100,blank=False)
    Description=models.CharField(max_length=200,blank=False)
    Date=models.DateField(blank=False)
    Completed=models.BooleanField(blank=False)

    def __str__(self):
        return self.Title