from django.db import models
# from django.utils import timezone

gender=[('F','female'),('M','male')]

class Course(models.Model):
    STARTERS = 'ST'
    MOVERS = 'MV'
    FLYERS = 'FL'
    KET = 'KT'
    PET = 'PT'
    FCE = 'FC'
    COURSE_CHOICES = [
        (STARTERS, 'Starters'),
        (MOVERS, 'Movers'),
        (FLYERS, 'Flyers'),
        (KET, 'KET'),
        (PET, 'PET'),
        (FCE, 'FCE'),
    ]
    course = models.CharField(
        max_length=2,
        choices=COURSE_CHOICES,
        default=STARTERS,
    )

    def __str__(self):
        return self.course

    # def is_upperclass(self):
    #     return self.COURSE in {self.STARTERS, self.MOVERS}

class Period(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.CharField(max_length=15)

    def __str__(self):
        return self.period


class Parent(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1,choices=gender,default='male')
    adress = models.CharField(max_length=300)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    photo = models.ImageField(upload_to='profile_pics/')
    register_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name

class Clss(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    clss = models.CharField(max_length=15)

    def __str__(self):
        return self.clss

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1,choices=gender,default='male')
    birth_date = models.DateField(auto_now_add=False, auto_now=False)
    adress = models.CharField(max_length=300)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    clss = models.ForeignKey(Clss, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_pics/')
    enroll_date = models.DateField(auto_now_add=True)
    start_date = models.DateField(auto_now_add=False, auto_now=False)
    end_date = models.DateField(auto_now_add=False, auto_now=False)
    fee = models.PositiveIntegerField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1,choices=gender,default='male')
    adress = models.CharField(max_length=300)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    photo = models.ImageField(upload_to='profile_pics/')
    apply_date = models.DateField(auto_now_add=True)
    salary = models.PositiveIntegerField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    clss = models.ForeignKey(Clss, on_delete=models.CASCADE)
    date = models.DateField()
    lesson_time = models.TimeField()
    teachers = models.ManyToManyField(Teacher, default=False)
    lesson_title = models.CharField(max_length=15)
    lesson_description = models.CharField(max_length=500)
    lesson_link = models.URLField(max_length=500)
    lesson_preclass = models.URLField(max_length=500)

    def __str__(self):
        return self.lesson_title


class Attendance(models.Model):
    PRESENT = 'PR'
    ABSENT = 'AB'
    SICK = 'SK'
    LEAVE = 'LV'
    STATUS_CHOICES = [
        (PRESENT, 'Present'),
        (ABSENT, 'Absent'),
        (SICK, 'Sick'),
        (LEAVE, 'Leave'),
    ]
    clss = models.ForeignKey(Clss, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)
    date=models.DateField()
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=PRESENT,
    )

    def __str__(self):
        return self.date

