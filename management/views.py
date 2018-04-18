import json

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from management.models import Teacher, Student, Lession, Score

# Create your views here.

# 全局变量
user = ""
xuehao = ""
pwd = ""


# 到登录界面
def index(request):
    return render(request, 'login.html')


# noinspection PyUnresolvedReferences
def login(request):
    global xuehao, user, pwd
    if request.method == 'POST':
        xuehao = request.POST.get('xuehao')
        pwd = request.POST.get('pwd')
        user = request.POST.get('user')
    # 单选框值为１代表学生
    if user == '1':
        try:
            # 获取对应学号的学生对象
            student = Student.objects.get(xuehao=xuehao)
        except Student.DoesNotExist:
            # 　不存在则重定向
            return HttpResponseRedirect('/')
        # 密码等于学号,则获取课程，返回student页面
        if pwd == xuehao:
            score = Score.objects.filter(student=student)
            all_lession = Lession.objects.all()
            return render(request, 'student.html',
                          dict(student=student, score=score, all_lession=all_lession, ))
        else:
            return HttpResponseRedirect('/')
    # 单选框值为２代表老师
    elif user == '2':
        try:
            # 获取老师对象
            teacher = Teacher.objects.get(teacher_id=xuehao)
        except Teacher.DoesNotExist:
            return HttpResponseRedirect('/')
        # 密码==学号
        if pwd == xuehao:
            all_lession = Lession.objects.filter(lession_teacher=teacher)
            print(all_lession)
            # lession_score列表中包含了成绩model
            lession_score = []
            for lession in all_lession:
                lession.score = Score.objects.filter(lession=lession)
                lession_score.append(lession)
            print(lession_score)
            return render(request, 'teacher.html',
                          {'teacher': teacher, 'all_lession': all_lession, 'lession_score': lession_score})
        else:
            return HttpResponseRedirect('/')
    # 管理员
    else:
        return HttpResponseRedirect("/admin/")


# noinspection PyUnresolvedReferences
@csrf_exempt
def selected_lession(request):
    lession_name = request.POST.get('lession_name')
    student_name = request.POST.get('student_name')
    lession_list = json.loads(lession_name)
    student = Student.objects.get(name=student_name)
    exists_lession = ""
    insert_lession = ""
    # 判断是否为ajax
    if request.is_ajax:
        # 遍历选中的课程
        for ls in lession_list:
            lession = Lession.objects.get(lession_name=ls)
            s = Score.objects.filter(student=student, lession=lession)
            # 判断课程是否选过
            if s.exists():
                exists_lession += "%s\n" % ls
                print(exists_lession)
                continue
            else:
                insert_lession += "%s\n" % ls
                # 创建成绩对象
                score = Score()
                score.student = student
                print(insert_lession)
                score.lession = Lession.objects.get(lession_name=ls)
                score.score = '未出'
                score.save()
    return JsonResponse({'exists_lession': exists_lession, 'insert_lession': insert_lession})


# noinspection PyUnresolvedReferences
@csrf_exempt
def remove_lession(request):
    if request.is_ajax:
        # 获取学生对象
        student = Student.objects.get(name=request.POST.get('student'))
        # 获取课程对象
        lession = Lession.objects.get(lession_name=request.POST.get('lession'))
        # 删除成绩
        Score.objects.filter(student=student, lession=lession).delete()
        print(student, lession)
        print(type(student))
        return JsonResponse({})


# noinspection PyUnresolvedReferences
@csrf_exempt
def modify_score(request):
    if request.is_ajax:
        score = request.POST.get('score')
        student = Student.objects.get(name=request.POST.get('student'))
        lession = Lession.objects.get(lession_name=request.POST.get('lession'))
        # 更新成绩
        Score.objects.filter(student=student, lession=lession).update(score=score)
        print(score, student, lession)
    return JsonResponse({})
