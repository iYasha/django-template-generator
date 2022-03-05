from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from base.views import *
from accounts.serializers import *
from accounts.models import *
from drf_yasg import openapi

from rest_framework import status

un_auth = openapi.Response('Error: Unauthorized', ErrorSerializer)
server_error = openapi.Response('Error: Server Error', ErrorSerializer)
user_in_blacklist_error = openapi.Response('Error: User in blacklist', ErrorSerializer)


# class CreateUserView(mixins.CreateModelMixin, mixins.UpdateModelMixin, BaseView):
#     serializer_class = UserSerializer
#     serializer_action_classes = {
#         'create': UpdateUserSerializer
#     }
#     http_method_names = ('post', )
#     model = Account
#     queryset = Account.objects.all()
#     permission_classes = (IsAuthenticated, )
#
#     def get_object(self) -> Account:
#         return self.request.user
#
#     @swagger_auto_schema(responses={
#         400: validation_error,
#         401: un_auth,
#         403: un_auth,
#         451: user_in_blacklist_error,
#         500: server_error})
#     def create(self, request, *args, **kwargs):
#         """
#         Нужно в заголовках отправлять токен пользователя, который был получен в api /token [POST]
#         """
#         if request.user.in_blacklist:
#             return Response({
#                 'detail': 'Error: You in blacklist'
#             }, status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)
#         resp = super().update(request, *args, **kwargs)
#         resp.status_code = status.HTTP_201_CREATED
#         return resp

