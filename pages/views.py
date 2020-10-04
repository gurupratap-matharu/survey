from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'


class IndexPageView(TemplateView):
    template_name = 'pages/index.html'
