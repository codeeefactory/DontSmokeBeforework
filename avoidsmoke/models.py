from django.db import models
from django.utils.translation import gettext_lazy as _
class Content(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField(_(""))

    def __str__(self):
        return str(self.title)+"<br>"+str(self.description)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'
# Create your models here.
