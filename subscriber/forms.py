from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from .models import Subscriber, NextOfKin


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            '__all__',
            ButtonHolder(
                Submit('register', 'Register', css_class='btn-primary')
            )
        )


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            ButtonHolder(
                Submit('login', 'Login', css_class='btn btn-info btn-round btn-lg btn-block')
            )
        )


class BioDataForm(UserCreationForm):
    class Meta:
        model = Subscriber
        fields = (
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
            'gender',
            'date_of_birth',
            'state_of_origin',
            'occupation',
            'address',
            'local_government',
            'nationality',
            'image',
        )

    def __init__(self, *args, **kwargs):
        super(BioDataForm, self).__init__(*args, **kwargs)

        self.form_name = 'bio_data_form'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
            'gender',
            'date_of_birth',
            'state_of_origin',
            'occupation',
            'address',
            'local_government',
            'nationality',
            'image',

            ButtonHolder(
                Submit('register bio data', 'Register bio data', css_class='btn-primary')
            )
        )


class NextOfKinForm(forms.ModelForm):
    class Meta:
        model = NextOfKin
        fields = (
            'referrer',
            'first_name',
            'last_name',
            'gender',
            'relationship',
            'address',
            'phone_number',
        )

    def __init__(self, *args, **kwargs):
        super(NextOfKinForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'referrer',
            'first_name',
            'last_name',
            'gender',
            'relationship',
            'address',
            'phone_number',

            ButtonHolder(
                Submit('register next of kin', 'Register next of kin', css_class='btn-primary')
            )
        )


class BioDataUpdateForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'gender',
            'date_of_birth',
            'state_of_origin',
            'occupation',
            'address',
            'local_government',
            'nationality',
            'image',
        )

    def __init__(self, *args, **kwargs):
        super(BioDataUpdateForm, self).__init__(*args, **kwargs)

        self.form_name = 'bio_data_form'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'first_name',
            'last_name',
            'email',
            'gender',
            'date_of_birth',
            'state_of_origin',
            'occupation',
            'address',
            'local_government',
            'nationality',
            'image',

            ButtonHolder(
                Submit('update bio data', 'Update bio data', css_class='btn-primary')
            )
        )


class NextOfKinUpdateForm(forms.ModelForm):
    class Meta:
        model = NextOfKin
        fields = (
            'first_name',
            'last_name',
            'gender',
            'relationship',
            'address',
            'phone_number',
        )

    def __init__(self, *args, **kwargs):
        super(NextOfKinUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'gender',
            'relationship',
            'address',
            'phone_number',

            ButtonHolder(
                Submit('update next of kin', 'update next of kin', css_class='btn-primary')
            )
        )
class ImageUploadForm(forms.ModelForm):
    """Image upload form."""
    image = forms.ImageField()