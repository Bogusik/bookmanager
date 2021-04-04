from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import UserSerializer
from .permissions import UserViewSetPermissions


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        UserViewSetPermissions
    ]

    @action(detail=False, methods=['get'])
    def me(self, request, *args, **kwargs):
        return Response(self.serializer_class(request.user).data)
