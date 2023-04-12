from django.db import migrations
from django.contrib.auth.models import Group, Permission


def create_objects(apps, schema_editor):
    # Create INVENTORY group
    inventory_group = Group(name='INVENTORY')
    inventory_group.save()

    # Get permissions for adding, changing and deleting Inventory
    app_label = 'inventory'
    model_name = 'inventory'
    add_permission = Permission.objects.get(codename=f'add_{model_name}', content_type__app_label=app_label)
    change_permission = Permission.objects.get(codename=f'change_{model_name}', content_type__app_label=app_label)
    delete_permission = Permission.objects.get(codename=f'delete_{model_name}', content_type__app_label=app_label)

    # Assign permissions to the group
    inventory_group.permissions.add(add_permission, change_permission, delete_permission)
    inventory_group.save()

    # Get permissions for adding, changing and deleting Inventory
    app_label = 'inventory'
    model_name = 'category'
    add_permission = Permission.objects.get(codename=f'add_{model_name}', content_type__app_label=app_label)
    change_permission = Permission.objects.get(codename=f'change_{model_name}', content_type__app_label=app_label)
    delete_permission = Permission.objects.get(codename=f'delete_{model_name}', content_type__app_label=app_label)

    # Assign permissions to the group
    inventory_group.permissions.add(add_permission, change_permission, delete_permission)
    inventory_group.save()


class Migration(migrations.Migration):
    dependencies = [
        ('inventory', '0002_alter_product_image'),
    ]

    operations = [
        migrations.RunPython(create_objects)
    ]
