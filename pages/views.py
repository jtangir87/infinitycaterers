from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.template.loader import get_template
from django.core.mail import send_mail


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
    pass


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
                "event_date": form.cleaned_data["requested_date"],
                "event_type": form.cleaned_data["event_type"],
            }

            ### SEND EMAIL ###

            template = get_template("pages/emails/quote_request.txt")
            content = template.render(context)
            send_mail(
                "NEW QUOTE REQUEST",
                content,
                "{}<{}>".format(name, email),
                ## @todo SET EMAIL ADDRESS ##
                ["chad@exteriordd.com", "darren@exteriordd.com"],
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
