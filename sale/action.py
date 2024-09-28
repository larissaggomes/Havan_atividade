from sale import models
from django.db.models import F


def update_sale_prince_item():
    sale_item_list = models.SaleItem.objects.select_related(
        'product',
        'product__product_group'
    ).all()

    print(sale_item_list.query)

    for sale_item in sale_item_list:
        print(sale_item.product.product_group.name)
        sale_item.sale_price = sale_item.product.sale_price
        sale_item.save()
