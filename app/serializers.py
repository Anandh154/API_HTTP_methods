from rest_framework import serializers
from app.models import *
<<<<<<< HEAD
class EmployeMS(serializers.ModelSerializer):
    class Meta:
        model=Employe
        fields='__all__'
=======

class ProductMSR(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
>>>>>>> 3def1e2 (first commit)
