from django.contrib import admin
from plate.models import Plate, PlateAdmin, PlateCell, PlateCellAdmin

admin.site.register(Plate, PlateAdmin)
admin.site.register(PlateCell, PlateCellAdmin)