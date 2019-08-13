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
    Address_of_Employee = models.CharField(null=True,max_length=200, verbose_name='Address of Employee')
    Company_Name = models.CharField(null=True,max_length=200, verbose_name='Company Name')
    Address_of_Company = models.CharField(null=True,max_length=200, verbose_name='Address of Company')
    Role = models.ForeignKey(Role,db_column='Role', on_delete=models.CASCADE, null=True)
    Base_Salary = models.CharField(null=True,max_length=200, verbose_name='Base Salary')
    Date_of_Agreement = models.CharField(null=True,max_length=200, verbose_name='Date of Agreement')
    Start_Date = models.CharField(null=True,max_length=200, verbose_name='Start Date')
    End_Date = models.CharField(null=True,max_length=200, verbose_name='End Date')
    Supervisor_Information = models.CharField(null=True,max_length=200, verbose_name='Supervisor Information')
    Bonus = models.CharField(null=True,max_length=200, verbose_name='Bonus')
    Notice_Period = models.CharField(null=True,max_length=200, verbose_name='Notice Period')
    Other_Compensation = models.CharField(null=True,max_length=200, verbose_name='Other Compensation')
    Non_Monetary_Benefits = models.CharField(null=True,max_length=200, verbose_name='Non Monetary Benefits')
    Health_Insurance = models.CharField(null=True,max_length=200, verbose_name='Health Insurance')
    _401k = models.CharField(null=True,max_length=200, verbose_name='401k')
    At_will = models.CharField(null=True,max_length=200, verbose_name='At will')
    Stock = models.CharField(null=True,max_length=200, verbose_name='Stock')
    Vacation = models.CharField(null=True,max_length=200, verbose_name='Vacation')
    doc= models.ForeignKey(Document,db_column='doc', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Document_Name


