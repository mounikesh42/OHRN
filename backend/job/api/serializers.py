from rest_framework import serializers
from job.models import Job

class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ("id","company_name","connect", "job_description", "job_type", "skills","reference_name","email")