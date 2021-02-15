# serializers.py

# In this file, we need to:
# Import the User model
# Import the REST Framework serializer
# Create a new class that links the Hero with its serializer


from rest_framework import serializers

from .models import Profile
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'image_url')
    
    def get_image_url(self, User):
        print(User.profile.image)
        return str(User.profile.image)