# Generated by Django 5.1.1 on 2024-09-17 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=13),
        ),
    ]
