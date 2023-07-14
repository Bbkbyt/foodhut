from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class ReserveModel(models.Model):
    name=models.CharField(_('نام و نام خانوادگی'),max_length=150)
    email=models.EmailField(_('ایمیل'),default='abc@gmail.com')
    phone=models.CharField(_('تلفن'),max_length=15)
    guests=models.PositiveIntegerField(_('تعداد مهمان ها'))
    date=models.DateField(_('تاریخ'),auto_now=False,auto_now_add=False,default='2023-01-01')
    time=models.TimeField(_('ساعت'),auto_now=False,auto_now_add=False,default='08:00')
    def __str__(self):
        return self.name