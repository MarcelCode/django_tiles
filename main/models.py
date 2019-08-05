from django.db import models
from django.contrib.gis.db import models


class Stroke(models.Model):
    internal_id = models.IntegerField()
    geom = models.PolygonField(srid=4326)


class Field(models.Model):
    internal_id = models.IntegerField()
    geom = models.PolygonField(srid=4326)

