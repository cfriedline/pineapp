from django.db import models
from django.contrib import admin
from django.forms import ModelForm
from suit.widgets import SuitDateWidget
from freezerbox.models import FreezerBoxCell
from plate.models import PlateCell
from barcode.models import Barcode
from django.contrib.gis.geos import Point

# Create your models here.


class Population(models.Model):
    name = models.CharField(max_length=20, blank=False,
                            null=False, unique=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Sample(models.Model):
    population = models.ForeignKey(Population, null=True, blank=True)
    name = models.CharField(max_length=20, blank=False, null=False,
                            unique=True)
    sample_date = models.DateField(null=True, blank=False)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    dbh = models.FloatField(blank=True, null=True)
    angle_low = models.FloatField(blank=True, null=True)
    angle_high = models.FloatField(blank=True, null=True)
    angle_distance = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    bark1 = models.FloatField(blank=True, null=True)
    bark2 = models.FloatField(blank=True, null=True)
    bark3 = models.FloatField(blank=True, null=True)
    bark4 = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    stock_cell = models.ForeignKey(FreezerBoxCell, blank=True, null=True, related_name="stock",
                                   on_delete=models.SET_NULL)
    library_cell = models.ForeignKey(FreezerBoxCell, blank=True, null=True, related_name="library",
                                     on_delete=models.SET_NULL)
    plate_cell = models.ForeignKey(PlateCell, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    @property
    def geom(self):
        if self.lon > 0:
            print "bad value for %s" % self.name
            self.lon = -self.lon
        return Point(self.lon, self.lat, srid=4326)

    @property
    def species(self):
        return self.name[0]


class SampleForm(ModelForm):
    class Meta:
        model = Sample
        exclude = []
        widgets = {
            'sample_date': SuitDateWidget,
        }


class SampleInline(admin.StackedInline):
    model = Sample
    max_num = 15
    extra = 15


class SampleAdmin(admin.ModelAdmin):
    list_display = ['name', 'population', 'sample_date']
    form = SampleForm


class PopulationAdmin(admin.ModelAdmin):
    inlines = [SampleInline]
    list_display = ['name', 'notes']
