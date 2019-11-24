# Generated by Django 2.2.7 on 2019-11-24 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_classes', '0002_studentsemester'),
        ('subjects', '0004_auto_20191124_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectcombination',
            name='subject_semester',
            field=models.ForeignKey(choices=[('1-1', '1-1'), ('1-2', '1-2'), ('2-1', '2-1'), ('2-2', '2-2'), ('3-1', '3-1'), ('3-2', '3-2'), ('4-1', '4-1'), ('4-2', '4-2')], default='1-1', on_delete=django.db.models.deletion.CASCADE, to='student_classes.StudentSemester'),
        ),
    ]