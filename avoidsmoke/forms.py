from django import forms

from django.utils.translation import gettext_lazy as _
class Comment(forms.Form):
    name = forms.CharField()
    email=forms.EmailField()
    comment=forms.Textarea()
    # TODO: Define form fields here
