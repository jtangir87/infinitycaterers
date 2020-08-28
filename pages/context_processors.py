from .forms import RequestQuoteForm

def quote_form_processor(request):
 quote_form = RequestQuoteForm()         
 return {'quote_form': quote_form}