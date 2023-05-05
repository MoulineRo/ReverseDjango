from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from polls.forms import StudentForm, TeachersForm, Students_GroupsForm
from .forms import Student, Teachers, Students_Groups


def index(request):
    return HttpResponse("Choose another id")


def student_view(request, id: int):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))
    if request.method == "GET":
        form = StudentForm(instance=student)
        context = {"form": form}
        return render(request, "student.html", context)
    elif request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if not form.is_valid():
            return HttpResponse(reverse("new_student"))
        if 'create' in request.POST:
            form.save()
            context = {"form": form}
            return render(request, "student.html", context)
        if 'delete' in request.POST:
            student.delete()
            return HttpResponseRedirect(reverse("all_students"))


def all_students(request):
    if request.method == "GET":
        student = Student.objects.all()
        return render(request, "all_students.html", {"student": student})


def new_student(request):
    if request.method == "GET":
        form = StudentForm()
        context = {"form": form}
        return render(request, "new_student.html", context)
    elif request.method == "POST":
        form = StudentForm(request.POST)
        if not form.is_valid():
            return HttpResponse(reverse("new_student"))
        form.save()
        return HttpResponseRedirect(reverse("student_view", args=[form.instance.id]))


def teacher_view(request, id: int):
    try:
        teachers = Teachers.objects.get(id=id)
    except Teachers.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))
    if request.method == "GET":
        form = TeachersForm(instance=teachers)
        context = {"form": form}
        return render(request, "teachers.html", context)
    elif request.method == "POST":
        form = TeachersForm(request.POST, instance=teachers)
        if not form.is_valid():
            return HttpResponse(reverse("new_teachers"))

        if 'create' in request.POST:
            form.save()
            context = {"form": form}
            return render(request, "teachers.html", context)
        if 'delete' in request.POST:
            teachers.delete()
            return HttpResponseRedirect(reverse("all_teachers"))


def all_teachers(request):
    if request.method == "GET":
        teachers = Teachers.objects.all()
        return render(request, "all_teachers.html", {"teachers": teachers})


def new_teachers(request):
    if request.method == "GET":
        form = TeachersForm()
        context = {"form": form}
        return render(request, "new_teachers.html", context)
    elif request.method == "POST":
        form = TeachersForm(request.POST)
        if not form.is_valid():
            return HttpResponse(reverse("new_teachers"))
        form.save()
        return HttpResponseRedirect(reverse("teacher_view", args=[form.instance.id]))


def add_st_to_group(request):
    if request.method == "GET":
        form = Students_GroupsForm()
        context = {"form": form}
        return render(request, "add_to_group.html", context)
    elif request.method == "POST":
        form = Students_GroupsForm(request.POST)
        if not form.is_valid():
            return HttpResponse(reverse("add_st_to_group"))
        form.save()
        get = Students_Groups.objects.latest('id')
        Student.objects.create(first_name=get.first_name, year=get.year)
        return HttpResponse('OK Your name added')
