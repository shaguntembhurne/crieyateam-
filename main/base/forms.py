from django.contrib.auth.forms import UserCreationForm
from .models import CustomerClass

class CustomerForm(UserCreationForm):
    class Meta:
        model = CustomerClass
        fields = ('email','username','password1','password2')