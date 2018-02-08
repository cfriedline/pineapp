from django.conf.urls import include, url
from django.contrib import admin
from envdata.api import SampleResource, PopulationResource
from tastypie.api import Api
from www import views as www_views
from django.conf import settings
from django.conf.urls.static import static

sample_resource = SampleResource()
population_resource = PopulationResource()

v1_api = Api(api_name='v1')
v1_api.register(sample_resource)
v1_api.register(population_resource)


urlpatterns = [url('^admin/', include(admin.site.urls)),
               url('', include(admin.site.urls)),
               url('^api/', include(v1_api.urls)),
               url('^www/', www_views.index),
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
