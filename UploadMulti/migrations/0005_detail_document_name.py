# Generated by Django 2.2.1 on 2019-06-25 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UploadMulti', '0004_auto_20190624_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='Document_Name',
            field=models.CharField(default=1, max_length=200, verbose_name='Document Name'),
            preserve_default=False,
        ),
    ]
