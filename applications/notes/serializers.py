from rest_framework import serializers
from .models import Notes


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['text','owner','id','isStore']
        extra_kwargs = {
            "owner":{
                "read_only":True
            },
            "id":{
                "read_only":True
            }
        }

    def create(self, validated_data):
        user = self.context.get('request').user
        
        note = Notes.objects.create(owner=user, text = validated_data.get('text'))
        return note    

class NotesStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id','isStore']
        extra_kwargs = {
            'id':{
                'read_only':True
            }
        }        

class NotesUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['text', 'id']
        extra_kwargs = {
            'id':{
                'read_only':True
            }
        }         