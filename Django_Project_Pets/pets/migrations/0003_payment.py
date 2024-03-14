# Generated by Django 5.0.1 on 2024-02-28 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_cartitem_product_delete_pets_delete_toys_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
