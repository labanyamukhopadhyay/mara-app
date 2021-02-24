from django.db import models

# Create your models here.
class Report(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=20)
    dob = models.CharField(max_length=4)
    id_notes = models.TextField()
    data_owners = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    bio = models.TextField()
    image = models.FilePathField(path="/img")