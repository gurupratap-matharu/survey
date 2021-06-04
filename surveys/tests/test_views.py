from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import resolve, reverse

from surveys.forms import SurveyForm
from surveys.models import Survey
from surveys.views import SurveyCreate

print('Veer importing {}'.format(__name__))


class SurveyCreateTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            email='testuser@email.com',
            password='testpass123'
        )
        self.data = {'title': 'Favorite City', 'description': 'We would like to know your favorite city'}

    def test_survey_create_view_redirect_for_anonymous_user(self):
        response = self.client.get(reverse('survey_create'))
        self.assertTemplateNotUsed(response, 'surveys/survey_form.html')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=response.url, status_code=302,
                             target_status_code=200)

    def test_survey_create_view_works_for_logged_in_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('survey_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'surveys/survey_form.html')

    def test_survey_create_view_contains_survey_create_form(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('survey_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'surveys/survey_form.html')
        self.assertIsInstance(response.context['form'], SurveyForm)

    def test_survey_create_view_resolve_SurveyCreateView(self):
        view = resolve(reverse('survey_create'))
        self.assertEqual(view.func.__name__, SurveyCreate.as_view().__name__)

    def test_survey_create_view_uses_correct_html_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('survey_create'))
        self.assertTemplateUsed(response, 'surveys/survey_form.html')

    def test_survey_create_view_works(self):
        path = reverse('survey_create')

        self.assertEqual(Survey.objects.count(), 0)
        self.client.force_login(self.user)
        response = self.client.post(path=path, data=self.data)

        survey = Survey.objects.all()[0]

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Survey.objects.count(), 1)
        self.assertEqual(survey.title, data.get('title'))
        self.assertEqual(survey.description, data.get('description'))
        self.assertEqual(survey.author, self.user)

        expected_url = survey.get_absolute_url()
        self.assertRedirects(response, expected_url=expected_url, status_code=302,
                             target_status_code=200)

    def test_survey_create_view_redirects_to_survey_detail_after_successful_creation(self):

        self.client.force_login(self.user)
        response = self.client.post(path=reverse('survey_create'), data=self.data)
        survey = Survey.objects.first()
        expected_url = survey.get_absolute_url()

        self.assertRedirects(response, expected_url=expected_url, status_code=302, target_status_code=200)

    def test_survey_create_view_creates_success_alert_after_successful_creation(self):
        self.client.force_login(self.user)
        response = self.client.post(path=reverse('survey_create'), data=self.data)
        messages = list(get_messages(response.wsgi_request))

        expected_message = f"{self.data.get('title')} created successfully!"

        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), expected_message)

    def test_survey_create_view_assigns_logged_in_user_after_successful_creation(self):
        self.assertEqual(Survey.objects.count(), 0)
        self.client.force_login(self.user)
        response = self.client.post(path=reverse('survey_create'), data=self.data)

        survey = Survey.objects.first()
        self.assertEquals(survey.author, self.user)
