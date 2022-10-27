from . models import MyCartItem


def cart_count(request):
    count = 0
    if request.user.is_authenticated:
        cart_item = MyCartItem.objects.filter(user=request.user)
        count = cart_item.count()
    return dict(count=count)