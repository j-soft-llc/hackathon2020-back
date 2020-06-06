from django.contrib import admin
from initiative.models import Category, Initiative, InitiativePhoto


class InitiativePhotoInline(admin.TabularInline):
    model = InitiativePhoto


class InitiativeAdmin(admin.ModelAdmin):
    inlines = [InitiativePhotoInline]


admin.site.register(Category)
admin.site.register(Initiative, InitiativeAdmin)
