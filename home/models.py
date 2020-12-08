from django.db import models
from datetime import datetime
# Create your models here.


def create_time():
    return datetime.now()


class Home(models.Model):
    activity_image = models.ImageField(verbose_name="活动展示图片", upload_to='home/data/', null=None, default="")
    case_image = models.ImageField(verbose_name="案例落地图片", upload_to='home/data/', null=None, default="")
    cooperation_image = models.ImageField(verbose_name="合作流程图片", upload_to='home/data/', null=None, default="")
    activity_image_data = models.TextField(verbose_name="活动展示图片数据", blank=True, null=True)
    case_image_data = models.TextField(verbose_name="案例落地图片数据", blank=True, null=True)
    cooperation_image_data = models.TextField(verbose_name="合作流程图片数据", blank=True, null=True)
    create_time = models.DateTimeField(verbose_name="创建时间", blank=True, null=True, default=create_time)

    class Meta:
        verbose_name = '首页'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.activity_image}"
