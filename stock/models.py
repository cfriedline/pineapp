from django.db import models
from django.contrib import admin


# Create your models here.

class Stock(models.Model):
    name = models.CharField(blank=False, null=False, unique=True, max_length=50)
    full = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self):
        return self.name


class StockCell(models.Model):
    box = models.ForeignKey(Stock, null=True, blank=True)
    row = models.CharField(blank=False, null=False, max_length=1)
    col = models.IntegerField(blank=False, null=False)

    class Meta:
        unique_together = (("box", "row", "col"),)

    def __str__(self):
        return "%s/%d" % (self.row, int(self.col))

    def sample(self):
        return self.sample_set.all()[0]


class StockCellInline(admin.TabularInline):
    model = StockCell
    max_num = 96

class StockAdmin(admin.ModelAdmin):
    inlines = [StockCellInline]
    list_display = ['name', 'full']


class StockCellAdmin(admin.ModelAdmin):
    inlines = []
    list_display = ['box', 'row', 'col', 'sample']

