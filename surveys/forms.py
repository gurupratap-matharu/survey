import datetime
import logging

from django import forms

from surveys.models import Survey

logger = logging.getLogger(__name__)
print('Veer importing {}'.format(__name__))


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ('title', 'description',)
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }


class RegisterForm(forms.Form):
    """
    A dummy form i am creating to try out various django forms
    fields and how do they render.

    Specifically I wanna try out how to make the forms more beautiful
    with bootstrap classes.
    """
    name = forms.CharField(label='Your name', min_length=4, max_length=60,
                           help_text='Please enter your name as it appears on your passport',
                           error_messages={'required': 'Without your name we cannot proceed',
                                           'min_length': 'Is that your full name?', 'max_length': 'Your name is too long'})

    email = forms.EmailField(label='Your email', max_length=100, required=True,
                             help_text='We would never share you email with anyone',
                             error_messages={'required': 'Without this how are gonna contact you my friend'})

    website = forms.URLField(label='Your website', max_length=100, initial='http://',
                             help_text='Where can we know more about you?')
    day = forms.DateField(label='Subscription date', initial=datetime.date.today,
                          help_text='From this date we will charge you for our services')

    terms = forms.BooleanField(label='I have read the terms and conditions?', required=True)
