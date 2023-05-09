from django.db import migrations
from django.contrib.auth.models import Group, Permission

class Migration(migrations.Migration):
    dependencies = [
        ('inventory', '0002_alter_product_image'),
    ]
