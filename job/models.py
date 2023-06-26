from django.db import models
from common.models import AuditModel

JOB_TYPE_CHOICES = (
    ('Parttime', 'parttime'),
    ('Fulltime', 'fulltime'),
    ('Freelancer', 'freelancer'),
    
) 

# Create your models here.
class Job(AuditModel):
    company_name = models.CharField(max_length= 120)
    job_description = models.TextField(blank = True, null = True)
    job_type = models.CharField(choices =JOB_TYPE_CHOICES ,max_length = 20)
    skills = models.TextField()

    def __str__(self):
        return self.company_name