# Generated by Django 2.2.1 on 2019-08-31 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UploadMulti', '0002_auto_20190831_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='processed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
