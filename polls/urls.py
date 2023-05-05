from django.urls import path

from . import views

urlpatterns = [
    path(' ', views.index, name='index'),
    path('student/', views.new_student, name='new_student'),
    path('students/', views.all_students, name='all_students'),
    path('students<int:id>/', views.student_view, name='student_view'),
    path('teachers/', views.new_teachers, name='new_teachers'),
    path('allteachers/', views.all_teachers, name='all_teachers'),
    path('teachersedit<int:id>/', views.teacher_view, name='teacher_view'),
    path('add_to_gr/', views.add_st_to_group, name='add_st_to_group'),
]
