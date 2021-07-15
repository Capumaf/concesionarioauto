from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginHenryForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=request, *args, **kwargs)
