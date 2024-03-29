from django.db import models
from django.urls import reverse
# Create your models here.
# select_semester = (('1-1','1-1'),
#                 ('1-2','1-2'),
#                 ('2-1','2-1'),
#                 ('2-2','2-2'),
#                 ('3-1','3-1'),
#                 ('3-2','3-2'),
#                 ('4-1','4-1'),
#                 ('4-2','4-2'),)
class StudentClass(models.Model):
    class_name              =   models.CharField(max_length=100, help_text='Eg- Third, Fouth,Sixth etc')
    class_name_in_numeric   =   models.IntegerField(help_text='Eg- 1,2,4,5 etc') 
    section                 =   models.CharField(max_length=10, help_text='Eg- A,B,C etc')
    creation_date           =   models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return reverse('student_classes:class_list')

    def __str__(self):
        return "%s Section-%s"%(self.class_name, self.section)


# class StudentSemester(models.Model):
#     StudentSemester = models.CharField(max_length=100,choices=select_semester)