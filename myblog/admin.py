from django.contrib import admin
from . import models


class AboutListAdmin(admin.ModelAdmin):
    list_display = ("title",  "created")


class WorksListAdmin(admin.ModelAdmin):
    list_display = ("title",  "created")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",  "created")


admin.site.register(models.AboutList, AboutListAdmin)
admin.site.register(models.WorksList, WorksListAdmin)
admin.site.register(models.Category, CategoryAdmin)
# Register your models here.
