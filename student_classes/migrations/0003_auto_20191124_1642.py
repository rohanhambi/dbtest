# Generated by Django 2.2.7 on 2019-11-24 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_classes', '0002_studentsemester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsemester',
            name='StudentSemester',
            field=models.CharField(choices=[('1-1', '1-1'), ('1-2', '1-2'), ('2-1', '2-1'), ('2-2', '2-2'), ('3-1', '3-1'), ('3-2', '3-2'), ('4-1', '4-1'), ('4-2', '4-2')], max_length=10),
        ),
    ]
