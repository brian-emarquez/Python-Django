from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import ensure_csrf_cookie
from accounts.serializers import UserSerializer
from accounts.utils import generate_access_token, generate_refresh_token

# Create your views here.

@api_view(['GET'])
def profile(request):
    user = request.user
    serialized_user = UserSerializer(user).data
    return Response({'user': serialized_user })

@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def login_view(request):
    User = get_user_model()
    username = request.data.get('username')
    password = request.data.get('password')
    response = Response()
    if (username is None) or (password is None):
        raise exceptions.AuthenticationFailed(
            'username and password required')

    user = User.objects.filter(username=username).first()
    if(user is None):
        raise exceptions.AuthenticationFailed('user not found')
    if (not user.check_password(password)):
        raise exceptions.AuthenticationFailed('wrong password')

    serialized_user = UserSerializer(user).data
    print(",,,,,")

    access_token = generate_access_token(user)
    print(">>>", access_token)
    refresh_token = generate_refresh_token(user)
    print("<<<", refresh_token)

    response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
    response.data = {
        'access_token': access_token,
        'user': serialized_user,
    }

    return response