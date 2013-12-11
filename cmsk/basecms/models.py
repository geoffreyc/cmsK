from django.db import models
from django.contrib.auth.models import User


# Media Table
class Media(models.Model):
    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Medias"

    name = models.CharField(max_length=80)
    path = models.CharField(max_length=5096)
    description = models.CharField(max_length=256)
    date_added = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(User)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.user