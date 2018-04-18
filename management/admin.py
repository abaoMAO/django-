from django.contrib import admin
from management.models import Student, Lession, Teacher,Score


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'xuehao', 'sex', 'subject', 'native_place')


@admin.register(Lession)
class LessionAdmin(admin.ModelAdmin):
    list_display = ('lession_name', 'lession_teacher', 'lession_credit', 'lession_time')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id','teacher_name', 'teacher_sex', )
@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('student', 'lession', 'score')