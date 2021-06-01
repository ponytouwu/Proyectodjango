# Generated by Django 3.2.3 on 2021-06-01 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0002_auto_20210531_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='id_carrito',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id del carrito'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='id_categoria',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id de la categoria'),
        ),
        migrations.AlterField(
            model_name='comuna',
            name='id_comuna',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la comuna'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='id_contacto',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id del contacto'),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='id_direccion',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la direccion'),
        ),
        migrations.AlterField(
            model_name='marca',
            name='id_marca',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id de la marca'),
        ),
        migrations.AlterField(
            model_name='pro_carrito',
            name='id_pro_carr',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id del producto en el carrito'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_producto',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id del producto'),
        ),
        migrations.AlterField(
            model_name='tipo_usuario',
            name='id_usu_tip',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id del usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id_usuario',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id del contacto'),
        ),
    ]
