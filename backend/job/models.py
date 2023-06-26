from django.db import models
from common.models import AuditModel

JOB_TYPE_CHOICES = (
    ('Part-time', 'parttime'),
    ('Full-time', 'fulltime'),
    ('Freelancer', 'freelancer'),
    # ('Remote', 'R'),

    
) 

# Create your models here.
class Job(AuditModel):
    company_name = models.CharField(max_length= 120)
    job_description = models.TextField(blank = True, null = True)
    job_type = models.CharField(choices =JOB_TYPE_CHOICES ,max_length = 20)
    email= models.CharField(max_length=250,default='none')

    skills = models.TextField()
    reference_name= models.CharField(max_length=120,default='none')


    def __str__(self):
        return self.company_name