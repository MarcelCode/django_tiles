from django.contrib.gis import admin
from .models import Field, Stroke

# Register your models here.
admin.site.register(Stroke, admin.GeoModelAdmin)
admin.site.register(Field, admin.GeoModelAdmin)
