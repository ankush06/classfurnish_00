from django.db import models

# Create your models here.
class merchantProfile(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    def get_name(self):
        """
        Get all active vouchers. The returned ``Queryset`` of vouchers
        is filtered by end date greater then the current date.
        """
        return self.name