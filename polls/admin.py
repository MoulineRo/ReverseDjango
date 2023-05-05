from django.contrib import admin

from polls.models import Teachers, Groups, Student, Students_Groups

admin.site.register(Teachers)
admin.site.register(Groups)
admin.site.register(Student)
admin.site.register(Students_Groups)
