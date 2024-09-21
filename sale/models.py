from django.db import models

# Create your models here.
class ModelBase(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

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
        on_delete=models.DO_NOTHING(),
        null=False,
    )

    class Meta:
        db_table = 'city'


class Employee(ModelBase):
    name = models.CharField(max_length=64, null=False)
    department = models.ForeignKey(
        to='Department',
        on_delete=models.DO_NOTHING(),
        null=False,
        blank=True,
    )

    class Meta:
        db_table = 'employee'
