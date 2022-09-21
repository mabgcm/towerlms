from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required,user_passes_test
from . import models
from django.db.models import Sum


def home(request):
    return render(request, 'towerweb/home.html')

def user_login(request):
    login(request)
    return render(request, 'towerweb/adminlogin.html')

# def is_admin(user):
#     return user.groups.filter(name='admin').exists()

# @login_required(login_url='dashboard')
# @user_passes_test(is_admin)
def admindashboard(request):
    coursescount=models.Course.objects.all().count()
    clasescount=models.Clss.objects.all().count()
    teachercount=models.Teacher.objects.all().filter(is_active=True).count()
    # pendingteachercount=models.Teacher.objects.all().filter(status=False).count()

    studentcount=models.Student.objects.all().filter(is_active=True).count()
    # pendingstudentcount=models.StudentExtra.objects.all().filter(status=False).count()

    teachersalary=models.Teacher.objects.filter(is_active=True).aggregate(Sum('salary'))
    # pendingteachersalary=models.TeacherExtra.objects.filter(status=False).aggregate(Sum('salary'))

    studentfee=models.Student.objects.filter(is_active=True).aggregate(Sum('fee'))
    # pendingstudentfee=models.StudentExtra.objects.filter(status=False).aggregate(Sum('fee'))

    # notice=models.Notice.objects.all()

    #aggregate function return dictionary so fetch data from dictionay
    mydict={
        'coursescount':coursescount,
        'clasescount':clasescount,
        'teachercount':teachercount,
        # 'pendingteachercount':pendingteachercount,

        'studentcount':studentcount,
        # 'pendingstudentcount':pendingstudentcount,

        'teachersalary':teachersalary['salary__sum'],
        # 'pendingteachersalary':pendingteachersalary['salary__sum'],

        'studentfee':studentfee['fee__sum'],
        # 'pendingstudentfee':pendingstudentfee['fee__sum'],

        # 'notice':notice

    }

    return render(request,'towerweb/admindashboard.html',context=mydict)

def user_logout(request):
    logout(request)
    return redirect('home')

def user_login(request):
    form=AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('admindashboard')
    return render(request, 'towerweb/adminlogin.html', {'form':form})    