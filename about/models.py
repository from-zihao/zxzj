from django.db import models
from datetime import datetime
# Create your models here.


def create_time():
    return datetime.now()


class About(models.Model):

    about_title = models.CharField(verbose_name="案例标题", max_length=255, blank=True, null=True, default="房产快销赋能平台")
    title_image = models.ImageField(verbose_name="头图片", upload_to='about/data/', null=None, default="")
    activity_image = models.ImageField(verbose_name="活动展示图片", upload_to='about/data/', null=None, default="")
    case_image = models.ImageField(verbose_name="案例落地图片", upload_to='about/data/', null=None, default="")
    title_image_data = models.TextField(verbose_name="头图片数据", blank=True, null=True)
    activity_image_data = models.TextField(verbose_name="活动展示图片数据", blank=True, null=True)
    case_image_data = models.TextField(verbose_name="案例落地图片数据", blank=True, null=True)
    create_time = models.DateTimeField(verbose_name="创建时间", blank=True, null=True, default=create_time)

    class Meta:
        verbose_name = '关于'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.about_title}"
