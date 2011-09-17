from django.db import models

# Create your models here.

class Asunto(models.Model):
    osoite = models.CharField(max_length=40)
    asukkaiden_maara = models.IntegerField()

    def __unicode__(self):
        return self.osoite

class Asukas(models.Model):
    nimi = models.CharField(max_length=40)
    osoite = models.ForeignKey(Asunto)

    def __unicode__(self):
        return self.nimi