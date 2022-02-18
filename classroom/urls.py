from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
# from rest_framework_nested.routers import DefaultRouter,NestedDefaultRouter,SimpleRouter
import pprint

root_router = DefaultRouter()
root_router.register('teacher',TeacherViewSet,basename='teacher')


# qset_router = DefaultRouter()
root_router.register('quiz-set',QuizSetView,basename='quizset')
root_router.register('qustions',QuestionSetView,basename='qus')
pprint.pprint(root_router.urls)
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
    path("",include(root_router.urls)),
    # path("",include(qset_router.urls)),
]
         
