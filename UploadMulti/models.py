from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='docs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Detail(models.Model):
    Document_Name = models.CharField(max_length=200, verbose_name='Document Name', primary_key=True)
    Employee_Name = models.CharField(null=True,max_length=200, verbose_name='Employee Name')
    Address_of_Employee = models.CharField(null=True,max_length=200, verbose_name='Address of Employee')
    Company_Name = models.CharField(null=True,max_length=200, verbose_name='Company Name')
    Address_of_Company = models.CharField(null=True,max_length=200, verbose_name='Address of Company')
    Role = models.CharField(null=True,max_length=200, verbose_name='Role')
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

    def __str__(self):
        return self.Document_Name
    
