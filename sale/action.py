from sale import models


def update_sale_prince_item():
    sale_item_list = models.SaleItem.objects.all()

    for sale_item in sale_item_list:
        sale_item.sale_price = sale_item.product.sale_price
        sale_item.save()
