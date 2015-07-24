from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

class AttendLog(models.Model):
    user = models.ForeignKey(UserProfile)

    date = models.DateField()
    morning = models.TimeField()
    afternoon = models.TimeField()
    evening = models.TimeField()

    def __unicode__(self):
        return unicode(self.date)

    class Meta:
        ordering = ["-date"]
