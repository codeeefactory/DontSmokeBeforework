from django import forms
from .models import Comment, Contact, Idea
from django.utils.translation import gettext_lazy as _
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        exclude=['id']

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        exclude=['id']
    # TODO: Define form fields here
class ContactForm(forms.Form):
   class Meta:
        model = Contact
        exclude=['id']