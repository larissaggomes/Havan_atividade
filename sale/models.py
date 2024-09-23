from django.db import models


# Create your models here.
class ModelBase(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    modified_at = models.DateTimeField(auto_now=True, null=False)
    active = models.BooleanField(default=True, null=False)

    class Meta:
        managed = True
        abstract = True


class Department(ModelBase):
    name = models.CharField(max_length=64, null=False)

    class Meta:
        db_table = 'department'


class MaritalStatus(ModelBase):
    name = models.CharField(max_length=64, null=False)

    class Meta:
        db_table = 'marital_status'


class State(ModelBase):
    name = models.CharField(max_length=64, null=False)
    abbreviation = models.CharField(max_length=2, null=False)

    class Meta:
        db_table = 'state'


class City(ModelBase):
    name = models.CharField(max_length=64, null=False)
    state = models.ForeignKey(
        to='State',
        on_delete=models.DO_NOTHING,
        db_column='id_state',
        null=False,
    )

    class Meta:
        db_table = 'city'


class Zone(ModelBase):
    name = models.CharField(max_length=64, null=False)
    state = models.ForeignKey(
        to='State',
        on_delete=models.DO_NOTHING,
        db_column='id_state',
        null=False,
    )

    class Meta:
        db_table = 'zone'


class Employee(ModelBase):
    name = models.CharField(max_length=64, null=False)
    department = models.ForeignKey(
        to='Department',
        on_delete=models.DO_NOTHING,
        db_column='id_department',
        null=False,
    )

    class Meta:
        db_table = 'employee'


class Customer(ModelBase):
    class Gender(models.TextChoices):
        MALE = 'M'
        FEMALE = 'F'

    name = models.CharField(max_length=64, null=False)
    income = models.DecimalField(max_digits=16, decimal_places=2, null=False)
    gender = models.CharField(max_length=1, null=False, choices=Gender.choices)

    class Meta:
        db_table = 'customer'


class District(ModelBase):
    name = models.CharField(max_length=64, null=False)
    zone = models.ForeignKey(
        to='Zone',
        on_delete=models.DO_NOTHING,
        db_column='id_zone',
        null=False,
    )
    city = models.ForeignKey(
        to='City',
        on_delete=models.DO_NOTHING,
        db_column='id_city',
        null=False,
    )

    class Meta:
        db_table = 'district'


class Branch(ModelBase):
    name = models.CharField(max_length=64, null=False)
    district = models.ForeignKey(
        to='District',
        on_delete=models.DO_NOTHING,
        db_column='id_district',
        null=False,
    )

    class Meta:
        db_table = 'branch'


class Product(ModelBase):
    name = models.CharField(max_length=64, null=False)
    cost_price = models.DecimalField(max_digits=16, decimal_places=2, null=False)
    sale_price = models.DecimalField(max_digits=16, decimal_places=2, null=False)
    product_group = models.ForeignKey(
        to='ProductGroup',
        on_delete=models.DO_NOTHING,
        db_column='id_product_group',
        null=False,
    )
    supplier = models.ForeignKey(
        to='Supplier',
        on_delete=models.DO_NOTHING,
        db_column='id_supplier',
        null=False,
    )

    class Meta:
        db_table = 'product'


class ProductGroup(ModelBase):
    name = models.CharField(max_length=64, null=False)
    comission_percent = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    gain_percent = models.DecimalField(max_digits=5, decimal_places=2, null=False)

    class Meta:
        db_table = 'product_group'


class Supplier(ModelBase):
    name = models.CharField(max_length=64, null=False)
    legal_document = models.CharField(max_length=20, null=False)

    class Meta:
        db_table = 'supplier'


class Sale(ModelBase):
    date = models.DateField(null=False)
    customer = models.ForeignKey(
        to='Customer',
        on_delete=models.DO_NOTHING,
        db_column='id_customer',
        null=False,
    )
    branch = models.ForeignKey(
        to='Branch',
        on_delete=models.DO_NOTHING,
        db_column='id_branch',
        null=False,
    )
    employee = models.ForeignKey(
        to='Employee',
        on_delete=models.DO_NOTHING,
        db_column='id_employee',
        null=False,
    )

    class Meta:
        db_table = 'sale'


class SaleProduct(ModelBase):
    quantity = models.DecimalField(max_digits=16, decimal_places=2, null=False)
    sale_price = models.DecimalField(max_digits=16, decimal_places=2, null=False)
    sale = models.ForeignKey(
        to='Sale',
        on_delete=models.DO_NOTHING,
        db_column='id_sale',
        null=False,
    )
    product = models.ForeignKey(
        to='Product',
        on_delete=models.DO_NOTHING,
        db_column='id_product',
        null=False,
    )

    class Meta:
        db_table = 'sale_product'
