# Generated by Django 2.2.7 on 2019-11-24 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0008_auto_20191124_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjectcombination',
            name='subject_semester',
        ),
    ]