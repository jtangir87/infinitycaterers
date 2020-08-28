from django import forms
from bootstrap_datepicker_plus import DatePickerInput


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "How can we help?"})
    )


EVENT_TYPE_CHOICES = [
    ("Wedding", "Wedding"),
    ("Bar/Bat Mitzvah", "Bar/Bat Mitzvah"),
    ("Corporate", "Corporate"),
    ("Private Party", "Private Party"),
]


class RequestQuoteForm(forms.Form):
    name = name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    event_date = forms.DateField(
        widget=DatePickerInput(format="%m/%d/%Y"), label="Event Date"
    )
    event_type = forms.ChoiceField(choices=EVENT_TYPE_CHOICES, label="Event Type")
