from django.db import models
from sqlalchemy import true
from rest_framework import serializers
from EmployeeApp.models import Departments, Employees

class DepartmentSerializers(serializers.ModelSerializers):
    class Meta:
        model = Departments
        fields=('DepartmentId', 'DepartmentName')

class EmployeeSerializers(serializers.ModelSerializers):
    class Meta:
        model = Employees
        fields=('EmployeeId', 'EmployeeName', 'Department', 'DateOfJoining', 'PhotoFileName')
