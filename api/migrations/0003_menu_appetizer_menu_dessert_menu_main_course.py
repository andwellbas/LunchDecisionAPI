# Generated by Django 4.2.3 on 2023-07-28 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_employee_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='appetizer',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='dessert',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='main_course',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
