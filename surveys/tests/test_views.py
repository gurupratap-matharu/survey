from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse
from surveys.forms import SurveyForm
from surveys.views import SurveyCreate


class SurveyCreateTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            email='testuser@email.com',
            password='testpass123'
        )

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
