from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age', 'email', 'created_at') 
    search_fields = ('name', 'surname', 'email') 
    list_filter = ('age', 'created_at')
    prepopulated_fields = {'slug': ('name', 'surname')} 