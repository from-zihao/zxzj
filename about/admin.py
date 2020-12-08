from django.contrib import admin
from .models import *
import os
import shutil
import base64
# Register your models here.


@admin.register(About)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_title')
    fields = ('about_title', 'title_image', 'activity_image', 'case_image')
    list_display_links = ['about_title', ]

    def save_model(self, request, obj, form, change):
        obj.save()
        with open(f"{obj.title_image}", 'rb') as file:
            img = file.read()
            image_base64 = str(base64.b64encode(img), encoding='utf-8')
        obj.title_image_data = image_base64
        with open(f"{obj.activity_image}", 'rb') as file:
            img = file.read()
            image_base64 = str(base64.b64encode(img), encoding='utf-8')
        obj.activity_image_data = image_base64
        with open(f"{obj.case_image}", 'rb') as file:
            img = file.read()
            image_base64 = str(base64.b64encode(img), encoding='utf-8')
        obj.case_image_data = image_base64
        obj.save()

    def delete_model(self, request, obj):
        os.remove(f"{obj.title_image}")
        os.remove(f"{obj.activity_image}")
        os.remove(f"{obj.case_image}")
        obj.delete()

    def delete_queryset(self, request, queryset):
        """ TODO 删除查询集中的模板 """
        for obj in queryset:
            self.delete_model(request, obj)