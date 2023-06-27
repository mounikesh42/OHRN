from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from .serializers import JobSerializer
from job.models import Job

from rest_framework.filters import SearchFilter
# from django_filters.rest_framework import DjangoFilterBackend

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-id')
    serializer_class = JobSerializer
    permission_classes = []
    authentication_classes = []

    filter_backends = [SearchFilter]
    search_fields = ['skills']

    def get_permissions(self):
        if self.request.method in ['POST', 'DELETE', 'PUT']:
            self.authentication_classes = [TokenAuthentication]
            # self.permission_classes = [IsAuthenticated]
        else:
            self.authentication_classes = []
            self.permission_classes = []
        return super().get_permissions()

    def get_queryset(self):
        queryset = super().get_queryset()
        skills = self.request.query_params.get('skills', None)
        if skills:
            queryset = queryset.filter(skills__icontains=skills)
        return queryset
