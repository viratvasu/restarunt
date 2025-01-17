# Generated by Django 3.0.6 on 2020-07-12 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('discription', models.CharField(max_length=260)),
                ('is_veg', models.BooleanField()),
                ('original_price', models.IntegerField()),
                ('discount_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_phone', models.CharField(max_length=10)),
                ('status', models.CharField(choices=[('Ordered', 'Ordered'), ('Deliveried', 'Deliveried'), ('Cancelled', 'Cancelled')], max_length=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product')),
            ],
        ),
    ]
