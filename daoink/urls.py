from django.urls import path
# from rest_framework_jwt.views import obtain_jwt_token
from .views import TestAPIView
from rest_framework.authtoken import views
from daoink_api.views import self_obtain_auth_token

urlpatterns = [
    # drf自带token认证
    # path(r'api-token-auth/', views.obtain_auth_token),
    # 自定义的drf自带token认证
    path(r'login/', self_obtain_auth_token),
    # path(r'api-token-auth/', obtain_expiring_auth_token),
    # JWT的认证接口
    # path('jwt-token-auth', obtain_jwt_token),
    path(r'testapi/', TestAPIView.as_view(), name='test')
]