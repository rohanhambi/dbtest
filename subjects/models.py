from django.db import models
from django.urls import reverse
from student_classes.models import StudentClass

# Create your models here.
select_grade = (('O','O'),
                ('A+','A+'),
                ('A','A'),
                ('B+','B+'),
                ('C','C'),
                ('F','F'),)

select_semester = (('1-1','1-1'),
                ('1-2','1-2'),
                ('2-1','2-1'),
                ('2-2','2-2'),
                ('3-1','3-1'),
                ('3-2','3-2'),
                ('4-1','4-1'),
                ('4-2','4-2'),)
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_code = models.IntegerField()
    subject_credits = models.IntegerField(default=2)
    subject_grade = models.CharField(max_length=10,choices=select_grade,default='O')
    subject_semester = models.CharField(max_length=10,choices=select_semester,default='1-1')
    subject_creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    subject_update_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.subject_name
    
    def get_absolute_url(self):
        return reverse('subjects:subject_list')



class SubjectCombination(models.Model):
    select_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    select_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('subjects:subject_combination_list')

    def __str__(self):
        return '%s Section-%s'%(self.select_class.class_name, self.select_class.section)
    
