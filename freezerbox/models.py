from django.db import models
from django.contrib import admin
from django.forms import ModelForm
from suit.widgets import SuitDateWidget

# Create your models here.

class FreezerBox(models.Model):
    name = models.IntegerField(blank=False, null=False, unique=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Box %d" % self.name


class FreezerBoxCell(models.Model):
    box = models.ForeignKey(FreezerBox, null=False, blank=False)
    row = models.CharField(max_length=1, blank=False, null=False)
    col = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return "%s: %s/%d" % (self.box, self.row, self.col)


class FreezerBoxAdmin(admin.ModelAdmin):
    list_display = ['name']


class FreezerBoxCellAdmin(admin.ModelAdmin):
    list_display = ['box', 'row', 'col']
