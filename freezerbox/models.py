from django.db import models
from django.contrib import admin
from django.forms import ModelForm
from suit.widgets import SuitDateWidget

# Create your models here.

class FreezerBox(models.Model):
    name = models.CharField(max_length=10, blank=False, null=False, unique=True)
    notes = models.TextField(blank=True, null=True)
    STOCK = "STK"
    LIBRARY = "LIB"
    KIND_CHOICES = (
        (STOCK, "Stock"),
        (LIBRARY, "Library")
    )
    kind = models.CharField(max_length=3, choices=KIND_CHOICES, default=STOCK)

    def __str__(self):
        return self.name


class FreezerBoxCell(models.Model):
    box = models.ForeignKey(FreezerBox, null=False, blank=False)
    row = models.CharField(max_length=1, blank=False, null=False)
    col = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return "%s: %s/%d" % (self.box, self.row, self.col)

    class Meta:
        unique_together = (("box", "row", "col"),)


class FreezerBoxAdmin(admin.ModelAdmin):
    list_display = ['name']


class FreezerBoxCellAdmin(admin.ModelAdmin):
    list_display = ['box', 'row', 'col']
