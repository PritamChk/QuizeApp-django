from ..models import Teacher
from rest_framework.serializers import ModelSerializer as ms,SerializerMethodField as method_field

class TeacherSerializer(ms):
    no_of_classrooms =  method_field(method_name='get_assosiated_classroom_no')
    class Meta:
        model = Teacher
        fields = (
                "id",
                "first_name",
                "last_name",
                "email",
                "username",
                "password",
                "classroom",
                "no_of_classrooms",
            )
        read_only_fields = [
                "id",
                "no_of_classrooms",
            ]
        # write_only_fields =["password"]
        extra_kwargs = {
                "password":{
                    "write_only":True
                    }
                }
        # depth = 1
        
    def get_assosiated_classroom_no(self,obj:Teacher)->int:
        return obj.classroom.count()