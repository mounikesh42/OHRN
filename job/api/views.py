from rest_framework import views,viewsets
from job.models import Job
from .serializers import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset= Job.objects.all().order_by('-id')
    serializer_class = JobSerializer
    permission_class = []
    authentication_class = []