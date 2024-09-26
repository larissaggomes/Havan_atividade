from django.db import models


class ModelBase(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    modified_at = models.DateTimeField(auto_now=True, null=False)
    active = models.BooleanField(default=True, null=False)

    class Meta:
        managed = True
        abstract = True


# Create your models here.
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

    def __str__(self):
        return self.name


class City(ModelBase):
    name = models.CharField(max_length=64, null=False)
    state = models.ForeignKey(
        to='State',
        on_delete=models.DO_NOTHING,
        db_column='id_state',
        null=False
    )

    class Meta:
        db_table = 'city'


class Zone(ModelBase):
    name = models.CharField(max_length=64, null=False)

    class Meta:
        db_table = 'zone'


class District(ModelBase):
    name = models.CharField(max_length=64, null=False)
    city = models.ForeignKey(
        to='City',
        on_delete=models.DO_NOTHING,
        db_column='id_city',
        null=False
    )
    zone = models.ForeignKey(
        to='Zone',
        on_delete=models.DO_NOTHING,
        db_column='id_zone',
        null=False
    )


class Customer(ModelBase):
    class Gender(models.TextChoices):
        MALE = 'M', 'Masculino'
        FEMALE = 'F', 'Feminino'

    name = models.CharField(max_length=64, null=False)
    income = models.DecimalField(max_digits=16, decimal_places=2, null=False)
    gender = models.CharField(max_length=1, null=False, choices=Gender.choices)
    district = models.ForeignKey(
        to='District',
        on_delete=models.DO_NOTHING,
        db_column='id_city',
        null=False
    )
    marital_status = models.ForeignKey(
        to='MaritalStatus',
        on_delete=models.DO_NOTHING,
        db_column='id_marital_status',
        null=False
    )

    class Meta:
        db_table = 'customer'


class Employee(ModelBase):
    class Gender(models.TextChoices):
        MALE = 'M', 'Masculino'
        FEMALE = 'F', 'Feminino'

    name = models.CharField(max_length=64, null=False)
    salary = models.DecimalField(max_digits=16, decimal_places=2, null=False)
    admission_date = models.DateField(null=False)
    birth_date = models.DateField(null=False)
    gender = models.CharField(max_length=1, null=False, choices=Gender.choices)
    department = models.ForeignKey(
        to='Department',
        on_delete=models.DO_NOTHING,
        db_column='id_department',
        null=False
    )
    marital_status = models.ForeignKey(
        to='MaritalStatus',
        on_delete=models.DO_NOTHING,
        db_column='id_marital_status',
        null=False
    )
    district = models.ForeignKey(
        to='District',
        on_delete=models.DO_NOTHING,
        db_column='id_city',
        null=False
    )

    class Meta:
        db_table = 'employee'


class ProductGroup(ModelBase):
    name = models.CharField(max_length=64, null=False)
    commission_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    gain_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=False)

    class Meta:
        db_table = 'product_group'


class Supplier(ModelBase):
    name = models.CharField(max_length=64, null=False)
    legal_document = models.CharField(max_length=20, null=False)

    class Meta:
        db_table = 'supplier'


class Product(ModelBase):
    name = models.CharField(max_length=64, null=False)
    cost_price = models.DecimalField(max_digits=16, decimal_places=2, null=False)
    sale_price = models.DecimalField(max_digits=16, decimal_places=2, null=False)
    supplier = models.ForeignKey(
        to='Supplier',
        on_delete=models.DO_NOTHING,
        db_column='id_supplier',
        null=False
    )
    product_group = models.ForeignKey(
        to='ProductGroup',
        on_delete=models.DO_NOTHING,
        db_column='id_product_group',
        null=False
    )

    class Meta:
        db_table = 'product'


class Branch(ModelBase):
    name = models.CharField(max_length=64, null=False)
    district = models.ForeignKey(
        to='District',
        on_delete=models.DO_NOTHING,
        db_column='id_city',
        null=False
    )

    class Meta:
        db_table = 'branch'


class Sale(ModelBase):
    date = models.DateTimeField(auto_now_add=True, null=False)
    customer = models.ForeignKey(
        to='Customer',
        on_delete=models.DO_NOTHING,
        db_column='id_customer',
        null=False
    )
    employee = models.ForeignKey(
        to='Employee',
        on_delete=models.DO_NOTHING,
        db_column='id_employee',
        null=False
    )
    branch = models.ForeignKey(
        to='Branch',
        on_delete=models.DO_NOTHING,
        db_column='id_branch',
        null=False
    )

    class Meta:
        db_table = 'sale'


class SaleItem(ModelBase):
    sale = models.ForeignKey(
        to='Sale',
        on_delete=models.DO_NOTHING,
        db_column='id_sale',
        null=False
    )
    product = models.ForeignKey(
        to='Product',
        on_delete=models.DO_NOTHING,
        db_column='id_product',
        null=False
    )
    quantity = models.DecimalField(max_digits=16, decimal_places=3, null=False)
    sale_price = models.DecimalField(max_digits=16, decimal_places=2, null=False)

    class Meta:
        db_table = 'sale_item'
