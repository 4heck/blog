from django.contrib import admin
from .models import Post, Tag
from import_export.admin import ImportExportModelAdmin


# admin.site.register(Post)
# admin.site.register(Tag)

@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin):
    pass
