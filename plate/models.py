from django.db import models
from django.contrib import admin
from barcode.models import Barcode

# Create your models here.

class Plate(models.Model):
    name = models.CharField(blank=False, null=False, unique=True, max_length=50)
    full = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self):
        return self.name


class PlateCell(models.Model):
    plate = models.ForeignKey(Plate, null=True, blank=True)
    row = models.CharField(blank=False, null=False, max_length=1)
    col = models.IntegerField(blank=False, null=False)
    barcode = models.ForeignKey(Barcode, blank=True, null=True)

    class Meta:
        unique_together = (("plate", "row", "col"),)

    def __str__(self):
        return "%s/%d" % (self.row, int(self.col))


class PlateCellInline(admin.TabularInline):
    model = PlateCell
    max_num = 96

class PlateAdmin(admin.ModelAdmin):
    inlines = [PlateCellInline]
    list_display = ['name']



class PlateCellAdmin(admin.ModelAdmin):
    inlines = []
    list_display = ['plate', 'row', 'col', 'barcode']
