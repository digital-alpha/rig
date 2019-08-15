# Generated by Django 2.2.1 on 2019-08-15 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UploadMulti', '0003_auto_20190815_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='Address_of_Company',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Address of Company'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Address_of_Employee',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Address of Employee'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='At_will',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='At will'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Base_Salary',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Base Salary'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Bonus',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Bonus'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Company_Name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Company Name'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Date_of_Agreement',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Date of Agreement'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='End_Date',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Health_Insurance',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Health Insurance'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Non_Monetary_Benefits',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Non Monetary Benefits'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Notice_Period',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Notice Period'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Other_Compensation',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Other Compensation'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Roles',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Start_Date',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Stock',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Stock'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Supervisor_Information',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Supervisor Information'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Vacation',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Vacation'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='_401k',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='401k'),
        ),
    ]
