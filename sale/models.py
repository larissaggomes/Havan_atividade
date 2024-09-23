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
