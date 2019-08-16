from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

from django.contrib.auth import get_user_model
User = get_user_model()
class Document(models.Model):
    
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='docs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        name = self.file.name
        name = name.replace('docs/', '')
        name = name.replace('.txt', '')
        return name

class Role(models.Model):
   
    Role_Name = models.CharField(null=True,max_length=200, verbose_name='Role_Name',unique=True)

    def __str__(self):
        return self.Role_Name

class Detail(models.Model):
    
    Document_Name = models.CharField(max_length=200, verbose_name='Document Name')
    Employee_Name = models.CharField(null=True,max_length=200, verbose_name='Employee Name')
    Address_of_Employee = models.CharField(null=True,max_length=200, verbose_name='Address of Employee',blank=True)
    Company_Name = models.CharField(null=True,max_length=200, verbose_name='Company Name',blank=True)
    Address_of_Company = models.CharField(null=True,max_length=200, verbose_name='Address of Company',blank=True)
    Roles=models.CharField(null=True,max_length=200, verbose_name='Role',blank=True)
    Base_Salary = models.CharField(null=True,max_length=200, verbose_name='Base Salary',blank=True)
    Date_of_Agreement = models.CharField(null=True,max_length=200, verbose_name='Date of Agreement',blank=True)
    Start_Date = models.CharField(null=True,max_length=200, verbose_name='Start Date',blank=True)
    End_Date = models.CharField(null=True,max_length=200, verbose_name='End Date',blank=True)
    Supervisor_Information = models.CharField(null=True,max_length=200, verbose_name='Supervisor Information',blank=True)
    Bonus = models.CharField(null=True,max_length=200, verbose_name='Bonus',blank=True)
    Notice_Period = models.CharField(null=True,max_length=200, verbose_name='Notice Period',blank=True)
    Other_Compensation = models.CharField(null=True,max_length=200, verbose_name='Other Compensation',blank=True)
    Non_Monetary_Benefits = models.CharField(null=True,max_length=200, verbose_name='Non Monetary Benefits',blank=True)
    Health_Insurance = models.CharField(null=True,max_length=200, verbose_name='Health Insurance',blank=True)
    _401k = models.CharField(null=True,max_length=200, verbose_name='401k',blank=True)
    At_will = models.CharField(null=True,max_length=200, verbose_name='At will',blank=True)
    Stock = models.CharField(null=True,max_length=200, verbose_name='Stock',blank=True)
    Vacation = models.CharField(null=True,max_length=200, verbose_name='Vacation',blank=True)
    doc= models.ForeignKey(Document,db_column='doc', on_delete=models.CASCADE, null=True)
    Role_ref = models.ForeignKey(Role,db_column='Role_ref', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Document_Name


