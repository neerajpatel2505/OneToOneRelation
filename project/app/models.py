# from django.db import models
  
# class VehicleModel(models.Model):
#     reg_no = models.IntegerField()
#     owner = models.CharField(max_length = 100)
#     def __str__(self):
#         return self.owner
  
# class CarModel(models.Model):
#     vehicle = models.OneToOneField(VehicleModel,on_delete = models.CASCADE, primary_key = True)
#     car_model = models.CharField(max_length = 100)
#     def __str__(self):
#         return self.car_model
from django.db import models

# Aadhar Model creat
class AadharModel(models.Model):
    aadhar_no=models.IntegerField()
    def __str__(self):
        return str(self.aadhar_no)

class StudentModel(models.Model):
    stu_name = models.CharField(max_length=100)
    stu_address = models.CharField(max_length=200)  
    # CASCADE - Means if we delete aadhar_no then related StudentModel also deleted.
    # aadhar_no = models.OneToOneField(AadharModel,on_delete=models.CASCADE,primary_key=True)
    
    # PROTECT - Means if you want delet aadhar no then it is require to delete first alloted student name.
    aadhar_no = models.OneToOneField(AadharModel, on_delete=models.PROTECT,primary_key=True)
    def __str__(self):
        return self.stu_name 