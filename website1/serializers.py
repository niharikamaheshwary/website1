from rest_framework import serializers
from .models import Team, Members

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields=('name','ids')

class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields='__all__'