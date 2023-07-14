from django.db import models
from django.utils.translation import gettext as _ # import farsi

# Create your models here.
#name,desc,price,preptime,created,img,food-type

class Food(models.Model):
    TYPES=[
        ('iranifood','غذای ایرانی'),
        ('fastfood','فست فود'),
        ('juices','نوشیدنی')
    ]

    name=models.CharField(_('نام غذا'),max_length=100)
    describtion=models.CharField(_('توضیحات'),max_length=50)
    price=models.PositiveIntegerField(_('قیمت'))
    preptime=models.PositiveSmallIntegerField(_('مدت آماده سازی'),default=2)
    created=models.DateTimeField(_('تاریخ انتشار'),auto_now_add=True)
    image=models.ImageField(_('تصویر'),upload_to='webs/')
    type=models.CharField(_('نوع غذا'),max_length=20,choices=TYPES,default='fastfood')

    def __str__(self):
        return self.name

