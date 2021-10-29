from django.db import models
from applications.users.models import Users
from model_utils.models import (
    SoftDeletableModel,
    TimeStampedModel
)
from .manager import NotesManager

# Create your models here.
class Notes(SoftDeletableModel, TimeStampedModel, models.Model):
    text = models.TextField()

    owner = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="note_owner")

    isStore=models.BooleanField(default=False)

    objects = NotesManager()