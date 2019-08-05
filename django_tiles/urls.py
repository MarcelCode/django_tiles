"""django_tiles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from main.models import Field, Stroke

urlpatterns = [
    path('admin/', admin.site.urls),
    path('raster/', include('raster.urls')),
    path("", TemplateView.as_view(template_name="neu.html")),
    path("fields.geojson", GeoJSONLayerView.as_view(model=Field), name='fields'),
    path("strokes.geojson", GeoJSONLayerView.as_view(model=Stroke), name='strokes')
]
