# coding=utf8
import datetime
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

EXPIRE_MINUTES = getattr(settings, 'REST_FRAMEWORK_TOKEN_EXPIRE_MINUTES', 1)


class SelfObtainAuthToken(ObtainAuthToken):
    """Create user token"""
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'success': True,
                             'token': token.key,
                             'username': user.username,
                             'user_id': user.id})
        return Response({'success': False,
                         'token': None,
                         'username': None,
                         'user_id': None})


self_obtain_auth_token = SelfObtainAuthToken.as_view()