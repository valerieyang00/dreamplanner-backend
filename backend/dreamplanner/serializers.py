from rest_framework import serializers
from .models import User
from .models import Destination
from .models import Expense
from django.contrib.auth.hashers import make_password

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"

class DestinationSerializer(serializers.ModelSerializer):
    expenses = ExpenseSerializer(many=True, required=False)

    class Meta:
        model = Destination
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    destinations = DestinationSerializer(many=True, required=False)
    # expenses = ExpenseSerializer(many=True, required=False)
    def validate_password(self, value: str) -> str:
        return make_password(value)
    class Meta:
        model = User
        fields = "__all__"