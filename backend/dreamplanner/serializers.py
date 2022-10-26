from rest_framework import serializers
from .models import User
from .models import Destination
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"

class DestinationSerializer(serializers.ModelSerializer):
    # expenses = ExpenseSerializer(many=True)

    class Meta:
        model = Destination
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    # destinations = DestinationSerializer(many=True)
    # expenses = ExpenseSerializer(many=True)

    class Meta:
        model = User
        fields = "__all__"