from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import RegisteredUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = RegisteredUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = RegisteredUser
        fields = ('email',)
