from django.conf.urls import patterns, include, url
from django.contrib import admin
from envdata.api import SampleResource, PopulationResource
from tastypie.api import Api

sample_resource = SampleResource()
population_resource = PopulationResource()

v1_api = Api(api_name='v1')
v1_api.register(sample_resource)
v1_api.register(population_resource)

urlpatterns = patterns('', url(r'^grappelli/', include('grappelli.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', include(admin.site.urls)),
                       url(r'^api/$', include(v1_api.urls)))
