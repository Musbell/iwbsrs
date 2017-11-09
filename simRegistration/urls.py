from django.conf.urls import url
from .views import *

app_name = 'sim_reg'

urlpatterns = [
    url(r'^add_subscriber_sim_detail/$', Sim.as_view(), name='add_subscriber_sim_detail'),
    url(r'^reg_sim/edit/(?P<pk>[0-9]+)/$', SimUpdate.as_view(), name='reg_sim_edit'),
]



