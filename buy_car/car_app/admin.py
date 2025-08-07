from django.contrib import admin
from .models import Car

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','car_model']