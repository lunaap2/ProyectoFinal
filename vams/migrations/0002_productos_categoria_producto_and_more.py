# Generated by Django 5.1.1 on 2024-10-15 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='categoria_producto',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='productos',
            name='producto_vendido',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='productos',
            name='descripcion_producto',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='productos',
            name='disponibilidad',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='productos',
            name='nombre_producto',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='productos',
            name='precio',
            field=models.FloatField(default=None),
        ),
    ]
