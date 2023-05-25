from django.test import TestCase, Client
from django.contrib.auth.models import User
from accounts.models import Profile, UserAddressHistory, Address
from accounts.forms import ProfileEditForm, AddressEditForm

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user('testuser1', 'testemail@test.com', 'testpassword1')
        self.address1 = Address.objects.create(address_line_1='Test Address Line 1', address_line_2='Test Address Line 2', city='Test City', zip_code='12345', country='Test Country')
        self.profile1 = Profile.objects.create(user=self.user1, phone_number='1234567890', default_address=self.address1)
        self.history1 = UserAddressHistory.objects.create(user=self.user1, address=self.address1)

    def test_edit_profile_GET(self):
        self.client.login(username='testuser1', password='testpassword1')
        response = self.client.get('/account/edit/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/edit_profile.html')

    def test_edit_profile_POST(self):
        self.client.login(username='testuser1', password='testpassword1')
        response = self.client.post('/account/edit/', {
            'phone_number': '0987654321',
            'profile_picture': '',
            'address_line_1': 'Updated Test Address Line 1',
            'address_line_2': 'Updated Test Address Line 2',
            'city': 'Updated Test City',
            'zip_code': '54321',
            'country': 'Updated Test Country'
        })

        self.assertEqual(response.status_code, 302)

    def test_login_view_GET(self):
        response = self.client.get('/account/login/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_login_view_POST(self):
        response = self.client.post('/account/login/', {
            'username': 'testuser1',
            'password': 'testpassword1'
        })

        self.assertEqual(response.status_code, 302)

    def test_register_view_GET(self):
        response = self.client.get('/account/register/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_register_view_POST(self):
        response = self.client.post('/account/register/', {
            'username': 'testuser2',
            'password1': 'testpassword2',
            'password2': 'testpassword2'
        })

        self.assertEqual(response.status_code, 302)

    def test_logout_view(self):
        self.client.login(username='testuser1', password='testpassword1')
        response = self.client.get('/account/logout/')

        self.assertEqual(response.status_code, 302)
