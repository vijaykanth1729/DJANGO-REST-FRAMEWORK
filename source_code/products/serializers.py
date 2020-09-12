from .models import Product,Animal, Movie
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name','quantity','available','description')

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username', '')
        password = data.get('password', '')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise ValidationError("User is Deactivated!")
            else:
                raise ValidationError("Unable to proceed login with given credentials.")
        else:
            raise ValidationError("Must provide username and password!")
        return data
