from django.test import TestCase, Client, TransactionTestCase
from django.contrib.auth.models import User
from .models import Cart, CartItem
from orders.models import Order, OrderStatus, OrderItem
from accounts.models import Profile, Address
from inventory.models import Inventory, Product, Category


class TestCartViews(TransactionTestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('testuser1', 'testemail@test.com', 'testpassword1')
        self.address1 = Address.objects.create(address_line_1='Test Address Line 1', address_line_2='Test Address Line 2', city='Test City', zip_code='12345', country='Test Country')
        self.profile1 = Profile.objects.create(user=self.user1, phone_number='1234567890', default_address=self.address1)
        self.cart1 = Cart.objects.create(user=self.user1)
        self.category1 = Category.objects.create(name='Test Category')
        self.product1 = Product.objects.create(name='Test Product', price=10, category=self.category1)
        self.order_status1 = OrderStatus.objects.create(name='Test Order Status')
        Inventory.objects.filter(product=self.product1).delete()
        self.inventory1 = Inventory.objects.create(product=self.product1, quantity=10)
        self.cart_item1 = CartItem.objects.create(cart=self.cart1, product=self.product1, quantity=2)

    def tearDown(self):
        self.cart_item1.delete()
        self.inventory1.delete()
        self.product1.delete()
        self.order_status1.delete()
        self.category1.delete()
        self.cart1.delete()
        self.profile1.delete()
        self.address1.delete()
        self.user1.delete()

    def test_cart_GET(self):
        self.client.login(username='testuser1', password='testpassword1')
        response = self.client.get('/cart/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_buy_cart_POST(self):
        self.client.login(username='testuser1', password='testpassword1')
        response = self.client.post('/buy/')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(OrderItem.objects.count(), 1)
