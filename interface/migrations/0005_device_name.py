# Generated by Django 3.1.3 on 2021-03-20 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0004_auto_20210319_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='Name',
            field=models.CharField(default='NRGYBOX', max_length=50),
        ),
    ]
