from django.views import generic
from django.core.urlresolvers import reverse_lazy

from .forms import *


class Sim(generic.CreateView):
    form_class = SimForm
    template_name = 'sim_registration/sim_form.html'
    success_url = reverse_lazy('subscriber:mobile_subscribers')


class SimUpdate(generic.UpdateView):
    model = RegisteredSims
    form_class = SimUpdateForm
    template_name = 'sim_registration/sim_update_form.html'
    success_url = reverse_lazy('subscriber:mobile_subscribers')
