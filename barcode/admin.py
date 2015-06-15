from django.contrib import admin
from barcode.models import Barcode, BarcodeAdmin

admin.site.register(Barcode, BarcodeAdmin)