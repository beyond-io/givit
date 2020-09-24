from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
            "email",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class PersonInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'student_id',
            'phone_number',
            'gender',
            'date_of_birth',
            'address_street_name',
            'address_house_number',
            'address_city',
            'field_of_study',
            'degree',
            'scholarship',
            'membership_type',
        ]
