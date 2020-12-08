import os
import base64
from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Home)
class HomeModelAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.save()
        with open(f"{obj.activity_image}", 'rb') as file:
            img = file.read()
            image_base64_1 = str(base64.b64encode(img), encoding='utf-8')
        with open(f"{obj.case_image}", 'rb') as file:
            img = file.read()
            image_base64_2 = str(base64.b64encode(img), encoding='utf-8')
        with open(f"{obj.cooperation_image}", 'rb') as file:
            img = file.read()
            image_base64_3 = str(base64.b64encode(img), encoding='utf-8')
        obj.activity_image_data = image_base64_1
        obj.case_image_data = image_base64_2
        obj.cooperation_image_data = image_base64_3
        obj.save()

    def delete_model(self, request, obj):
        os.remove(f"{obj.activity_image}")
        os.remove(f"{obj.case_image}")
        os.remove(f"{obj.cooperation_image}")
        obj.delete()

    def delete_queryset(self, request, queryset):
        """ TODO 删除查询集中的模板 """
        for obj in queryset:
            self.delete_model(request, obj)
