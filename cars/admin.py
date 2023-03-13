from django.contrib import admin
from cars.models import Cars
# Register your models here.




class CarAdmin(admin.ModelAdmin):
    #fields = ['year','brand']
    fieldsets=[
        ('TIME INFORMATION', {'fields':['year']}),
        ('CAR INFORMATION', {'fields':['brand']}),
    ]

admin.site.register(Cars,CarAdmin)
