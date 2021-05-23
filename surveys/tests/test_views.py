from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SurveyCreateTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            email='testuser@email.com',
            password='testpass123'
        )

    def test_survey_create_view_redirect_for_anonymous_user(self):
        self.fail()

    def test_survey_create_view_works_for_logged_in_user(self):
        self.fail()

    def test_survey_create_view_contains_survey_create_form(self):
        self.fail()

    def test_survey_create_view_resolve_SurveyCreateView(self):
        self.fail()

    def test_survey_create_view_uses_correct_html_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('survey_create'))
        self.assertTemplateUsed(response, 'surveys/survey_form.html')
