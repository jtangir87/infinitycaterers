from django.urls import path
from django.views.generic import TemplateView

from .views import HomeView, ContactUsView, contact_us_form, request_quote


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contact", ContactUsView.as_view(), name="contact_us"),
    path("contact-submit", contact_us_form, name="contact_us_form"),
    path("request-quote", request_quote, name="request_quote"),
    path(
        "about-us",
        TemplateView.as_view(template_name="pages/about_us.html"),
        name="about_us",
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
    path(
        "menus/informal-event",
        TemplateView.as_view(template_name="pages/menus/informal.html"),
        name="menu_informal",
    ),
    ## VENUES ##
    path(
        "venues",
        TemplateView.as_view(template_name="pages/venues/venues_list.html"),
        name="venues",
    ),
    path(
        "venues/society-hill-dance-academy",
        TemplateView.as_view(template_name="pages/venues/shda.html"),
        name="venue_shda",
    ),
    path(
        "venues/platform-thirty",
        TemplateView.as_view(template_name="pages/venues/platform_thirty.html"),
        name="venue_platform_thirty",
    ),
    path(
        "venues/beat-street",
        TemplateView.as_view(template_name="pages/venues/beat_street.html"),
        name="venue_beat_street",
    ),
    path(
        "venues/or-ami",
        TemplateView.as_view(template_name="pages/venues/or_ami.html"),
        name="venue_or_ami",
    ),
]

