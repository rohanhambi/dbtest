# Generated by Django 2.2.7 on 2019-11-24 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_subject_subject_credits'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subject_grade',
            field=models.CharField(choices=[('O', 'O'), ('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('C', 'C'), ('F', 'F')], default=False, max_length=10),
        ),
    ]
