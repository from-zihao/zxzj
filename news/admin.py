import os
import shutil
import base64
from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(News)
class NewsModelAdmin(admin.ModelAdmin):
    search_fields = ('news_title',)
    list_display = ('id', 'news_title', 'news_content', 'create_time')
    list_display_links = ['news_title', ]

    def save_model(self, request, obj, form, change):
        obj.save()
        with open(f"{obj.news_image}", 'rb') as file:
            img = file.read()
            image_base64 = str(base64.b64encode(img), encoding='utf-8')
        obj.image_data = image_base64
        obj.save()

    def delete_model(self, request, obj):
        os.remove(f"{obj.news_file}")
        os.remove(f"{obj.news_image}")
        obj.delete()

    def delete_queryset(self, request, queryset):
        """ TODO 删除查询集中的模板 """
        for obj in queryset:
            self.delete_model(request, obj)


