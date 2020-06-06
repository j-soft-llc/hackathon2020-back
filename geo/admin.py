from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Geo

admin.site.register(Geo, MPTTModelAdmin)
