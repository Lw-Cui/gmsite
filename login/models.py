from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

class AttendLog(models.Model):
    user = models.ForeignKey(UserProfile)

    date = models.DateField()
    morning = models.TimeField(null=True)
    afternoon = models.TimeField(null=True)
    evening = models.TimeField(null=True)

    def __unicode__(self):
        return unicode(self.date)

    def __getitem__(self, item):
        if item == 'morning':
            return self.morning
        elif item == 'afternoon':
            return self.afternoon
        elif item == 'evening':
            return self.evening

    def __setitem__(self, key, value):
        if key == 'morning':
            self.morning = value
        elif key == 'afternoon':
            self.afternoon = value
        elif key == 'evening':
            self.evening = value

    class Meta:
        ordering = ["-date"]
