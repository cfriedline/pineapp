from django.db import models
from django.contrib import admin


# Create your models here.

class Library(models.Model):
    name = models.CharField(blank=False, null=False, unique=True, max_length=50)
    full = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self):
        return self.name


class LibraryCell(models.Model):
    box = models.ForeignKey(Library, null=True, blank=True, on_delete=models.PROTECT)
    row = models.CharField(blank=False, null=False, max_length=1)
    col = models.IntegerField(blank=False, null=False)

    class Meta(object):
        unique_together = (("box", "row", "col"),)

    def __str__(self):
        return "%s/%s/%d" % (self.box.name, self.row, int(self.col))


class LibraryCellInline(admin.TabularInline):
    model = LibraryCell
    max_num = 96


class LibraryAdmin(admin.ModelAdmin):
    inlines = [LibraryCellInline]
    list_display = ['name', 'full']


class LibraryCellAdmin(admin.ModelAdmin):
    inlines = []
    list_display = ['box', 'row', 'col']
