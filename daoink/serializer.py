import re
import logging
from rest_framework import serializers
from .models import PrintOrder, User
from daoink_api.settings import REGEX_MOBILE
from .phone_auth import phone_verify

logger = logging.getLogger(__name__)


class PrintOrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintOrder
        fields = "__all__"              # 将表中所有字段序列化


class RegisterSerializer(serializers.Serializer):
    """
    用户发送手机验证码的Serializer类
    """
    phone_number = serializers.CharField(label='手机号码', max_length=11, min_length=11, required=True,
                                         error_messages={
                                             'required': '手机号码必填',
                                             'max_length': '手机号码格式错误',
                                             'min_length': '手机号码格式错误',
                                         })
    verify_code = serializers.CharField(label='手机验证码', max_length=6, min_length=6, write_only=True, required=True,
                                        error_messages={
                                            'required': '手机验证码必填',
                                            'max_length': '验证码格式错误',
                                            'min_length': '验证码格式错误',
                                        })
    password = serializers.CharField(label='手机验证码', min_length=6, write_only=True, required=True,
                                     error_messages={
                                         'required': '密码必填',
                                         'min_length': '密码需大于6位',
                                     })

    def validate_phone_number(self, *args, **kwargs):
        """
        验证手机号码的函数
        :return:
        """
        phone_number = self.initial_data.get('phone_number')
        # 正则判断手机号码格式
        if not re.match(REGEX_MOBILE, phone_number):
            raise serializers.ValidationError('手机号码格式错误')
        # 判断用户是否注册
        if User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError('该用户已经存在')
        return phone_number

    def validate_verify_code(self, *args, **kwargs):
        """
        手机验证码的校验
        :return:
        """
        phone_number = self.initial_data.get('phone_number')
        verify_code = self.initial_data.get('verify_code')
        if not phone_verify(phone_number, verify_code):
            raise serializers.ValidationError('验证码错误')
        return phone_number

    def create(self, validated_data):
        """
        创建用户
        :param validated_data:
        :return:
        """
        try:
            user = User.objects.create_user(username=validated_data.get('phone_number'),
                                            phone_number=validated_data.get('phone_number'),
                                            apassword=validated_data.get('password'))
            return user
        except Exception as e:
            logger.error(e)
            raise serializers.ValidationError({'success': False, 'message': 'inner server error', 'token': None})