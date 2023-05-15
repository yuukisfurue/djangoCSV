
#djangocsv/board 
(入力は全てプルダウンメニューを利用)
下記１３４目からご参照願います。
https://github.com/yuukisfurue/djangoCSV/blob/master/djangoCSV/settings.py

vps運用で公開運用予定のため、redisを採用しております。

models.py
#下記はCSVのエクスポートのみ実装

```sh
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import MinLengthValidator  #☆

#プルダウンメニュー
class Member(models.Model):
    name = models.CharField(verbose_name="名前",max_length=100)
    prefecture  = models.CharField(verbose_name="出身地",choices=settings.PREFECTURES,max_length=100)
    gender  = models.CharField(verbose_name="性別",choices=settings.GENDERS,max_length=100)
    employmentstatus  = models.CharField(verbose_name="雇用形態",choices=settings.EMPLOYMENTSTATUSS,max_length=100)
    company= models.CharField(verbose_name="業種",choices=settings.COMPANYS,max_length=100)
    jyob  = models.CharField(verbose_name="配属部署",choices=settings.JYOBS,max_length=100) 
    stay= models.CharField(verbose_name="現住所",choices=settings.STAYS,max_length=100)
    affiliation  = models.CharField(verbose_name="所属先",choices=settings.AFFILIATONS,max_length=100)
    postion  = models.CharField(verbose_name="現役職",choices=settings.POSITIONS,max_length=100)
    annual  = models.CharField(verbose_name="今年(万)",choices=settings.ANNUALS,max_length=100) 
    lastyear  = models.CharField(verbose_name="昨年(万)",choices=settings.LASTYEARS,max_length=100)
    
    def __str__(self):
        return '<Member:id=' + str(self.id) + ', ' + \
            self.name + '(' + str(self.name) + ')>'

#CSV
class Plofile(models.Model):            
    name = models.CharField(verbose_name="名前",max_length=100)
    prefecture  = models.CharField(verbose_name="出身地",choices=settings.PREFECTURES,max_length=100)
    gender  = models.CharField(verbose_name="性別",choices=settings.GENDERS,max_length=100)
    employmentstatus  = models.CharField(verbose_name="雇用形態",choices=settings.EMPLOYMENTSTATUSS,max_length=100)
    company= models.CharField(verbose_name="業種",choices=settings.COMPANYS,max_length=100)
    jyob  = models.CharField(verbose_name="配属部署",choices=settings.JYOBS,max_length=100) 
    stay= models.CharField(verbose_name="現住所",choices=settings.STAYS,max_length=100)
    affiliation  = models.CharField(verbose_name="所属先",choices=settings.AFFILIATONS,max_length=100)
    postion  = models.CharField(verbose_name="現役職",choices=settings.POSITIONS,max_length=100)
    annual  = models.CharField(verbose_name="今年(万)",choices=settings.ANNUALS,max_length=100) 
    lastyear  = models.CharField(verbose_name="昨年(万)",choices=settings.LASTYEARS,max_length=100)
```


#djangocsv/bguest
#下記はCSVのインポートとエクスポートの両機能実装
admins.py

```sh

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ImportExportMixin
from import_export.formats import base_formats
from guest.models import Guest


# Register your models here.
class GuestResource(resources.ModelResource):
    class Meta:
        model = Guest
    fields = ['id','name','prefecture','gender','employmentstatus','company','jyob','stay','affiliation','postion','annual','lastyear']
    import_id_fields = ['id']

class GuestAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'prefecture',
        'gender',
        'employmentstatus',
        'company',
        'jyob',
        'stay',
        'affiliation',                        
        'postion',
        'annual',
        'lastyear'
      )

    resource_class = GuestResource
    formats = [base_formats.CSV]

admin.site.register(Guest, GuestAdmin)

```
