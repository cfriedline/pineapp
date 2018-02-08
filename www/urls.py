

import views
from django.conf.urls import url
from djgeojson.views import GeoJSONLayerView, TiledGeoJSONLayerView
from envdata.models import Sample

urlpatterns = [url(r'^data.geojson$',
               GeoJSONLayerView.as_view(model=Sample,
                                        properties=['name', 'species']),
               name='data'),
               url(r'^$', views.index, name='index')]
