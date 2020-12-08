import os
import base64
from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Coordinate)
class CoordinateModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'lon', 'lat')
    list_display_links = ['lon', ]

    def save_model(self, request, obj, form, change):
        obj.save()

    def delete_model(self, request, obj):
        obj.delete()

    def delete_queryset(self, request, queryset):
        """ TODO 删除查询集中的模板 """
        for obj in queryset:
            self.delete_model(request, obj)


@admin.register(UserSubmitInfo)
class UserSubmitInfoModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'contact_info', 'contact_content', 'create_time')
    list_display_links = ['username', ]

    def save_model(self, request, obj, form, change):
        obj.save()

    def delete_model(self, request, obj):
        obj.delete()

    def delete_queryset(self, request, queryset):
        """ TODO 删除查询集中的模板 """
        for obj in queryset:
            self.delete_model(request, obj)
