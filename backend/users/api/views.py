from rest_framework.generics import GenericAPIView 
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer
from rest_framework import status
from rest_framework.generics import GenericAPIView,RetrieveUpdateAPIView
from .serializers import (
    UserRegistrationSerializer,
    LoginSerializer,
    UserDetailSerializer,

)


class UserRegistrationView(GenericAPIView):
    serializer_class = UserRegistrationSerializer
    authentication_classes=[]
    permission_classes=[]
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create_user()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'first_name':user.first_name 
                         ,'last_name':user.last_name ,
                            'username': user.username,
                            'email': user.email,
                        },
                        status=status.HTTP_201_CREATED)
    

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.authenticate()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'key':token.key,'detail': UserDetailSerializer(user).data}, status=status.HTTP_200_OK)


class UserDetailView(RetrieveUpdateAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = []

    def get_object(self):
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)