from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import  TokenObtainPairView

class JWTClaimsSerializers(TokenObtainPairSerializer):

    default_error_messages = {
        'no_active_account':"La cuenta no se encuentra registrada o fue dada de baja"
    }

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['nickname'] = user.nickname
        token['name'] = user.name
        token['lastname'] = user.lastname
        return token

class JWTClaimsView(TokenObtainPairView):
    serializer_class = JWTClaimsSerializers
         