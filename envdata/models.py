from django.db import models
from django.contrib import admin
from django.forms import ModelForm, CharField
from suit.widgets import SuitDateWidget
from library.models import LibraryCell
from stock.models import StockCell
from plate.models import PlateCell
from barcode.models import Barcode
from django.contrib.gis.geos import Point
from django import forms
from grappelli_filters import SearchFilter
import numpy as np

# Create your models here.


class Population(models.Model):
    name = models.CharField(max_length=20, blank=False,
                            null=False, unique=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Sample(models.Model):
    population = models.ForeignKey(Population, null=True, blank=True, on_delete=models.PROTECT)
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

    stock_cell = models.ForeignKey(StockCell, blank=True, null=True, on_delete=models.SET_NULL)
    library_cell = models.ForeignKey(LibraryCell, blank=True, null=True, on_delete=models.SET_NULL)
    plate_cell = models.ForeignKey(PlateCell, blank=True, null=True, on_delete=models.SET_NULL)

    usable = models.BooleanField(blank=False, null=False, default=True)

    @property
    def stock(self):
        if self.stock_cell:
            return "%s/%s/%s" % (self.stock_cell.box.name, self.stock_cell.row, self.stock_cell.col)
        return None

    @property
    def library(self):
        if self.library_cell:
            return "%s/%s/%s" % (self.library_cell.box.name, self.library_cell.row, self.library_cell.col)
        return None

    @property
    def plate(self):
        if self.plate_cell:
            return "%s/%s/%s" % (self.plate_cell.plate.name, self.plate_cell.row, self.plate_cell.col)
        return None

    def __str__(self):
        return self.name

    @property
    def geom(self):
        if self.lon > 0:
            print("bad value for %s" % self.name)
            self.lon = -self.lon
        return Point(self.lon, self.lat, srid=4326)

    @property
    def species(self):
        return self.name[0]

    @property
    def bark_avg_mm(self):
        factor = 25.4
        if self.bark1 and self.bark2 and self.bark3 and self.bark4:
            return np.mean([self.bark1, self.bark2, self.bark3, self.bark4]) * factor
        return None

    @property
    def height_calc(self):
        if self.height:
            return self.height

        if self.angle_low and self.angle_high:
            a1 = np.radians(self.angle_low)
            a2 = np.radians(self.angle_high)
            return (np.tan(a1) * self.angle_distance) + (np.tan(a2) * self.angle_distance)

        if self.angle_high and not self.angle_low:
            a1 = np.radians(self.angle_high)
            return np.tan(a1) * self.angle_distance

        return np.nan

    def boxes(self):
        return "%s, stock=%s, library=%s, plate=%s" % (self.name,
                                                       self.stock_cell,
                                                       self.library_cell,
                                                       self.plate_cell)


class SampleForm(ModelForm):
    class Meta:
        model = Sample
        exclude = ['stock_cell', 'library_cell', 'plate_cell']
        # exclude = []
        widgets = {
            'sample_date': SuitDateWidget,
        }
        readonly_fields = ['stock', 'library']


class SampleInline(admin.StackedInline):
    model = Sample
    exclude = ['stock_cell', 'library_cell', 'plate_cell']
    max_num = 15
    extra = 15
    readonly_fields = ['stock', 'library']


class SampleAdmin(admin.ModelAdmin):
    list_display = ['name', 'population', 'sample_date', 'stock', 'library', 'plate']
    search_fields = ['name', 'stock_cell__box__name', 'library_cell__box__name', 'plate_cell__plate__name']
    form = SampleForm
    list_per_page = 20


class PopulationAdmin(admin.ModelAdmin):
    inlines = [SampleInline]
    list_per_page = 20
    list_display = ['name', 'notes']
    search_fields = ['name']
