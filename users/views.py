from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializer import UserSerializer


# Create your views here.


class UserViewSet(mixins.ListModelMixin, GenericViewSet):

    serializer_class = UserSerializer
    model = serializer_class.Meta.model
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        print(request.GET)
        print(args)
        print(kwargs)
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
