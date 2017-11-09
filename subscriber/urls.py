from django.conf.urls import url
from subscriber.views import *

app_name = 'subscriber'

urlpatterns = [
    url(r'^registered_subscribers/$', MobileSubscribersPageView.as_view(), name='registered_subscribers'),
    url(r'^subscriber/(?P<pk>[0-9]+)/$', MobileSubscriberProfile.as_view(), name='mobile_network_subscriber_detail'),
    url(r'^$', LandingPageView.as_view(), name='landing_page'),
    url(r'^subscriber/', HomePageView.as_view(), name='home'),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', LogOutView.as_view(), name='logout'),
    url(r'^profile/', ProfilePageView.as_view(), name='profile'),
    url(r'^mobile_subscribers/', SubscribersPageView.as_view(), name='mobile_subscribers'),
    url(r'^create_subscriber/$', SubscriberForm.as_view(), name='create_subscriber'),
    url(r'^add_subscriber_bio_data/$', BioDataForm.as_view(), name='add_subscriber'),
    url(r'^capture_image/$', CaptureImagePage.as_view(),name='capture_image'),
    url(r'^add_subscriber_next_of_kin/$', NextOfKinForm.as_view(), name='add_subscriber_next_of_kin'),
    url(r'^bio_data/edit/(?P<pk>[0-9]+)/$', BioDataUpdate.as_view(), name='bio_data_edit'),
    url(r'^next_of_kin/edit/(?P<pk>[0-9]+)/$', NextOfKinUpdate.as_view(), name='next_of_kin_edit'),
    url(r'^profile/edit/(?P<pk>[0-9]+)/$', ProfileUpdateBar.as_view(), name='profile_edit'),
    url(r'^generate/pdf/(?P<subscriber_id>[0-9]+)/$',generate_pdf,name='subscriber_generate_pdf'),
    url(r'^generate/pdf/$', User_generate_pdf, name='user_generate_pdf'),
]



