# Generated by Django 4.2.1 on 2023-05-05 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Students_Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('group', models.ManyToManyField(to='polls.groups')),
                ('student', models.ManyToManyField(to='polls.student')),
            ],
        ),
        migrations.AddField(
            model_name='groups',
            name='teachers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.teachers'),
        ),
    ]
