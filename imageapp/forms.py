from django import forms

from imageapp.models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields='__all__'