from django import forms

from surveys.models import Survey


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ('title', 'description',)
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }
