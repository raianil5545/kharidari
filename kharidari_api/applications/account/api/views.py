from rest_framework.generics import CreateAPIView, GenericAPIView
from ..models import User
from .serializer import UserRegistrationSerializer, UserLoginSerializer
from rest_framework import status,permissions
from django.contrib.auth import authenticate, login, get_user_model
from rest_framework import status
from rest_framework.response import Response




class CreateUserView(CreateAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()


class UserLoginView(GenericAPIView):
    serializer_class = UserLoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        User = get_user_model()
        user = User.objects.get(email=data['email'])
        if not user:
            return Response({'message': 'User not registered'}, status=status.HTTP_401_UNAUTHORIZED)
        auth_user = authenticate(request, email=data['email'], password=data['password'])
        if user is not None:
            login(request, user)
            return Response({'message': 'Login Successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    