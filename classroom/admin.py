from pyexpat import model
from django.contrib import admin

from .models import *

admin.site.site_header= "Quizapp Admin"
admin.site.site_title= "Admin Section"

# -------------  inline classes -------------
# class StudentInline(admin.TabularInline):
#     model = Student
#     raw_id_fields = ("classroom",)
#     min_num = 0
#     max_num = 10
#     extra = 0

# -------------  inline classes -------------

# ---------------- CLASSROOM ADMIN --------------
@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    # inlines = [StudentInline]
    list_display = [
        "title",
        "subject",
        "count_teachers",
        "count_students",
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
    search_fields = [
        "first_name__icontains",
        "first_name__istartswith",
        "first_name__iendswith",
        "last_name__icontains",
        "last_name__istartswith",
        "last_name__iendswith",
    ]
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
    search_fields = [
        "first_name__icontains",
        "first_name__istartswith",
        "first_name__iendsswith",
        "last_name__icontains",
        "last_name__istartswith",
        "last_name__iendswith",
    ]
# --------------- STUDENT ADMIN -----------------    