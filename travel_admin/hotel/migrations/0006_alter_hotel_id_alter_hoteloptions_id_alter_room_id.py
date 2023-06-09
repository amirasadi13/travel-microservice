# Generated by Django 4.1.4 on 2023-05-13 20:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_rename_price_room_price_per_night'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hoteloptions',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
