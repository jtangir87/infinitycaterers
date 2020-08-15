from django.urls import path
from django.views.generic import TemplateView

from .views import HomeView, ContactUsView, contact_us_form


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contact", ContactUsView.as_view(), name="contact_us"),
    path("contact-submit", contact_us_form, name="contact_us_form"),
    path(
        "venues", TemplateView.as_view(template_name="pages/venues.html"), name="venues"
    ),
]

