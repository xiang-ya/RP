from django import forms
from .models import Post


class ProfessorForm(forms.ModelForm):
    post = forms.TextInput()

    class Meta:
        model = Post
        fields = ('post',)
