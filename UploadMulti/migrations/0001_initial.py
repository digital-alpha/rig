# Generated by Django 2.2.1 on 2019-08-16 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Role_Name', models.CharField(max_length=200, null=True, unique=True, verbose_name='Role_Name')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('file', models.FileField(upload_to='docs/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Document_Name', models.CharField(max_length=200, verbose_name='Document Name')),
                ('Employee_Name', models.CharField(max_length=200, null=True, verbose_name='Employee Name')),
                ('Address_of_Employee', models.CharField(blank=True, max_length=200, null=True, verbose_name='Address of Employee')),
                ('Company_Name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Company Name')),
                ('Address_of_Company', models.CharField(blank=True, max_length=200, null=True, verbose_name='Address of Company')),
                ('Roles', models.CharField(blank=True, max_length=200, null=True, verbose_name='Role')),
                ('Base_Salary', models.CharField(blank=True, max_length=200, null=True, verbose_name='Base Salary')),
                ('Date_of_Agreement', models.CharField(blank=True, max_length=200, null=True, verbose_name='Date of Agreement')),
                ('Start_Date', models.CharField(blank=True, max_length=200, null=True, verbose_name='Start Date')),
                ('End_Date', models.CharField(blank=True, max_length=200, null=True, verbose_name='End Date')),
                ('Supervisor_Information', models.CharField(blank=True, max_length=200, null=True, verbose_name='Supervisor Information')),
                ('Bonus', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bonus')),
                ('Notice_Period', models.CharField(blank=True, max_length=200, null=True, verbose_name='Notice Period')),
                ('Other_Compensation', models.CharField(blank=True, max_length=200, null=True, verbose_name='Other Compensation')),
                ('Non_Monetary_Benefits', models.CharField(blank=True, max_length=200, null=True, verbose_name='Non Monetary Benefits')),
                ('Health_Insurance', models.CharField(blank=True, max_length=200, null=True, verbose_name='Health Insurance')),
                ('_401k', models.CharField(blank=True, max_length=200, null=True, verbose_name='401k')),
                ('At_will', models.CharField(blank=True, max_length=200, null=True, verbose_name='At will')),
                ('Stock', models.CharField(blank=True, max_length=200, null=True, verbose_name='Stock')),
                ('Vacation', models.CharField(blank=True, max_length=200, null=True, verbose_name='Vacation')),
                ('Role_ref', models.ForeignKey(db_column='Role_ref', null=True, on_delete=django.db.models.deletion.CASCADE, to='UploadMulti.Role')),
                ('doc', models.ForeignKey(db_column='doc', null=True, on_delete=django.db.models.deletion.CASCADE, to='UploadMulti.Document')),
            ],
        ),
    ]
