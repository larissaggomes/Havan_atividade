from sale import models
from django.db.models import Value, Case, When, CharField

def listar_department():
    return models.Department.objects.all()


def listar_status():
    return models.MaritalStatus.objects.all()


def clientes():
    return models.Customer.objects.all()


def query04():
    queryset = models.Employee.objects.annotate(
        gender_description=Case(
            When(gender=models.Employee.Gender.FEMALE, then=Value('FEMALE')),
            default=Value('MALE'),
            output_field=CharField()
        )
    ).only('id', 'name')
    return queryset
