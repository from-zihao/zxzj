from django.db import models
from datetime import datetime
# Create your models here.


def create_time():
    return datetime.now()


class Coordinate(models.Model):

    lon = models.CharField(verbose_name="经度", max_length=255, blank=True, null=True)
    lat = models.CharField(verbose_name="纬度", max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(verbose_name="创建时间", blank=True, null=True, default=create_time)

    class Meta:
        verbose_name = '公司坐标'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f""


class UserSubmitInfo(models.Model):
    username = models.CharField(verbose_name="客户名", max_length=255, blank=True, null=True)
    contact_info = models.CharField(verbose_name="联系方式", max_length=255, blank=True, null=True)
    contact_content = models.TextField(verbose_name="联系内容", blank=True, null=True)
    create_time = models.DateTimeField(verbose_name="创建时间", blank=True, null=True, default=create_time)

    class Meta:
        verbose_name = '客户提交信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f""
