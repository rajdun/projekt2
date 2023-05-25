from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from accounts.models import Address
from .models import Order, OrderStatus


class OrdersTestCase(TestCase):
    def setUp(self):
        # Create a client instance
        self.client = Client()

        # Create a test user
        self.test_user1 = User.objects.create_user(username='testuser1', password='testpassword1')

        # Create order statuses
        self.status1 = OrderStatus.objects.create(name='Pending')
        self.status2 = OrderStatus.objects.create(name='Shipped')

        # create addresses
        self.address = Address.objects.create(address_line_1='Test Address Line 1', address_line_2='Test Address Line 2', city='Test City', zip_code='12345', country='Test Country')
        self.address2 = Address.objects.create(address_line_1='Test Address Line 1', address_line_2='Test Address Line 2', city='Test City', zip_code='12345', country='Test Country')

        # Create orders for the user
        self.order1 = Order.objects.create(user=self.test_user1, status=self.status1, address=self.address)
        self.order2 = Order.objects.create(user=self.test_user1, status=self.status2, address=self.address2)

        # Define URL for orders_list view
        self.orders_list_url = reverse('orders_list')

    def test_orders_list_GET(self):
        # Login the user
        self.client.login(username='testuser1', password='testpassword1')

        # Send a GET request to the orders_list view
        response = self.client.get(self.orders_list_url)

        # Check that the response has a status code of 200 (OK)
        self.assertEquals(response.status_code, 200)

        # Check that the response contains the orders for the user
        self.assertTrue('orders' in response.context)
        self.assertEqual(list(response.context['orders']), [self.order1, self.order2])

    def test_orders_list_filter_GET(self):
        # Login the user
        self.client.login(username='testuser1', password='testpassword1')

        # Send a GET request with the status filter
        response = self.client.get(self.orders_list_url, {'status': 'Shipped'})

        # Check that the response has a status code of 200 (OK)
        self.assertEquals(response.status_code, 200)

        # Check that the response contains the filtered orders for the user
        self.assertTrue('orders' in response.context)
        self.assertEqual(list(response.context['orders']), [self.order2])
