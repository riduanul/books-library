# Generated by Django 4.2.7 on 2024-01-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_remove_borrow_users_borrow_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='is_borrow',
            field=models.BooleanField(default=False),
        ),
    ]
