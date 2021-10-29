from rest_framework.exceptions import APIException

class AuthenticationException(APIException):
    status_code = 401
    default_detail = "Credenciales de autenticación no proporcionadas"
    default_code  = "unauthorized_error"

class UserNotFoundException(APIException):
    status_code = 404
    default_detail = "La cuenta no se encuentra registrada o ha sido dada de baja" 
    default_code = "account_not_found"   

class JWTExpired(APIException):
    status_code=400
    default_detail = "La vigencia del token ha expirado"
    default_code = "jwt_expirated"    

class Forbidden(APIException):
    status_code=403
    default_detail="No tienes permisos suficientes para ver este recurso"
    default_code="forbidden_error"