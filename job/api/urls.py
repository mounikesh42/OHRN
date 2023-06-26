from rest_framework.routers import DefaultRouter
from django.urls import path
from job.api.views import JobViewSet


router = DefaultRouter()


router.register(r'jobs', JobViewSet)


urlpatterns = [
    
]

urlpatterns += router.urls
