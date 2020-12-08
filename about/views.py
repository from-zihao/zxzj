from django.shortcuts import render
from .models import *
from zxzj.views import ViewBase
import os
import json
import base64
# Create your views here.


class AboutView(ViewBase):
    def get(self, request, *args, **kwargs):
        result = {
            "code": 0,
            "data": []
        }
        try:
            about_obj = About.objects.first()
            result["data"].append(f"data:image/png;base64,{about_obj.title_image_data}")
            result["data"].append(f"data:image/png;base64,{about_obj.activity_image_data}")
            result["data"].append(f"data:image/png;base64,{about_obj.case_image_data}")
        except Exception as e:
            print(e)
            result["code"] = 1
        return self.json_response(data=result)
