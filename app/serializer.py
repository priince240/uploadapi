from rest_framework import serializers
from .models import uploads
from .models import User
class uploads_serializer(serializers.ModelSerializer):
    class Meta:
        model = uploads
        fields=['id','file','name','date']

class registerapi(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"},write_only=True)
    class Meta:
        model=User
        fields=['email','name','password','password2']
        
    
    def validate(self, data):
        password=data.get('password')
        password2=data.get('password2')
        if password != password2:
            raise serializers.ValidationError("Passwords don't match")
        return data
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class loginapi(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=User
        fields=('email','password')



# fetch user data    
# class get_api(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=('id','email','name')  
      
        
        
    



        