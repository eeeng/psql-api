from datetime import date
import imp
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import importlib_metadata
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from sympy import Id

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializers, EmployeeSerializers

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        department_serializers = DepartmentSerializers(departments, many=True)
        return JsonResponse(department_serializers.data, safe=False)
    elif request.method =='POST':
        department_data = JSONParser().parse(request)
        department_serializers = DepartmentSerializers(data=department_data)
        if department_serializers.is_valid():
            department_serializers.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee= Employees.object.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer=EmployeeSerializers(employee, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        employee= Employees.object.get(EmployeeId=Id)
        employee.delete()
        return JsonResponse("Delete Successfully", safe=False)
@csrf_exempt
def saveFile(request):
    file     = request.FILES['file']
    file_name= default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
    