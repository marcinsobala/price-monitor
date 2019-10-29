from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Adres e-mail')

    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password1',
                  'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='Adres e-mail')

    class Meta:
        model = User
        fields = ['username',
                  'email']


class CustomLoginForm(AuthenticationForm):
    """Had to subclass it because of some ugly form stretching."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'username',
            'password',
            Submit('submit', u'Zaloguj', css_class='btn btn-primary'),
            HTML("""<small class="text-muted ml-2">
                        <a href="{% url 'password_reset' %}">Zapomniałeś hasła?</a>
                    </small>"""))
