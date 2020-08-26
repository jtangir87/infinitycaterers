from django.urls import path
from django.views.generic import TemplateView

from .views import HomeView, ContactUsView, contact_us_form


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contact", ContactUsView.as_view(), name="contact_us"),
    path("contact-submit", contact_us_form, name="contact_us_form"),
    path(
        "about-us",
        TemplateView.as_view(template_name="pages/about_us.html"),
        name="about_us",
    ),
    path(
        "venues", TemplateView.as_view(template_name="pages/venues.html"), name="venues"
    ),
    path(
        "gallery",
        TemplateView.as_view(template_name="pages/gallery.html"),
        name="gallery",
    ),
    ## MENUS ##
    path(
        "menus/wedding",
        TemplateView.as_view(template_name="pages/menus/wedding.html"),
        name="menu_wedding",
    ),
    path(
        "menus/mitzvah",
        TemplateView.as_view(template_name="pages/menus/mitzvah.html"),
        name="menu_mitzvah",
    ),
    path(
        "menus/private-party",
        TemplateView.as_view(template_name="pages/menus/private.html"),
        name="menu_private",
    ),
]

