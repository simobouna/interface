from django.db import models

# Create your models here.
class Groupe(models.Model):
    IdGroupe = models.CharField(max_length=50, primary_key=True)
    Groupe = models.CharField(max_length=50)

class Tag(models.Model):
    Tag = models.CharField(max_length=50, primary_key=True)

class Device(models.Model):
    Devui = models.CharField(max_length=50, primary_key=True)
    Name = models.CharField(max_length=50, default='NRGYBOX')
    IdGroupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    Tag = models.ManyToManyField(Tag)
    IdLora = models.CharField(max_length=50)