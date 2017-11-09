from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

from .models import RegisteredSims


class SimForm(forms.ModelForm):
    class Meta:
        model = RegisteredSims
        fields = (
            'owner',
            'phone_number',
            'mobile_network',
        )

    def __init__(self, *args, **kwargs):
        super(SimForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'owner',
            'phone_number',
            'mobile_network',

            ButtonHolder(
                Submit('register', 'Register', css_class='btn-primary')
            )
        )


class SimUpdateForm(forms.ModelForm):
    class Meta:
        model = RegisteredSims
        fields = (
            'phone_number',
            'mobile_network',
        )

    def __init__(self, *args, **kwargs):
        super(SimUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'phone_number',
            'mobile_network',

            ButtonHolder(
                Submit('register', 'Register', css_class='btn-primary')
            )
        )
