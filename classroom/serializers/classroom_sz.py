from rest_framework.serializers import ModelSerializer
from ..models import *

class ClassRoomSerializer(ModelSerializer):
    class Meta:
        model = Classroom
        fields = ('id', 'title', 'subject')