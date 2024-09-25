from sale import models


def listar_department():
    return models.Department.objects.all()


def listar_status():
    return models.MaritalStatus.objects.all()