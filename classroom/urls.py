from django.urls import path
from .views import *
from rest_framework_nested.routers import DefaultRouter,NestedDefaultRouter

teacher_router = DefaultRouter()
teacher_router.register('teacher',TeacherViewList,basename='teacher')


urlpatterns = [
    path('classrooms/',ClassRoomListView.as_view()),
    # path('teacher/',TeacherViewList.as_view()),
    path('qus-set/',QuestionSetViewList.as_view()),
    path('quizset/',QuizSetSetViewList.as_view()),
    path('studs/',show_students),
]+ teacher_router.urls

