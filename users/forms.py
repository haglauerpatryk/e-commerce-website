from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile, COUNTRIES

class UserForm(UserCreationForm):
    '''
    Form that uses built-in UserCreationForm to handel user creation.

    password1 and password2 are inherited from UserCreationForm.
    username isn't within UserCreationForm, so we add it here.
    '''
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput())

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted text-center"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted text-center"><small>Enter the same password as before, for verification.</small></span>'



class AuthForm(AuthenticationForm):
    '''
    Form that uses built-in AuthenticationForm to handel user auth.

    username, even though it is included within AuthenticationForm, we add it here,
    to make it consistent with UserForm.
    '''
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput())

    class Meta:
        model = User
        fields = ('username','password')

    def __init__(self, *args, **kwargs):
        super(AuthForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''

        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].label = ''



class UserProfileForm(forms.ModelForm):
    '''
    Basic model-form for our user profile
    '''
    avatar = forms.ImageField(required=False)
    telephone = forms.CharField(max_length=255, required=False, widget=forms.TextInput())
    address = forms.CharField(max_length=100, required=False, widget=forms.TextInput())
    town = forms.CharField(max_length=100, required=False, widget=forms.TextInput())
    county = forms.CharField(max_length=100, required=False, widget=forms.TextInput())
    post_code = forms.CharField(max_length=8, required=False, widget=forms.TextInput())
    country = forms.CharField(max_length=100, required=False, widget=forms.Select(choices=COUNTRIES))
	
    class Meta:
        model = UserProfile
        fields = ( 'avatar', 'telephone', 'address', 'town', 'county', 'post_code', 'country')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserAlterationForm(forms.ModelForm):
    '''
    Basic model-form for our user
    '''
    first_name = forms.CharField(max_length=150, required=True, widget=forms.TextInput())
    last_name = forms.CharField(max_length=150, required=True, widget=forms.TextInput())
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput())
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserAlterationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'