# from django.contrib import admin

# # Register your models here.

# from . models import Model1 ,Model2
# admin.site.register(Model2)



# class AdminModel(admin.ModelAdmin):
#     display = ('binary_data',)

# admin.site.register(Model1, AdminModel)



from django.contrib import admin
from .models import Model1, Model2, Teacher, Student

# class Model1Admin(admin.ModelAdmin):
#     list_display = ('pk1', 'big_number', 'binary_data')  # Add 'binary_data' to list_display

admin.site.register(Model1)
admin.site.register(Model2)
admin.site.register(Teacher)


class Test(admin.ModelAdmin):
    list_display = ['name', 'roll']

admin.site.register(Student, Test)

from .models import  Course
admin.site.register(Course)

from .models import Model3

class SlugModel(admin.ModelAdmin):
    prepopulated_fields = {"slug":('description',)}
    display = ['slug','description']

admin.site.register(Model3, SlugModel)
