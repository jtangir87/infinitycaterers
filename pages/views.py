from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import ContactUsForm

# Create your views here.
class HomeView(TemplateView):
    template_name = "pages/home.html"


class ContactUsView(TemplateView):
    template_name = "pages/contact_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_form"] = ContactUsForm()
        return context


def contact_us_form(request):
    pass
