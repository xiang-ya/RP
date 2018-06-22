from django import forms
from searchings.models import Rating


class RatingForm(forms.ModelForm):
    attendance_choices = (
        ('未知', "it's still a secret"),
        ('每周必点', "100% take attendance"),
        ('人少就点', "if there seems like not enough people"),
        ('基本不管', "doesn't really care the attendance"),
        ('纯看心情', "depends on the days or professor's mood"),
    )
    overall_rating = forms.FloatField(max_value=5, min_value=0, required=True)
    overall_difficulty_number = forms.FloatField(max_value=5, min_value=0, required=True)
    class_graded = forms.CharField(max_length=100, required=True)
    overall_difficulty = forms.CharField(max_length=100, required=True)
    overall_looking = forms.CharField(max_length=100, required=True)
    attendance_requirement = forms.ChoiceField(choices=attendance_choices, required=True)
    prof_personality_tag = forms.CharField(max_length=50, required=True)
    student_learning_tag = forms.CharField(max_length=50, required=True)
    class_atmosphere_tag = forms.CharField(max_length=30,required=True)
    homework_requirement_tag = forms.CharField(max_length=30,required=True)
    teaching_style_tag = forms.CharField(max_length=30, required=True)

    class Meta:
        model = Rating
        fields = ('overall_rating',
                  'overall_difficulty_number',
                  'class_graded',
                  'overall_difficulty',
                  'overall_looking',
                  'attendance_requirement',
                  'prof_personality_tag',
                  'student_learning_tag',
                  'class_atmosphere_tag',
                  'homework_requirement_tag',
                  'teaching_style_tag')
