# Generated by Django 2.2.7 on 2019-11-15 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20191115_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_roll',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
