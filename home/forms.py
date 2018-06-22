from django import forms

from .models import Search


class HomeForm(forms.ModelForm):
    school = forms.CharField(max_length=100, required=False)
    prof = forms.CharField(max_length=100, required=False)
    college = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Search
        fields = ('school',
                  'prof',
                  'college',)