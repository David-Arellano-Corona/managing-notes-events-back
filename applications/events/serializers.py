from rest_framework import serializers
from .models import Events

class EventSerializer(serializers.ModelSerializer):
    userId = serializers.IntegerField(source="owner.id", read_only=True)
    username = serializers.CharField(source="owner.full_name", read_only=True)
    class Meta:
        model = Events
        fields = ['id','name','description','starttime','endtime','owner', 'userId', 'username']
        extra_kwargs = {
            'id':{
                'read_only':True
            },
            'owner':{
                'write_only':True
            },
            'userId':{
                'read_only':True
            },
            'username':{
                'read_only':True
            }
        }