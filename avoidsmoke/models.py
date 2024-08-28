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
    img=models.ImageField(_("تصویر"), upload_to=None, height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return str(self.title)+"<br>"+str(self.description)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'
# Create your models here.
class Comment(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(_("نام"), max_length=50)
    email=models.EmailField(_("ایمیل"), max_length=254)
    text=models.TextField(_("نظر"))
    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.name+"<br><br>"+self.email+"<br><br>"+self.text

class Idea(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(_("نام"), max_length=50)
    email=models.EmailField(_("ایمیل"), max_length=254)
    idea=models.TextField(_("ایده"))
    class Meta:
        verbose_name = _("Idea")
        verbose_name_plural = _("Ideas")

    def __str__(self):
        return self.name+"<br><br>"+self.email+"<br><br>"+self.idea

class Contact(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(_("نام"), max_length=50)
    email=models.EmailField(_("ایمیل"), max_length=254)
    message=models.TextField(_("متن پیام"))
    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.name+"<br><br>"+self.email+"<br><br>"+self.message