from django.urls import path
from .views import *

urlpatterns = [
    path('classrooms/',ClassRoomListView.as_view()),
    path('teacher/',TeacherViewList.as_view())
]
