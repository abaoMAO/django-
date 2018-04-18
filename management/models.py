from django.db import models


class Teacher(models.Model):
    # 教工号
    teacher_id = models.CharField(u'教工号', max_length=9, null=True)
    # 姓名
    teacher_name = models.CharField(u'老师姓名', max_length=10)
    # 性别
    teacher_sex = models.CharField(u'性别', max_length=2)

    def __str__(self):
        return self.teacher_name


class Lession(models.Model):
    # 课程名称
    lession_name = models.CharField(u'课程名称', max_length=15)
    # 课程老师
    lession_teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, null=True)
    # 课时
    lession_credit = models.IntegerField(u'学分')
    # 学分
    lession_time = models.IntegerField(u'学时')

    def __str__(self):
        return self.lession_name


# Create your models here.
class Student(models.Model):
    # 学号
    xuehao = models.CharField(u'学号', max_length=9)
    # 姓名
    name = models.CharField(u'学生姓名', max_length=20)
    # 专业
    subject = models.CharField(u'专业', max_length=20)
    # 性别
    sex = models.CharField(u'性别', max_length=5)
    # 所在地
    native_place = models.CharField(u'所在地', max_length=15)

    def __str__(self):
        return self.name


class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    lession = models.ForeignKey(Lession, on_delete=models.DO_NOTHING)
    score = models.CharField(max_length=3)

    def __str__(self):
        return '%s' % self.lession.lession_name
