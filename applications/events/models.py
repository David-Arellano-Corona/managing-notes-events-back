from django.db import models
from applications.users.models import Users
from model_utils.models import (
    SoftDeletableModel,
    TimeStampedModel
)
# Create your models here.
class Events(SoftDeletableModel, TimeStampedModel,models.Model):
    name = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True)
    starttime = models.DateTimeField(null=False)
    endtime = models.DateTimeField(null=False)

    owner = models.ForeignKey(Users, related_name="user_event", on_delete=models.CASCADE)