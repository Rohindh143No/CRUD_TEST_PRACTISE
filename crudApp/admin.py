from django.contrib import admin
from crudApp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    details=['Sno','Sname','Sage','Sadrs']
admin.site.register(Student,StudentAdmin)