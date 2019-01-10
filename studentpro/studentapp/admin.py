from django.contrib import admin
from .models import Student

class AdminStudent(admin.ModelAdmin):
    list_display = ['sid','sname','email','fee']
admin.site.register(Student,AdminStudent)

