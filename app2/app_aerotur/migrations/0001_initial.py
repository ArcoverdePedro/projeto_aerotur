# Generated by Django 5.1.5 on 2025-01-15 02:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('quantidade_estoque', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
