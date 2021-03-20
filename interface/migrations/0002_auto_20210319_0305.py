# Generated by Django 3.1.3 on 2021-03-19 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='Devui',
            field=models.TextField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='devices',
            name='IdLora',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='groupes',
            name='Groupe',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='groupes',
            name='IdGroupe',
            field=models.TextField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sousgroupes',
            name='SousGroupe',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tags',
            name='Tag',
            field=models.TextField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
