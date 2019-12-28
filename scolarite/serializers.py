from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""

    name=serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects ."""

    class Meta :
        model = models.UserProfile
        fields= ('id' , 'name' , 'email', 'password','label')
        extra_kwargs = {'password' : {'write_only' :True}}

    def create(self, validated_data):
        """Create and return a new user ."""

        user = models.UserProfile(
            email= validated_data['email'] ,
            name = validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
class VerificationSerializer(serializers.ModelSerializer):

     class Meta :
       model = models.Verification
       field = ('matricule')
class SaisirNote(serializers.ModelSerializer):
    """saisir la note """




class ProfileFeedItemSerializer(serializers.ModelSerializer):
     """A serializer for profile feed items."""

     class Meta :
         model = models.ProfileFeedItem
         fields = ('id' , 'user_profile' , 'status_text' , 'created_on')
         extra_kwargs = {'user_profile': {'read_only' : True}}