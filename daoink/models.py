from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    用户
    """
    tel = models.CharField(max_length=20, null=False, blank=False, unique=True)


class PrintOrder(models.Model):
    """
    打印订单
    """
    user = models.ForeignKey('User', on_delete=models.CASCADE)                                  # 关联的用户
    # 上传的文件信息
    file_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='文件名')
    storage_uri = models.CharField(max_length=255, null=False, verbose_name='文件存储URI')
    # 打印机设置
    queue_way = models.IntegerField(default=1)                                                  # 打印排队方式选择
    print_date = models.DateTimeField(null=True)                                                # 预约的打印时间点
    printer_place = models.CharField(max_length=255, null=False)                                # 打印机地点选择
    # 纸张设置
    print_style = models.CharField(max_length=100, null=False)                                  # 单双面选择
    paper_pages = models.IntegerField(null=True)                                                # 文件页数
    paper_copies = models.IntegerField(default=1)                                               # 文件份数
    paper_direction = models.CharField(max_length=100, null=False)                              # 横向,纵向
    paper_color = models.CharField(max_length=100, null=False)                                  # 是否彩印,默认黑白
    paper_size = models.CharField(max_length=100, null=False)                                   # 纸张尺寸
    # 订单信息
    create_date = models.DateTimeField(auto_now=True, null=False)                               # 订单创建的时间
    trade_money = models.FloatField(max_length=255)                                             # 订单价格
    trade_number = models.CharField(max_length=255)                                             # 支付的订单号
    # 订单状态，0:已提交文件但未支付, 1:已经支付但未打印, 2:已经加入下载队列, 3:已打印
    trade_status = models.IntegerField(default=0)