def can_manage_inventory(user):
    return user.groups.filter(name='INVENTORY').exists()
