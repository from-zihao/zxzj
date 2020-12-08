import json
import uuid
import decimal
import datetime

from django.shortcuts import HttpResponse

from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, bytes):
            return obj.decode('gbk', errors='ignore')
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstance(obj, uuid.UUID):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page_number'
    max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):

        page_size = self.get_page_size(request)
        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = request.query_params.get(self.page_query_param, 1)
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages

        self.page = paginator.get_page(page_number)
        if paginator.num_pages > 1 and self.template is not None:
            self.display_page_controls = True

        self.request = request
        return list(self.page)


class ViewBase(APIView):

    def json_response(self, data=None, content_type="application/json;charset=UTF-8"):
        response = HttpResponse(content=json.dumps(data, indent=4, cls=MyEncoder), content_type=content_type)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "*"
        response["Access-Control-Allow-Methods"] = "DELETE,GET,OPTIONS,PATCH,POST,PUT"
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "*"
        response["Access-Control-Allow-Methods"] = "DELETE,GET,OPTIONS,PATCH,POST,PUT"
        return response

    def post(self, request, *args, **kwargs):
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "*"
        response["Access-Control-Allow-Methods"] = "DELETE,GET,OPTIONS,PATCH,POST,PUT"
        return response

    def pagination(self, queryset, serializer):
        paginator = Pagination()
        queryset_page = paginator.paginate_queryset(queryset, self.request, view=self)
        ser = serializer(instance=queryset_page, many=True)
        return {"rows": ser.data, "total": len(queryset)}
