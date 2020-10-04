from django.urls import path

from pages.views import ContactPageView, HomePageView, IndexPageView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('index/', IndexPageView.as_view(), name='index'),
    path('contact/', ContactPageView.as_view(), name='contact'),

]
