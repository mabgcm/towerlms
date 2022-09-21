from django.contrib import admin
from .models import Course, Period, Clss, Parent, Student, Teacher, Lesson, Attendance

class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)

class TeacherAdmin(admin.ModelAdmin):
    pass
admin.site.register(Teacher, TeacherAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Attendance, AttendanceAdmin)

class ParentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Parent, ParentAdmin)

class CourseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Course, CourseAdmin)

class PeriodAdmin(admin.ModelAdmin):
    pass
admin.site.register(Period, PeriodAdmin)

class ClssAdmin(admin.ModelAdmin):
    pass
admin.site.register(Clss, ClssAdmin)

class LessonAdmin(admin.ModelAdmin):
    pass
admin.site.register(Lesson, LessonAdmin)
