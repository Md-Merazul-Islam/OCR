# Generated by Django 5.0.4 on 2024-08-20 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocrdocument',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
