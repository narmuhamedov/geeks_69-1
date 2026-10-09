from django import forms
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm

GENDER = (
        ('M', 'M'),
        ('Ж', 'Ж')
    )

class CustomRegisterForm(UserCreationForm):
    photo = forms.ImageField(required=True)
    email = forms.EmailField(required=True, initial='@gmail.com')
    phone_number = forms.CharField(max_length=15, required=True, initial="+996")
    gender = forms.ChoiceField(required=True, choices=GENDER)

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'photo',
            'password1',
            'password2',
            'email',
            'first_name',
            'phone_number',
            'gender'
        )

        def save(self, commit=True):
            user = super(CustomRegisterForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user