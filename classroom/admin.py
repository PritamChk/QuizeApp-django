from django.contrib import admin

from .models import *


# ---------------- CLASSROOM ADMIN --------------
@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "subject",
        "count_teachers",
        "count_students"            
    ]
    search_fields = ["title__icontains",
                     "title__istartswith",
                     "subject__icontains",
                     "subject__istartswith"]
    ordering = ["-title","subject"]
    list_editable = ["subject"]
    
# ---------------- CLASSROOM ADMIN --------------

# --------------- TEACHER ADMIN -----------------    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display= [
        "full_name",
        "first_name",
        "username",
        "count_classroom"
    ]
    readonly_fields = ["last_updated","joined_at"]
    ordering = ["first_name","last_name"]
    autocomplete_fields = ["classroom"]
    list_per_page = 10
    
    @admin.display()
    def full_name(self,obj):
        return f"{obj.first_name} {obj.last_name}"
    
# --------------- TEACHER ADMIN -----------------

# --------------- STUDENT ADMIN -----------------

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    autocomplete_fields = ["classroom"]
    list_display = [
            "full_name",
            "username",
            "count_classroom"
        ]
    ordering = ["first_name","last_name"]
    readonly_fields = ["last_updated","joined_at"]
# --------------- STUDENT ADMIN -----------------    