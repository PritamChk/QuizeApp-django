from uuid import uuid4
from django.db.models import (
    Model,
    CharField,
    DateField,
    DateTimeField,
    UUIDField,
    EmailField,
    PositiveSmallIntegerField,
    TextField,
    ForeignKey,
    OneToOneField,
    ManyToManyField
)

STR_MAX_LEN = 300


class Classroom(Model):
    title = CharField(max_length=STR_MAX_LEN)
    subject = CharField(max_length=STR_MAX_LEN)

    def __str__(self) -> str:
        return self.title[:15] + " " + self.subject[:15]

    def count_teachers(self):
        return Teacher.objects.prefetch_related('classroom').filter(classroom__id=self.id).count()

    def count_students(self):
        return self.students.count()


class BaseUser(Model):
    first_name = CharField(max_length=STR_MAX_LEN)
    last_name = CharField(max_length=STR_MAX_LEN)
    email = EmailField(unique=True, db_index=True)
    username = CharField(max_length=60, unique=True, db_index=True)
    password = CharField(max_length=STR_MAX_LEN)
    joined_at = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    
    class Meta:
        abstract = True
    

class Teacher(BaseUser):
    classroom = ManyToManyField(
        "Classroom", related_name="teachers", blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def count_classroom(self):
        count_class = self.classroom.count()
        return count_class


class Student(BaseUser):
    classroom = ManyToManyField(Classroom, related_name="students", blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def count_classroom(self):
        count_class = self.classroom.count()
        return count_class
