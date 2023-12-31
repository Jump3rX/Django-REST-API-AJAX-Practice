# Generated by Django 4.0.4 on 2023-11-07 11:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('food_type', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('table_number', models.CharField(max_length=100, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('total', models.IntegerField(null=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.IntegerField(null=True)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.orders')),
            ],
        ),
    ]
