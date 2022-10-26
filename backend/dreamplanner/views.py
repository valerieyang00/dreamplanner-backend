from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .serializers import DestinationSerializer
from .serializers import ExpenseSerializer
from .models import User
from .models import Destination
from .models import Expense

# Create your views here.

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class DestinationView(viewsets.ModelViewSet):
    serializer_class = DestinationSerializer
    queryset = Destination.objects.all()

class ExpenseView(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
# Create your views here.
