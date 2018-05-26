# Generated by Django 2.0.5 on 2018-05-25 23:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=10, unique=True)),
                ('course_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CourseWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_course_work', models.CharField(max_length=50)),
                ('weight', models.FloatField()),
                ('grade', models.FloatField()),
                ('course', models.ForeignKey(on_delete=models.SET('deleted'), related_name='course_work', to='courses.Course')),
                ('starter', models.ForeignKey(on_delete=models.SET('deleted'), related_name='course_work', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
