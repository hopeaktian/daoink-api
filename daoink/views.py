from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import PrintOrderModelSerializer
from .models import PrintOrder
from rest_framework.authtoken.views import ObtainAuthToken


# class LoginView(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key})


class TestAPIView(APIView):
    def get(self, request, format=None):
        return Response("测试")