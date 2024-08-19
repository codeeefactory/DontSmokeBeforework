from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
class Content(models.Model):
    author = models.ForeignKey(
       settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='nevisandeh')
    title=models.CharField(_("قبل از"),max_length=20)
    description=models.TextField(_("نکش"))
    label=models.CharField(_("برچسب"), max_length=50)
    
    def __str__(self):
        return str(self.title)+"<br>"+str(self.description)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'
# Create your models here.
