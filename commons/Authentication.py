import jwt
import configparser
from jwt.exceptions import ExpiredSignatureError
from rest_framework import (
    exceptions,authentication
)
from .exceptions import (
    AuthenticationException,UserNotFoundException, JWTExpired
)
from applications.users.models import Users

config = configparser.ConfigParser()
config.read('config.ini')

class Authentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        bearertoken = request.META.get('HTTP_AUTHORIZATION')
        
        if bearertoken == None:
            raise AuthenticationException()

        token = bearertoken.split(" ").pop()
        if token == "":
            raise AuthenticationException()

        key = config['DEFAULT']['JWT_KEY']
        try:
            payload = jwt.decode(token, key, algorithms=["HS256"]) 
            user = Users.objects.filter(id=payload['user_id'])
            if not user.exists():
                raise UserNotFoundException()
            user.is_authenticated = True
        except ExpiredSignatureError:
            raise JWTExpired()
        
        return (user[0], None)
