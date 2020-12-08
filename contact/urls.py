from django.conf.urls import url

from .views import *


def contact_urls():
    urlpatterns = [
        url(r'^api/zxzj/v1/coordinate/info$', CoordinateView.as_view()),
        url(r'^api/zxzj/v1/submit/info$', UserSubmitInfoView.as_view()),
    ]
    return urlpatterns
