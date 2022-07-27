from django.db import models
from sqlalchemy import true

# Create your models here.


class Departments(models.Models):
    DepartmenId    = models.AutoField(primary_key = True)
    DepartmentName = models.CharField(max_length = 500)
    
class Employees(models.Models):
    EmployeeId       = models.AutoField(primary_key = True)
    EmployeeName     = models.CharField(max_length = 500)
    Department       = models.CharField(max_length = 500)
    DateOfJoining    = models.DateField()
    PhotoFileName    = models.CharField(max_length = 500)
    