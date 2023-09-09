from rest_framework import serializers
from job.models import Job

class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ("id","company_name","connect","expiry", "job_description", "experience","job_type", "skills","reference_name","email")