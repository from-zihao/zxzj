from django.db import models
from datetime import datetime
# Create your models here.


def create_time():
    return datetime.now()


class Case(models.Model):

    case_title = models.CharField(verbose_name="案例标题", max_length=255, blank=True, null=True)
    case_content = models.TextField(verbose_name="案例内容", blank=True, null=True)
    case_image = models.ImageField(verbose_name="案例图片", upload_to='case/data/', null=None, default="")
    image_data = models.TextField(verbose_name="图片数据", blank=True, null=True)
    create_time = models.DateTimeField(verbose_name="创建时间", blank=True, null=True, default=create_time)

    class Meta:
        verbose_name = '案例'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.case_title}"
