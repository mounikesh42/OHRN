from django.contrib.auth import get_user_model
from django.db import models

from users.models import User


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class AuditModel(models.Model):
    created_ts = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user), editable=False,
                                   related_name='%(class)s_created_by_set' ,null=True,blank=True)
    modified_ts = models.DateTimeField(auto_now=True,null=True, blank=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user), editable=False,
                                    related_name='%(class)s_modified_by_set',null=True,blank=True)

    class Meta:
        abstract = True

    # def __str__(self):
    #     return f"{self.created_ts.strftime('%d-%m-%Y')}"


