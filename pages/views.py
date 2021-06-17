from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.template.loader import get_template
from django.core.mail import send_mail
from django.contrib import messages

from .forms import ContactUsForm, RequestQuoteForm

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
    if request.method == "POST":
        form = ContactUsForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            context = {
                "name": name,
                "email": email,
                "phone": form.cleaned_data["phone"],
                "message": form.cleaned_data["message"],
            }

            ### SEND EMAIL ###

            template = get_template("pages/emails/contact_us.txt")
            content = template.render(context)
            send_mail(
                "NEW CONTACT FORM",
                content,
                "{}<{}>".format(name, email),
                ["fred@cbdevents.com"],
                fail_silently=False,
            )
            messages.success(
                request, 'Your form has been submitted. We will be in touch soon!')
    return HttpResponseRedirect(reverse("contact_us"))


def request_quote(request):
    data = dict()
    if request.method == "POST":
        form = RequestQuoteForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            context = {
                "name": name,
                "email": email,
                "phone": form.cleaned_data["phone"],
                "event_date": form.cleaned_data["event_date"],
                "event_type": form.cleaned_data["event_type"],
            }

            ### SEND EMAIL ###

            template = get_template("pages/emails/quote_request.txt")
            content = template.render(context)
            send_mail(
                "NEW QUOTE REQUEST",
                content,
                "{}<{}>".format(name, email),
                ["fred@cbdevents.com"],
                fail_silently=False,
            )

            data["html_success_message"] = render_to_string(
                "pages/includes/partial_quote_submit_success.html", request=request,
            )
            data["form_is_valid"] = True

        else:
            data["form_is_valid"] = False
    else:
        quote_form = RequestQuoteForm()
        data["html_form"] = render_to_string(
            "pages/includes/partial_quote_form.html",
            {"quote_form": quote_form},
            request=request,
        )
    return JsonResponse(data)
