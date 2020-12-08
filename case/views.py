from django.shortcuts import render
from .models import *
from zxzj.views import ViewBase
import os
import json
import base64
# Create your views here.


class CaseView(ViewBase):
    def get(self, request, *args, **kwargs):
        result = {
            "code": 0,
            "data": []
        }
        for obj in Case.objects.all():
            temp = {
                "id": obj.id,
                "title": obj.case_title,
                "create_time": obj.create_time,
                "content": obj.case_content,
                "image_data": f"data:image/png;base64,{obj.image_data}"
            }
            result['data'].append(temp)
        return self.json_response(data=result)
