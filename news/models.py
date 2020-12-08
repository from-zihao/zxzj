from datetime import datetime
from django.db import models

# Create your models here.


def create_time():
    return datetime.now()


class News(models.Model):

    news_title = models.CharField(verbose_name="资讯标题", max_length=255)
    news_content = models.CharField(verbose_name="资讯内容", max_length=255)
    news_image = models.ImageField(verbose_name="资讯图片", upload_to='news/data/', null=None, default="")
    news_file = models.FileField(verbose_name="资讯文件", upload_to='news/data/', null=None, default="")
    image_data = models.TextField(verbose_name="图片数据", blank=True, null=True)
    create_time = models.DateTimeField(verbose_name="创建时间", blank=True, null=True, default=create_time())

    class Meta:
        verbose_name = '资讯'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.news_title}"
