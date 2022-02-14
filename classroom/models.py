from uuid import uuid4
from django.core.validators import MaxValueValidator
from django.db.models import (
    Model,
    CharField,
    DateField,
    DateTimeField,
    UUIDField,
    EmailField,
    PositiveSmallIntegerField,
    TextField,
    BooleanField,
    ForeignKey,
    OneToOneField,
    ManyToManyField,
    CASCADE,
    SET_NULL,
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
        ordering = ["first_name", "last_name", "-joined_at"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Teacher(BaseUser):
    classroom = ManyToManyField(
        "Classroom", related_name="teachers", blank=True)

    def count_classroom(self):
        count_class = self.classroom.count()
        return count_class


class Student(BaseUser):
    classroom = ManyToManyField(Classroom, related_name="students", blank=True)

    def count_classroom(self):
        count_class = self.classroom.count()
        return count_class


class Question(Model):
    qustion_value = TextField()
    point = PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(
        15, "Hya hya, 1ta mcq tei 100 marks diye dao,Ajob Public")])
    updated_at = DateTimeField(auto_now=True)
    quizset = ForeignKey("QuizSet", on_delete=CASCADE, related_name="qustions")
    #options = ...

    class Meta:
        ordering = ["point"]

    def __str__(self) -> str:
        return self.question_value.lower()[:20]


class Options(Model):
    option_value = TextField()
    is_correct = BooleanField(default=False, editable=True)
    qustion = ForeignKey(Question, on_delete=CASCADE, related_name="options")

    def __str__(self) -> str:
        return self.option_value.lower()[:15]


class QuizSet(Model):
    LEVEL_EASY = 0
    LEVEL_MEDIUM = 1
    LEVEL_HARD = 2
    LEVEL = [
        (LEVEL_EASY, "Easy"),
        (LEVEL_MEDIUM, "Medium"),
        (LEVEL_HARD, "Hard"),
    ]

    heading = CharField(max_length=STR_MAX_LEN,
                        default=uuid4, db_index=True, blank=True)
    created_at = DateTimeField(auto_now_add=True, db_index=True)
    update_at = DateTimeField(auto_now=True, editable=False)
    dificulty_level = CharField(
        max_length=2, choices=LEVEL, default=LEVEL_EASY)
    author_teacher = ForeignKey(
        Teacher, on_delete=SET_NULL, related_name='quizsets')
    #questions = ...

    class Meta:
        ordering = ["-created_at", "dificulty_level"]

    def __str__(self) -> str:
        return f"{self.id} - {self.heading[:25]}"

    def get_teacher_count_for_each_quizset(self):
        return self.author_teacher.count()
