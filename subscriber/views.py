# -*- coding: utf-8 -*-
from django.http import HttpResponse,HttpResponseForbidden
from django.views import generic
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate,login,logout
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .forms import *
from .models import Subscriber,NextOfKin,CaptureImage
from django.template import RequestContext
from simRegistration.models import RegisteredSims
from django.template.loader import get_template
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML,CSS
import tempfile
from django.conf import settings

# Create your views here.
"""This generates a pdf file for subscriber's profile detail"""


def generate_pdf(request,subscriber_id):
    html_template = get_template('subscriber/subscriber_profile_report.html')
    subscriber = Subscriber.objects.get(pk=subscriber_id)

    rendered_html = html_template.render({'subscriber': subscriber}).encode(encoding="UTF-8")

    pdf_file = HTML(string=rendered_html).write_pdf(
        stylesheets=['iwsrs/static/assets/css/now-ui-kit.css','iwsrs/static/assets/css/bootstrap.min.css'])

    http_response = HttpResponse(pdf_file,content_type='application/pdf')
    http_response['Content-Disposition'] = 'filename="report.pdf"'

    return http_response


def User_generate_pdf(request):
    html_template = get_template('subscriber/user_profile_report.html')
    user = request.user

    rendered_html = html_template.render({'user': user}).encode(encoding="UTF-8")

    pdf_file = HTML(string=rendered_html).write_pdf(
        stylesheets=['iwsrs/static/assets/css/now-ui-kit.css','iwsrs/static/assets/css/bootstrap.min.css'])

    http_response = HttpResponse(pdf_file,content_type='application/pdf')
    http_response['Content-Disposition'] = 'filename="report.pdf"'

    return http_response


def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            m = CaptureImage.objects.get(pk=id)
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')


class CaptureImagePage(generic.TemplateView):
    template_name = 'subscriber/capture_image.html'


class ProfileUpdateBar(generic.DetailView):
    model = Subscriber
    template_name = 'subscriber/side_bar_update.html'


class SubscriberForm(generic.TemplateView):
    template_name = 'subscriber/register_subscribers.html'


class BioDataForm(generic.CreateView):
    form_class = BioDataForm
    template_name = 'subscriber/bio_data_form.html'
    success_url = reverse_lazy('subscriber:add_subscriber_next_of_kin')


class NextOfKinForm(generic.CreateView):
    form_class = NextOfKinForm
    template_name = 'subscriber/next_of_kin_form.html'
    success_url = reverse_lazy('subscriber:add_subscriber_sim_detail')


class BioDataUpdate(generic.UpdateView):
    model = Subscriber
    form_class = BioDataUpdateForm
    template_name = 'subscriber/bio_data_update_form.html'
    success_url = reverse_lazy('subscriber:mobile_subscribers')


class NextOfKinUpdate(generic.UpdateView):
    model = NextOfKin
    form_class = NextOfKinUpdateForm
    template_name = 'subscriber/next_of_kin_update_form.html'
    success_url = reverse_lazy('subscriber:mobile_subscribers')


class MobileSubscribersPageView(generic.ListView):
    template_name = 'mobile_network_operator/mobile_operator_page.html'
    context_object_name = 'mobile_network_subscriber_list'

    def get_queryset(self):
        return RegisteredSims.objects.all()


class MobileSubscriberProfile(generic.DetailView):
    model = Subscriber
    template_name = 'subscriber/mobile_network_subscriber_detail.html'


"""The users visits this page first before logging-in"""


class LandingPageView(TemplateView):
    template_name = "subscriber/landing-page.html"


class HomePageView(TemplateView):
    template_name = "base_generic.html"


class ProfilePageView(generic.TemplateView):
    template_name = "subscriber/profile.html"


class SubscribersPageView(generic.ListView):
    template_name = 'subscriber/mobile_subscibers.html'
    context_object_name = 'mobile_subscriber_list'

    def get_queryset(self):
        return Subscriber.objects.all()

"""User login page"""
class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('subscriber:profile')
    template_name = 'registration/accounts/login.html'

    def form_valid(self,form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username,password=password)

        if user is not None and user.is_active:
            login(self.request,user)
            return super(LoginView,self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogOutView(generic.RedirectView):
    url = reverse_lazy('subscriber:landing_page')

    def get(self,request,*args,**kwargs):
        logout(request)
        return super(LogOutView,self).get(request,*args,**kwargs)


class NextOfKinUpdateFormTest(generic.UpdateView):
    model = NextOfKin
    template_name = 'subscriber/next_of_kin_test.html'
    fields = '__all__'
