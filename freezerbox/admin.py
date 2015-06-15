from django.contrib import admin

# Register your models here.
from freezerbox.models import FreezerBox, FreezerBoxCell, FreezerBoxAdmin, FreezerBoxCellAdmin

admin.site.register(FreezerBox, FreezerBoxAdmin)
admin.site.register(FreezerBoxCell, FreezerBoxCellAdmin)
