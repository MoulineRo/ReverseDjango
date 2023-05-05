from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return str(self.first_name)


class Teachers(models.Model):
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.first_name)


class Groups(models.Model):
    teachers = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Students_Groups(models.Model):
    group = models.ManyToManyField(Groups)
    student = models.ManyToManyField(Student)
    first_name = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return str(self.first_name)
