from django.contrib import admin

# Register your models here.
from envdata.models import Sample, SampleAdmin, Population

admin.site.register(Sample, SampleAdmin)
admin.site.register(Population)
