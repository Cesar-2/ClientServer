from rest_framework import serializers
from to_do.models import Card, Task, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Card
        fields = ['user']

    def get_user(self, obj):
        return User.objects.filter(id=obj.id)


class TaskSerializer(serializers.ModelSerializer):
    card = CardSerializer()

    class Meta:
        model = Task
        fields = ['task', 'card', 'is_completed', 'is_active']

    def get_card(self, obj):
        return Card.objects.filter(card=obj.id)
