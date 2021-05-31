from django.urls import path

from surveys.views import (SurveyCreate, SurveyDelete, SurveyDetail,
                           SurveyList, SurveyRegister, SurveyUpdate)

"""
Rest Endpoints for surveys app

POST /surveys -> create a survey
GET /surveys/:id -> Retrieve a survey
POST /surveys/:id -> Update a survey (optional)
POST /surveys/:id/submit -> Submit a survey
POST /surveys/:id/delete -> Delete a survey
GET /surveys -> List all surveys
"""
urlpatterns = [
    path('', SurveyList.as_view(), name='survey_list'),
    path('create/', SurveyCreate.as_view(), name='survey_create'),
    path('<uuid:pk>/', SurveyDetail.as_view(), name='survey_detail'),
    path('<uuid:pk>/update/', SurveyUpdate.as_view(), name='survey_update'),
    path('<uuid:pk>/delete/', SurveyDelete.as_view(), name='survey_delete'),
    path('register/', SurveyRegister.as_view(), name='survey_register'),
]
