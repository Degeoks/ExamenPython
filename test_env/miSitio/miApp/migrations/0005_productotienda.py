# Generated by Django 2.1.4 on 2018-12-08 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0004_remove_producto_costoproducto'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoTienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costoProducto', models.PositiveIntegerField()),
                ('codigoProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miApp.Producto')),
            ],
        ),
    ]
