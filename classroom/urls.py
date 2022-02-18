from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
# from rest_framework_nested.routers import DefaultRouter,NestedDefaultRouter,SimpleRouter
import pprint

teacher_router = DefaultRouter()
teacher_router.register('teacher',TeacherViewList,basename='teacher')


# qset_router = DefaultRouter()
teacher_router.register('quiz-set',QuizSetViewList,basename='quizset')

pprint.pprint(teacher_router.urls)
# urlpatterns = [
#     path('classrooms/',ClassRoomListView.as_view()),
#     # path('teacher/',TeacherViewList.as_view()),
#     path('qus-set/',QuestionSetViewList.as_view()),
#     path('quizset/',QuizSetViewList.as_view()),
#     path('studs/',show_students),
# ]
# urlpatterns  =  teacher_router.urls \
#                 + qset_router.urls

urlpatterns  =  [
    path("",include(teacher_router.urls)),
    # path("",include(qset_router.urls)),
]
         
