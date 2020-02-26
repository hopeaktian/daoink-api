from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import PrintOrderModelSerializer
from .models import PrintOrder
from .phone_auth import send_message, phone_verify
from .serializer import RegisterSerializer
from rest_framework.authtoken.models import Token


class RegisterAPIView(APIView):
    # 免Token认证访问
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        """
        获取手机验证码
        :param request: phone_number
        :return:
        """
        # todo: phone_number 验证
        phone_number = request.query_params.get('phone_number')
        if phone_number:
            if send_message(phone_number):
                return Response({'success': True, 'message': 'send msg success'})
            return Response({'success': False, 'message': 'send msg failed, server error'})
        return Response({'success': False, 'message': 'send msg success, param <phone_number> is null'})

    def post(self, request, *args, **kwargs):
        """
        用户注册视图
        """
        ser = RegisterSerializer(data=request.data)
        # 判断参数是否合法
        if ser.is_valid():
            # 创建用户
            user = ser.create(request.data)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'success': True, 'message': '用户注册成功', 'token': token.key})
        return Response({'success': False, 'message': ser.errors, 'token': None})