from django.forms import ModelForm

from polls.models import Student, Teachers, Groups, Students_Groups


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "year"]


class TeachersForm(ModelForm):
    class Meta:
        model = Teachers
        fields = ["first_name"]


class GroupsForm(ModelForm):
    class Meta:
        model = Groups
        fields = ['name']


class Students_GroupsForm(ModelForm):
    class Meta:
        model = Students_Groups
        fields = ["first_name", "year"]
