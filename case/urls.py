from django.conf.urls import url

from .views import *


def case_urls():
    urlpatterns = [
        url(r'^api/zxzj/v1/case/info$', CaseView.as_view()),
    ]
    return urlpatterns
