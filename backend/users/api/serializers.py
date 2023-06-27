from rest_framework import serializers
from django.db.models import Q
from django.contrib.auth import authenticate, password_validation,login
from django.contrib.auth import get_user_model
User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=128)
    last_name = serializers.CharField(max_length=128)
    email = serializers.EmailField(max_length=32)   
    password = serializers.CharField(validators=[password_validation.validate_password],
                                     style={'input_type': 'password'})
    confirm_password = serializers.CharField(style={'input_type': 'password'})


    def validate(self,value):
        password = value.get('password')
        confirm_password = value.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Password not matched")
        return value

    def validate_email(self, value):
        value = value.strip()
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value


    def create_user(self):
        first_name = self.data.get('first_name')
        last_name = self.data.get('last_name')
        email = self.data.get('email')
        password = self.data.get('password')
        phone_number = self.data.get('phone_number')

        user = User.objects.create_user(
            first_name=first_name, last_name=last_name,
            username=email,email=email,password=password ,
            phone_number = phone_number    
        )
        user.save()
        return (user)

    class Meta:
        model = User
        fields = (
        'first_name','last_name','email','password', 'confirm_password',
        'phone_number',
        )

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})


    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
       
        try:
            user = User.objects.get(Q(username__iexact=email) | Q(email__iexact=email))
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid Credentials')

        user = authenticate(username=user.username, password=password)
        if not user:
            raise serializers.ValidationError('Invalid Credentials')
        return attrs


    def authenticate(self):
        email = self.data.get('email')
        password = self.data.get('password')
        user = User.objects.get(Q(username__iexact=email) | Q(email__iexact=email))
        user = authenticate(username=user.username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid email or password")
        login(self.context.get('request'), user)
        return (user)


class UserDetailSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = (
            'pk', 'email', 'first_name', 'last_name',  
            'phone_number' ,'verified' 
        )
        read_only_fields = ('email','username')