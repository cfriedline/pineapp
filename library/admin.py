from django.contrib import admin
from library.models import Library, LibraryAdmin, LibraryCell, LibraryCellAdmin

admin.site.register(Library, LibraryAdmin)
admin.site.register(LibraryCell, LibraryCellAdmin)