# Generated by Django 3.2.3 on 2021-07-01 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0008_usuario_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='foto_pro',
            field=models.ImageField(null=True, upload_to='producto'),
        ),
    ]
