from tastypie.resources import ModelResource
from envdata.models import Sample, Population


class SampleResource(ModelResource):
    class Meta:
        queryset = Sample.objects.all()
        resource_name = 'sample'
        allowed_methods = ['get'] 


class PopulationResource(ModelResource):
    class Meta:
        queryset = Population.objects.all()
        resource_name = 'population'
        allowed_methods = ['get']
