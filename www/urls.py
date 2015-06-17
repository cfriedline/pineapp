from . import views
from django.conf.urls import url, include, patterns
from djgeojson.views import GeoJSONLayerView, TiledGeoJSONLayerView
from envdata.models import Sample

urlpatterns = patterns('',
                       url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Sample,
                                                                       properties=['name','species']), name='data'),
                       url(r'^$', views.index, name='index'), )
