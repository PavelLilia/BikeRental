from django.contrib import admin
from rental.models import Bike, BikeOptions, BikeCategory, News


# Register your models here.

class BikeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


class BikeCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(Bike, BikeAdmin)
admin.site.register(BikeOptions)
admin.site.register(BikeCategory, BikeCategoryAdmin)
admin.site.register(News, NewsAdmin)
