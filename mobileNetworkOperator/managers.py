from django.db.models.query import QuerySet
from .models import MobileNetworkOperator


class MobileNetworkSubscribers(QuerySet):
    def subscribers(self):
        return self.filter(mobile_network=MobileNetworkOperator.mobile_network.network_name)


MobileNetworkSubscribersManager = MobileNetworkSubscribers.as_manager()