from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import HttpResponse
from .models import *
from zxzj.views import ViewBase
import os
import json
import base64
# Create your views here.


class NewsView(ViewBase):
    def get(self, request, *args, **kwargs):
        result = {
            'data': [],
        }
        for obj in News.objects.all():
            temp = {
                "id": obj.id,
                "title": obj.news_title,
                "create_time": obj.create_time,
                "content": obj.news_content,
                "image_data": obj.image_data
            }
            result['data'].append(temp)
        result['data'] = sorted(result['data'], key=lambda e: e.__getitem__('create_time'), reverse=True)
        return self.json_response(data=result)


class NewsDocView(ViewBase):
    def get(self, request, *args, **kwargs):
        doc_id = request.query_params.dict().get("doc_id")
        news_obj = News.objects.filter(id=doc_id).first()
        if os.path.exists(f"{news_obj.news_file}"):
            with open(f"{news_obj.news_file}", 'rb') as file:
                doc_data = file.read()
                doc_base64 = str(base64.b64encode(doc_data), encoding='utf-8')
                return self.json_response(data={"code": 0, "msg": doc_base64})
        else:
            return self.json_response(data={"code": 1, "msg": ""})
