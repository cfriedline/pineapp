from django.db import models
from django.contrib import admin

# Create your models here.

class Barcode(models.Model):
    name = models.CharField(blank=False, null=False, unique=True, max_length=50)
    seq = models.CharField(blank=True, null=True, unique=True, max_length=100)

    def __str__(self):
        return self.name


class BarcodeAdmin(admin.ModelAdmin):
    list_display = ['name', 'seq']
