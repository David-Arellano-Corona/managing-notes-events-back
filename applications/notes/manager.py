from django.db import models

class NotesManager(models.Manager):

    def findNotesByOwner(self, owner):
        return self.filter(owner=owner, isStore=False)

    def findNotes(self, owner, isStore, filter):
        return self.filter(
            owner= owner,
            isStore= isStore,
            text__contains= filter
        )    