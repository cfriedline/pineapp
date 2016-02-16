from django.shortcuts import render
from django.contrib.gis.geos import Point
from envdata.models import Population, Sample
from django.core.urlresolvers import reverse


def index(request):
    pops = Population.objects.all().order_by('name')
    samples = Sample.objects.all().order_by('name')
    context = {'pops': pops,
               'samples': samples}
    return render(request, 'www/index.html', context)
