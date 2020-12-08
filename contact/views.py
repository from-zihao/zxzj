from django.shortcuts import render
from zxzj.views import ViewBase
from .models import *
import os
import json
import base64
# Create your views here.


class CoordinateView(ViewBase):
    def get(self, request, *args, **kwargs):
        result = {
            "code": 0,
            "data": []
        }
        try:
            obj = Coordinate.objects.first()
            result["data"].append(f"{obj.lon}")
            result["data"].append(f"{obj.lat}")
        except Exception as e:
            print(e)
            result["code"] = 1
        return self.json_response(data=result)


class UserSubmitInfoView(ViewBase):
    def post(self, request, *args, **kwargs):
        data = json.loads(request._request.body.decode())
        username = data.get("username")
        contact_info = data.get("contact_info")
        contact_content = data.get("contact_content")
        UserSubmitInfo.objects.create(
            username=username,
            contact_info=contact_info,
            contact_content=contact_content
        )
        return self.json_response(data={"code": 0, "data": ""})
