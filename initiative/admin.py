from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from initiative.models import Category, Geo

admin.site.register(Category)
admin.site.register(Geo, MPTTModelAdmin)

