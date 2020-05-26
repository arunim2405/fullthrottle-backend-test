from rest_framework import serializers
from backend.models import User,ActivityPeriod

# Lead Serializer
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    

class ActivityPeriodSerializer(serializers.ModelSerializer):
  class Meta:
    model=ActivityPeriod
    fields = ('start_time', 'end_time')
    