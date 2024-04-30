from django.test import TestCase
from django.contrib.auth.models import User
from ..forms import UserForm, AuthForm, UserProfileForm, UserAlterationForm

class TestManager(TestCase):
    tested_object = None

    def _test_form(self, case, **kwargs):
        if case == True:
            form = self.tested_object(data=kwargs)
            self.assertTrue(form.is_valid())
        elif case == False:
            form = self.tested_object(data=kwargs)
            self.assertFalse(form.is_valid())

    def _test_form_missing_or_invalid(self, case, missing_value, **kwargs):
        if case == True:
            form = self.tested_object(data=kwargs)
            self.assertTrue(form.is_valid())
            self.assertIn(missing_value, form.errors.keys())
        elif case == False:
            form = self.tested_object(data=kwargs)
            self.assertFalse(form.is_valid())
            self.assertIn(missing_value, form.errors.keys())

class UserFormTest(TestManager):
    tested_object = UserForm

    def test_valid(self):
        self._test_form(True, 
        username='testuser', 
        password1='testpassword123', 
        password2='testpassword123'
        )

    def test_missing_username(self):
        self._test_form_missing_or_invalid(False, 'username',
        password1='testpassword123', 
        password2='testpassword123'
        )

    def test_invalid_password(self):
        self._test_form_missing_or_invalid(False, 'password2',
        username='testuser', 
        password1='testpassword123', 
        password2='testpassword321'
        )

class AuthFormTest(TestManager):
    tested_object = AuthForm

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword123')

    def test_valid(self):
        self._test_form(True, 
        username='testuser', 
        password='testpassword123'
        )

class UserProfileFormTest(TestManager):
    def test_user_profile_form_valid_data(self):
        form = UserProfileForm(data={
            'telephone': '123456789',
            'address': 'Test Address',
            'town': 'Test Town',
            'county': 'Test County',
            'post_code': '12345',
            'country': 'Poland'
        })
        self.assertTrue(form.is_valid())

class UserAlterationFormTest(TestManager):
    def test_user_alteration_form_valid_data(self):
        user = User.objects.create_user(username='testuser', password='testpassword123')
        form = UserAlterationForm(instance=user, data={
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com'
        })
        self.assertTrue(form.is_valid())
