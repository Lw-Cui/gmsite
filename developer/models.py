from django.db import models

class developer(models.Model):
    name = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20,)

    def __unicode__(self):
        return unicode(self.name)

class attendLog(models.Model):
    date = models.DateField()
    morning = models.TimeField(null=True)
    afternoon = models.TimeField(null=True)
    evening = models.TimeField(null=True)
    person = models.ForeignKey(developer)

    def __unicode__(self):
        return unicode(self.date)

    class Meta:
        ordering = ['-date']
