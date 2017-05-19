from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ToDo(models.Model):

    title = models.CharField(max_length=140, unique=True)
    content = models.TextField(max_length=250)
    createdate = models.DateTimeField(auto_now_add=True)
    tododate = models.DateTimeField()
    user = models.ForeignKey("auth.User")

    def __unicode__(self):
        return self.title

    class Meta:

        ordering = ["-createdate"]
