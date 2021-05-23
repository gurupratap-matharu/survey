from django import forms

from surveys.models import Survey


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ('title', 'description',)
