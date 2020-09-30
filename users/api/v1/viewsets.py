from rest_framework import authentication
from users.models import Hygfhgfj
from .serializers import HygfhgfjSerializer
from rest_framework import viewsets


class HygfhgfjViewSet(viewsets.ModelViewSet):
    serializer_class = HygfhgfjSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Hygfhgfj.objects.all()
