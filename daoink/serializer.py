from rest_framework import serializers
from .models import PrintOrder


class PrintOrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintOrder
        fields = "__all__"              # 将表中所有字段序列化