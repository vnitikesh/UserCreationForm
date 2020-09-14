from django.test import TestCase
from django.urls import resolve, reverse
from .views import signup
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your tests here.
class SignUpTests(TestCase):
    def setUp(self):
        url = reverse('singup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/')
        self.assertEquals(view.func, signup)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form,UserCreationForm)


class SuccessfulSignUpTests(TestCase):
    def setUp(self):
        url = reverse('singup')
        data = {
        'username': 'john',
        'password1': 'abcdef1234',
        'password2': 'abcdef1234'
        }
        self.response = self.client.post(url,data)
        self.login_url = reverse('login')

    def test_redirection(self):
        self.assertRedirects(self.response, self.login_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authenticated(self):
        response = self.client.get(self.login_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)
