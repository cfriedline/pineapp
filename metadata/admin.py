from django.contrib import admin

# Register your models here.
from metadata.models import Sample, Population

admin.site.register(Sample)
admin.site.register(Population)
