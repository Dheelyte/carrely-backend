from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import CustomUser, Profile


class RegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'name',
            'password',
        ]

    def create(self, validated_data):
        profile_data = {
            'name': validated_data.pop('name'),
        }
        user = CustomUser.objects.create_user(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(request=self.context.get('request'), email=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid email or password.")
        
        attrs['user'] = user
        return attrs


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name',)

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'profile',)
