import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from surveys.forms import SurveyForm
from surveys.models import Survey

logger = logging.getLogger(__name__)
print('Veer logger: {}'.format(logger))
logger.debug('Veer I am debug')
logger.info('Veer I am info')
logger.warning('Veer I am warning')
logger.error('Veer I am error')
logger.critical('Veer I am critical')


class SurveyList(ListView):
    model = Survey
    template_name = 'surveys/survey_list.html'


class SurveyDetail(DetailView):
    model = Survey
    template_name = 'surveys/survey_detail.html'


class SurveyCreate(LoginRequiredMixin, CreateView):
    model = Survey
    form_class = SurveyForm
    template_name = 'surveys/survey_form.html'
    success_message = '%(title)s created successfully!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SurveyUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Survey
    template_name = 'surveys/survey_update_form.html'
    success_message = '%(title)s updated successfully!'


class SurveyDelete(LoginRequiredMixin, DeleteView):
    model = Survey
    template_name = 'surveys/survey_confirm_delete.html'
    success_message = '%s(title) deleted successfully!'
