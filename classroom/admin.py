from django.contrib import admin
from django.db.models import Sum, F, Count
from .models import *

admin.site.site_header = "Quizapp Admin"
admin.site.site_title = "Admin Section"


# -------------  inline classes -------------
# ---------- QuizEvent Inline ---------
class QuizSetInline(admin.TabularInline):
    model = QuizSet
    extra = 0
    min_num = 0
    max_num = 20

# class QuizEventInline(admin.TabularInline):
#     model = QuizEvent
#     extra=0
#     min_num = 0
#     max_num = 20


class OptionInline(admin.TabularInline):
    model = Option
    min_num = 2
    extra = 0
    max_num = 100


class QustionsInline(admin.TabularInline):
    model = Question
    extra = 0
    min_num = 0
    max_num = 100

# ---------------- CLASSROOM ADMIN --------------


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    # inlines = [StudentInline]
    list_display = [
        "title",
        "subject",
        "count_teachers",
        "count_students",
        "count_events",
    ]
    list_filter = ["subject"]
    search_fields = ["title__icontains",
                     "title__istartswith",
                     "subject__icontains",
                     "subject__istartswith"]
    ordering = ["-title", "subject"]
    list_editable = ["subject"]

    @admin.display()
    def count_events(self, class_room):
        return QuizEvent.objects.select_related("host_classroom").\
            filter(host_classroom=class_room).count()

# ---------------- CLASSROOM ADMIN --------------

# --------------- TEACHER ADMIN -----------------


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    date_hierarchy = 'joined_at'
    list_display = [
        "full_name",
        # "first_name",
        # "last_name",
        "username",
        "count_classroom"
    ]
    list_filter = ('joined_at', 'last_updated')
    prepopulated_fields = {
        "username": ["first_name", "last_name"]
    }
    raw_id_fields = ('classroom',)
    # list_editable = ["first_name","last_name"]
    readonly_fields = ["id","last_updated", "joined_at"]
    search_fields = [
        "first_name__icontains",
        "first_name__istartswith",
        "first_name__iendswith",
        "last_name__icontains",
        "last_name__istartswith",
        "last_name__iendswith",
    ]
    ordering = ["first_name", "last_name"]
    autocomplete_fields = ["classroom"]
    list_per_page = 10

    @admin.display()
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

# --------------- TEACHER ADMIN -----------------

# --------------- STUDENT ADMIN -----------------


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    autocomplete_fields = ["classroom"]
    date_hierarchy = 'joined_at'
    list_display = [
        "full_name",
        "username",
        "count_classroom"
    ]
    list_filter = ('joined_at', 'last_updated')
    ordering = ["first_name", "last_name"]
    readonly_fields = ["last_updated", "joined_at"]
    prepopulated_fields = {
        "username": ["first_name", "last_name"]
    }
    raw_id_fields = ('classroom',)
    search_fields = [
        "first_name__icontains",
        "first_name__istartswith",
        "first_name__iendsswith",
        "last_name__icontains",
        "last_name__istartswith",
        "last_name__iendswith",
    ]

# --------------- STUDENT ADMIN -----------------


# --------------- Option ADMIN -----------------
@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = [
        "option_value",
        "id",
        "is_correct",
        "qustion",
    ]
    list_editable = ["is_correct"]
    list_filter = (
        'is_correct',
        "qustion",
        # "get_qus_id"
    )

# --------------- Question ADMIN -----------------


@admin.register(Question)
class QustionAdmin(admin.ModelAdmin):
    list_display = [
        "question_value",
        "id",
        "point",
        "quizset"
    ]
    list_editable = ["point"]
    list_filter = ('updated_at', 'quizset')
    inlines = [OptionInline]
    autocomplete_fields = [
        "quizset"
    ]
# --------------- QuizSet ADMIN -----------------


@admin.register(QuizSet)
class QuizsetAdmin(admin.ModelAdmin):
    autocomplete_fields = [
        "author_teacher",
        "quiz_event",
    ]

    list_display = (
        "heading",
        "id",
        "difficulty_level",
        "get_total_marks"
    )
    list_editable = ("difficulty_level",)
    list_filter = ('created_at', 'update_at', 'author_teacher', "difficulty_level", 'quiz_event')
    inlines = [
        QustionsInline,
        # OptionInline,
    ]
    search_fields = [
        "heading__icontains",
        "heading__istartswith",
        "heading__iendswith",
    ]

    @admin.display()
    def get_total_marks(self, qset):
        return Question.objects.filter(quizset__id=qset.id).\
            aggregate(Sum('point'))['point__sum']


@admin.register(QuizEvent)
class QuizEventAdmin(admin.ModelAdmin):
    search_fields = [
        "title__icontains",
        "title__istartswith",
        "title__iendswith",
        # "host_classroom_name",
    ]
    autocomplete_fields = [
        "host_classroom",
    ]
    list_display = (
        "title",
        "start_date",
        "start_time",
        "exam_duration"
    )
    # list_editable = (
    #     # "host_classroom",
    #     "host_classroom_name",
    # )
    list_filter = ('start_date', 'host_classroom')
    # inlines = [QuizSetInline]

    # @admin.display()
    # def host_classroom_name(self,obj:QuizEvent):
    #     return Classroom.objects.prefetch_related('hosted_quizes') \
    #             .filter(hosted_quizes__id = obj.id).heading

class AnswerInline(admin.TabularInline):
    model = Answer
    extra=0
    min_num=0
    max_num = 100


@admin.register(AnswerSet)
class AnswerSetAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        # 'quizevent', 
        'created_at', 
        'updated_at'
    )
    # select_related_fields = ["quizevent"]
    list_filter = ('quizevent', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    inlines = [AnswerInline]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        "qzid",
        "qid",
        "optid",
        'created_at',
        'updated_at',
        'student',
        'answer_set',
    )
    list_editable = (
        "qzid",
        "qid",
        "optid",          
    )
    list_filter = ('created_at', 'updated_at', 'student', 'answer_set')
    date_hierarchy = 'created_at'