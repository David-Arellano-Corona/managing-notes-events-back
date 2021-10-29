from datetime import date
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Users
from commons.HTTPMethods import HTTPMethod

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email','name','lastname','nickname','password','gender','date_of_birth','is_active']
        
        
        
        extra_kwargs = {
            "is_active":{
                "read_only":True
            },
            "password":{
                "write_only":True
            },
            "email":{
                "validators":[
                    UniqueValidator(
                        queryset=Users.objects.all(),
                        message="El correo electrónico ya se encuentra en uso"
                    )
                ]
            },
            "date_of_birth":{
                "error_messages":{
                    "invalid":"Formato de fecha incorrecto, intente con YYYY-MM-DD"
                }
            }
        }


    def validate_nickname(self, value):
        user = Users.objects.filter(nickname=value)
        method = self.context.get("request").method
        
        if method == HTTPMethod.POST.name and user.exists():
            raise serializers.ValidationError("El alias ya se encuentra en uso")
        
        if method == HTTPMethod.PUT.name or method == HTTPMethod.PATCH.name:
            pk = int(self.context.get("request").parser_context['kwargs']['pk'])
            if user.exists() and  (pk != user[0].pk):
                raise serializers.ValidationError("El alias ya se encuentra en uso")   
        
        return value

    def validate_date_of_birth(self, value):
        if value >= date.today():
            raise serializers.ValidationError("La fecha de cumpleaños debe ser menor a la fecha actual")
        return value    


    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        kwargs = validated_data
        del kwargs['email']
        del kwargs['password']
        print(kwargs)
        user = Users.objects.create_user(
            email,
            password,
            **kwargs
        )
        return user 

    def to_representation(self, instance):
        return {
            "email":instance.email or "",
            "name":instance.name or "",
            "lastname":instance.lastname or "",
            "nickname":instance.nickname or "",
            "gender": instance.gender or "",
            "date_of_birth": instance.date_of_birth or "",
            "is_active": instance.is_active or False
        }           



class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users        
        fields = ['email','nickname','password']
        extra_kwargs={
            'email':{
                'validators':[
                    UniqueValidator(
                        queryset=Users.objects.all(),
                        message="El correo electrónico ya se encuentra en uso"
                    )
                ],
                'error_messages':{
                    'blank':'Email es un campo obligatorio'
                }
            },
            'nickname':{
                'validators':[
                    UniqueValidator(
                        queryset=Users.objects.all(),
                        message="El alias ya se encuentra en uso"
                    )
                ],
                'error_messages':{
                    'blank':"Nombre de usuario es un campo obligatorio"
                }
            },
            'password':{
                'error_messages':{
                    "blank":"Contraseña es un campo obligatorio"
                }
            }
        }

    def validate_nickname(self, value):
        user = Users.objects.filter(nickname=value)
        method = self.context.get("request").method
        
        if method == HTTPMethod.POST.name and user.exists():
            raise serializers.ValidationError("El alias ya se encuentra en uso")
        
        if method == HTTPMethod.PUT.name or method == HTTPMethod.PATCH.name:
            pk = int(self.context.get("request").parser_context['kwargs']['pk'])
            if user.exists() and  (pk != user[0].pk):
                raise serializers.ValidationError("El alias ya se encuentra en uso")   
        
        return value 

    def create(self, validated_data):
        email = validated_data['email']   
        password = validated_data['password']
        kwargs = validated_data
        del kwargs['email']
        del kwargs['password']
        user = Users.objects.create_user(
            email,
            password,
            **kwargs
        ) 
        return user


