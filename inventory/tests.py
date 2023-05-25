from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.contrib.auth.models import User, Group
from django.urls import reverse
from orders.models import Product, Order, OrderItem, OrderStatus
from accounts.models import Profile, Address
from inventory.models import Category, Inventory
from cart.models import Cart, CartItem
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

def create_test_image():
    file = BytesIO()
    image = Image.new('RGBA', size=(50, 50), color=(155, 0, 0))
    image.save(file, 'png')
    file.name = 'test_image.png'
    file.seek(0)
    return file

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.inventory_manager_group = Group.objects.create(name='INVENTORY')
        self.user.groups.add(self.inventory_manager_group)
        self.category = Category.objects.create(name='Test Category')
        dummy_image = SimpleUploadedFile(name='test_image.jpg', content=b"\x00\x01\x02\x03", content_type='image/jpeg')
        self.product = Product.objects.create(name='Test Product', price=10, category=self.category, image=dummy_image)
        Inventory.objects.filter(product=self.product).delete()
        self.inventory = Inventory.objects.create(product=self.product, quantity=10)
        self.address = Address.objects.create(address_line_1='Test Address Line 1', address_line_2='Test Address Line 2', city='Test City', zip_code='12345', country='Test Country')
        self.profile = Profile.objects.create(user=self.user, phone_number='1234567890', default_address=self.address, amount=100)
        self.cart = Cart.objects.create(user=self.user)
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)

        self.add_product_url = reverse('add_product')
        self.products_list_url = reverse('products_list')
        self.buy_now_url = reverse('add_to_cart_or_buy')

    def tearDown(self):
        User.objects.all().delete()
        Category.objects.all().delete()
        Product.objects.all().delete()
        Inventory.objects.all().delete()
        Address.objects.all().delete()
        Profile.objects.all().delete()
        Cart.objects.all().delete()
        CartItem.objects.all().delete()

    def test_add_product_POST(self):
        self.client.login(username='testuser', password='testpass')
        dummy_image = SimpleUploadedFile(name='test_image.jpg', content=b"\x00\x01\x02\x03", content_type='image/jpeg')
        response = self.client.post(self.add_product_url, {
            'name': 'New Test Product',
            'description': 'This is a test product',
            'price': 15,
            'category': self.category.id,
            'image': dummy_image
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Product.objects.last().name, 'New Test Product')

    def test_products_list_GET(self):
        response = self.client.get(self.products_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/products_list.html')

    def test_add_product_POST(self):
        self.client.login(username='testuser', password='testpass')
        test_image = create_test_image()
        image_upload_file = InMemoryUploadedFile(test_image, None, 'test_image.png', 'image/png', test_image.tell, None)
        response = self.client.post(self.add_product_url, {
            'name': 'New Test Product',
            'description': 'This is a test product',
            'price': 15,
            'category': self.category.id,
            'image': image_upload_file
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Product.objects.last().name, 'New Test Product')
