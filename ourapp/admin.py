from django.contrib import admin
from .models import School, Faculty, Certificate_type, Department, Grade, Student
# Register your models here.

admin.site.register(School)
admin.site.register(Faculty)
admin.site.register(Certificate_type)
admin.site.register(Department)
admin.site.register(Grade)
admin.site.register(Student)