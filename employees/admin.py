from django.contrib import admin
from .models import Department, Employee

# Register your models here.


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "department", "birthdate"]
    list_filter = ["department", "birthdate"]
    search_fields = ["first_name", "last_name"]
