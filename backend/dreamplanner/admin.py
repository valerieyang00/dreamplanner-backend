from django.contrib import admin
from .models import User
from .models import Destination
from .models import Expense

# Register your models here.

admin.site.register(User)
admin.site.register(Destination)
admin.site.register(Expense)